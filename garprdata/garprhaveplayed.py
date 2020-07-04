import json
import requests
from datetime import datetime
import time
import config
import logging

players = config.players
seasonStart = config.prevseasonStart
seasonEnd = config.prevseasonEnd
maxRetries = config.maxRetries

# initialize number of retries to access the csv file
numRetries = 0

# initialize boolean to determine if we can write to csv file
txtWrite = False

# create loop to try to access file
while not txtWrite:

    try:
        # open text file to write output to
        results = open("outputs/matchups.txt", "a")

        # specify that we can now write
        txtWrite = True

    # if a KeyboardInterrupt occurs abort execution
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception as e:
        # log the exception
        logging.exception(e)
        # if we have exceeded the maximum number of retries raise an exception
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

# truncate the text file to remove old results
results.truncate()

# look at each player in the list of players
for player in players:

    # for each opponent (every other player)
    for opponent in players:

        # check to make sure opponent is different from player
        if player != opponent:

            # print matchup title to console
            print(player.name + " vs. " + opponent.name)

            results.write(player.name + " vs. " + opponent.name + "\r\n")

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
                    # if we have exceeded the maximum number of retries raise an
                    # exception
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

            data = json.loads(response.text)

            # boolean to check if players have played during timeframe
            played = False

            # sometimes GARPR will not return match data (this only happens when the players have not played, but
            # sometimes GARPR will also just give match data with 0s), check for this case to avoid index not found
            # error
            if 'matches' in data:
                # look at each match sub-dictionary within the pulled data
                for match in data['matches']:
                    # check to make sure the match date is within the time frame
                    date = datetime.strptime(match['tournament_date'], '%m/%d/%y')
                    # if a match is found within the time frame update the played
                    # boolean and break out of the loop
                    if seasonStart <= date <= seasonEnd:
                        # check to make sure match isn't excluded
                        if match['result'] != 'excluded':
                            played = True
                            break
            # write the resulting played boolean to the output text file
            results.write(str(played) + "\r\n")
            # print the played result to the console
            print(played)

results.close()

# indicate the program has completed (typically takes a while, time will increase quadratically with more opponents in
# worst case)
print("done")
