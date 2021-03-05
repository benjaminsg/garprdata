import config
import requests
from datetime import datetime
import json
import time
import logging

players = config.players
maxRetries = config.maxRetries
seasonStart = config.seasonStart
seasonEnd = config.seasonEnd

cont = True

first_player_name = ''

while cont:
    print('Enter first player (or \'q\' to quit)')
    user_func = input()
    print()

    try:
        first_player_name = str(user_func)

    except ValueError:
        print("Invalid input. Please input a valid player.")
        print()

    else:
        first_player = None
        first_player_name = first_player_name.lower()
        if(first_player_name == 'q'):
            cont = False
        else:
            for player in players:
                if player.name.lower() == first_player_name:
                    first_player = player
            if(first_player == None):
                print("Invalid input. Please input a valid player.")
                print()
            else:
                cont2 = True
                second_player_name = ''
                while(cont2):
                    print('Enter second player (or \'b\' to go back)')
                    user_func = input()
                    print()
                
                    try:
                        second_player_name = str(user_func)
                
                    except ValueError:
                        print("Invalid input. Please input a valid player.")
                        print()
                        
                    else:
                        second_player = None
                        second_player_name = second_player_name.lower()
                        if(second_player_name == 'b'):
                            cont2 = False
                        else:
                            if(second_player_name == first_player_name):
                                print("Invalid input. Players cannot be the same.")
                            else:
                                for player in players:
                                    if player.name.lower() == second_player_name:
                                        second_player = player
                                        
                                        url = "https://notgarpr.com:3001/" + config.region + "/matches/" + first_player.id + "?opponent=" + second_player.id
                                        
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
                                            # check to make sure the match date is within the timeframe
                                            
                                            print("Restrict results to within season only (y/n)?")
                                            user_resp = input()
                                            print()
                                        
                                            try:
                                                user_resp = str(user_resp)
                                        
                                            except ValueError:
                                                print("Invalid input. Please input \'y\' for yes or \'n\' for no.")
                                                print()
                                        
                                            else:
                                                wins = 0
                                                losses = 0
                                                played = False
                                                
                                                tournament_names = []
                                                results = []
                                                tournament_dates = []
                                                if(user_resp.lower() == 'yes' or user_resp.lower() == 'y'):
                                                    for match in data['matches']:
#                                                        print(match)
                                                        date = datetime.strptime(match['tournament_date'], '%m/%d/%y')
                                                        if seasonStart <= date <= seasonEnd:
                                                            # read the match result (win or loss), update the counts accordingly, and indicate that the
                                                            # players have played
                                                            tournament_name = match['tournament_name']
                                                            if(len(tournament_name) > 20):
                                                                tournament_name = tournament_name[:18] + '..'
                                                            tournament_names.append(tournament_name)
                                                            results.append(match['result'])
                                                            tournament_dates.append(match['tournament_date'])
                                                            if match['result'] == 'win':
                                                                wins += 1
                                                                played = True
                                                            # check to make sure match isn't excluded (in which case it would have a result of 'excluded')
                                                            elif match['result'] == 'lose':
                                                                losses += 1
                                                                played = True
                                                else:
                                                    for match in data['matches']:
                                                        tournament_name = match['tournament_name']
                                                        if(len(tournament_name) > 20):
                                                            tournament_name = tournament_name[:18] + '..'
                                                        tournament_names.append(tournament_name)
                                                        results.append(match['result'])
                                                        tournament_dates.append(match['tournament_date'])
                                                        if match['result'] == 'win':
                                                            wins += 1
                                                            played = True
                                                        # check to make sure match isn't excluded (in which case it would have a result of 'excluded')
                                                        elif match['result'] == 'lose':
                                                            losses += 1
                                                            played = True
                                                if(played):
                                                    print(first_player.name + " vs. " + second_player.name)
                                                    print(str(wins) + " - " + str(losses))
                                                    print()
                                                    print("{:<10} {:<20} {:<10}".format('Date','Tournament','Winner'))
                                                    for i in range(len(results)):
                                                        winner = first_player.name if results[i] == 'win' else second_player.name
                                                        print ("{:<10} {:<20} {:<10}".format(tournament_dates[i],tournament_names[i],winner))
                                                    print()
                                                    cont2 = False
                                                else:
                                                    print("These players have never played.")
                                                    cont2 = False
                                        else:
                                            print("These players have never played.")
                                            cont2 = False