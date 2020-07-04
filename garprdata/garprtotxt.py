import json
import requests
from datetime import datetime
import time
import config
import logging

players = config.players
seasonStart = config.seasonStart
seasonEnd = config.seasonEnd
maxRetries = config.maxRetries

# initialize number of retries to access the csv file
numRetries = 0

# initialize boolean to determine if we can write to csv file
txtWrite = False

# create loop to try to access file
while not txtWrite:

    try:
        # open text file to write output to
        results = open("outputs/h2hs.txt", "a")

        # specify that we can now write
        txtWrite = True

    # if a KeyboardInterrupt occurs abort execution
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception as e:
        # log the exception
        logging.exception(e)
        # if we have exceeded the maximum number of retries raise an
        # exception
        if numRetries > maxRetries:
            raise Exception("Exceeded maximum number of retries to access the file")
        # otherwise sleep for five seconds and then retry the request
        print("Permission to access txt file denied, please close any programs with the file open")
        print("Waiting to retry write request to file")
        time.sleep(5)
        print("Retrying write request")

        # increment number of retries then retry connection
        numRetries += 1

        continue

# truncate text file to clear it
results.truncate()

for player in players:

    # for each opponent (every other player)
    for opponent in players:

        # check to make sure opponent is different from player
        if player != opponent:

            # generate URL to pull head-to-head json data from
            url = "https://notgarpr.com:3001/newengland/matches/" + player.id + "?opponent=" + opponent.id + "&fbclid=IwAR3V8QosRC1_d-tBrPtSLB7pHKWuwXlea6fuKVjU645bq6dKNEshOvL7tv8"

            # initialize response
            response = ''

            # initialize number of retries to connect to server
            numRetries = 0

            # create loop to try to generate response
            while response == '':
                try:
                    # load json response from url
                    response = requests.get(url)
                    break
                # if a KeyboardInterrupt occurs abort execution
                except (KeyboardInterrupt, SystemExit):
                    raise
                # if an exception occurs due to connection refusal
                except Exception as e:
                    # log the exception
                    logging.exception(e)
                    # if we have exceeded the maximum number of retries raise an exception
                    if numRetries > maxRetries:
                        raise Exception("Exceeded maximum number of retries to connect to the server")
                    # otherwise sleep for five seconds and then retry the request
                    print("Connection refused by the server")
                    print("Waiting to retry")
                    time.sleep(5)
                    print("Retrying connection")

                    # increment number of retries then retry connection
                    numRetries += 1
                    continue

            # load data from the response
            data = json.loads(response.text)

            # initialize counts of wins and losses for given matchup
            wins = 0
            losses = 0

            # boolean to check if players have played during time frame
            played = False

            # sometimes GARPR will not return match data (this only happens when the players have not played, but
            # sometimes GARPR will also just give match data with 0s), check for this case to avoid index not found
            # error
            if 'matches' in data:
                # look at each match sub-dictionary within the pulled data
                for match in data['matches']:
                    # check to make sure the match date is within the timeframe
                    date = datetime.strptime(match['tournament_date'], '%m/%d/%y')
                    if seasonStart <= date <= seasonEnd:
                        # read the match result (win or loss), update the counts accordingly, and indicate that the
                        # players have played
                        if match['result'] == 'win':
                            wins += 1
                            played = True
                        # check to make sure match isn't excluded (in which case it would have a result of 'excluded')
                        elif match['result'] == 'lose':
                            losses += 1
                            played = True

            # handle additional set Slox and DrLobster played OOR               
            if player == config.Slox and opponent == config.DrLobster:
                wins += 1
                played = True
            elif player == config.DrLobster and opponent == config.Slox:
                losses += 1
                played = True

                # if the players have played, print the head-to-head to the console and record the win and loss counts
                # in the playerlist
            if played:
                print(player.name + " vs. " + opponent.name + "\r\n")
                print(str(wins) + " - " + str(losses))

                # write matchup information to text file
                results.write(player.name + " vs. " + opponent.name + "\r\n")
                results.write(str(wins) + " - " + str(losses) + "\r\n")

# indicate the program has completed (typically takes a while, time will increase quadratically with more opponents)
print("done")
