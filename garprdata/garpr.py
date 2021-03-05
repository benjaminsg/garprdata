import json
import requests
from datetime import datetime
import csv
import time
import config
import logging

# uncomment for reading to text file
# results = open("h2hs.txt","a")

# initialize the results list
resultsList = []

# initialize the list of headings (containing opponent names)
headingsList = ['Players (W / L)']

players = config.players
seasonStart = config.seasonStart
seasonEnd = config.seasonEnd
maxRetries = config.maxRetries

for player in players:

    # add wins and losses vs. player to headings list
    headingsList.append(player.name + ' W')
    headingsList.append(player.name + ' L')

    # initialize list of player wins and losses
    playerList = [player.name]

    # for each opponent (every other player)
    for opponent in players:

        # check to make sure opponent is different from player
        if player != opponent:

            # generate URL to pull head-to-head json data from
            url = "https://notgarpr.com:3001/" + config.region + "/matches/" + player.id + "?opponent=" + opponent.id

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

            # load data from the reponse
            data = json.loads(response.text)

            # initialize counts of wins and losses for given matchup
            wins = 0
            losses = 0

            # boolean to check if players have played during timeframe
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

            # if the players have played, print the head-to-head to the console and record the win and loss counts in
            # the playerList
            if played:
                print(player.name + " vs. " + opponent.name + "\r\n")
                print(str(wins) + " - " + str(losses))
                # uncomment to write to text file
                # results.write(player.name + " vs. " + opponent.name + "\r\n")
                # results.write(str(wins) + " - " + str(losses) + "\r\n")
                playerList.append(str(wins))
                playerList.append(str(losses))
            # if the players have not played, append empty strings to the player list to match the desired csv output
            else:
                playerList.append('')
                playerList.append('')
        # similarly create empty strings if there is no match data for the given matchup
        else:
            playerList.append('')
            playerList.append('')
    # add given player list to end of the results list to create one list of all player data
    resultsList.append(playerList)

# once all matchups have been recorded, insert the completed list of headings at the beginning of the resultsList
resultsList.insert(0, headingsList)

# initialize number of retries to access the csv file
numRetries = 0

# initialize boolean to determine if we can write to csv file
csvWrite = False

# create loop to try to access file
while not csvWrite:

    try:
        # open the csv output file and avoid creating extra spacing lines
        csvFile = open("outputs/h2hresults.csv", "w", newline='')

        # specify that we can now write
        csvWrite = True

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
        print("Permission to access csv file denied, please close any programs with the file open")
        print("Waiting to retry write request to file")
        time.sleep(5)
        print("Retrying write request")

        # increment number of retries then retry connection
        numRetries += 1

        continue

# truncate the csv file to remove old results
csvFile.truncate(0)

# write each element in the results list to the csv file
with csvFile:
    csv
    writer = csv.writer(csvFile)
    writer.writerows(resultsList)
csvFile.close()

# indicate the program has completed (typically takes a while, time will increase quadratically with more opponents)
print("done")
