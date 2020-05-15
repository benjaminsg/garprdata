import json
import requests
from datetime import datetime
import time
import settings

#initialize the results list
resultslist = []

#initialize the list of headings (containing opponent names)
headingslist = ['Regions (W / L)']

players = settings.players
seasonstart = settings.seasonstart
seasonend = settings.seasonend
maxretries = settings.maxretries

regionmatches = {}

for player in players:
    
    #for each opponent (every other player)
    for opponent in players:
    
        #boolean to check if players have played during timeframe
        played = False
        
        #check to make sure opponent is different from player
        if(player != opponent):

            if(player.state != opponent.state):

                #generate URL to pull head-to-head json data from
                url = "https://notgarpr.com:3001/newengland/matches/" + player.id + "?opponent=" + opponent.id + "&fbclid=IwAR3V8QosRC1_d-tBrPtSLB7pHKWuwXlea6fuKVjU645bq6dKNEshOvL7tv8"

                #initialize response
                response = ''

                #initialize number of retries to connect to server
                numretries = 0

                #create loop to try to generate response
                while(response == ''):
                    try:
                        #load json response from url
                        response = requests.get(url)
                        break
                    #if a keyboardinterupt occurs abort execution
                    except (KeyboardInterrupt, SystemExit):
                        raise
                    #if an exception occurs due to connection refusal
                    except:
                        #if we have exceeded the maximum number of retries raise an
                        #exception
                        if(numretries > maxretries):
                            raise Exception("Exceeded maximum number of retries to connect to the server")
                        #otherwise sleep for five seconds and then retry the request
                        print("Connection refused by the server")
                        print("Waiting to retry")
                        time.sleep(5)
                        print("Retrying connection")
    
                        #increment number of retries then retry connection
                        numretries += 1
                        continue
    
                #load data from the reponse
                data = json.loads(response.text)

                #initialize counts of wins and losses for given matchup
                wins = 0
                losses = 0

                #sometimes GARPR will not return match data (this only happens when
                #the players have not played, but sometiems GARPR will also just
                #give match data with 0s), check for this case to avoid index not
                #found error
                if('matches' in data):
                    #look at each match sub-dictionary within the pulled data
                    for match in data['matches']:
                        #check to make sure the match date is within the timeframe
                        date = datetime.strptime(match['tournament_date'], '%m/%d/%y')
                        if(seasonstart <= date <= seasonend):
                            #read the match result (win or loss), update the
                            #counts accordingly, and indicate that the players have
                            #played
                            rmexists = False
                            regionmatchup = player.state + ' vs. ' + opponent.state
                            if(regionmatchup in regionmatches):
                                rmexists = True
                            if(match['result'] == 'win'):
                                if(rmexists):
                                    regionmatches[regionmatchup][0] += 1
                                else:
                                    regionmatches[regionmatchup] = [1, 0]
                                wins += 1
                                played = True
                            #check to make sure match isn't excluded (in which case
                            #it would have a result of 'excluded')
                            elif(match['result'] == 'lose'):
                                if(rmexists):
                                    regionmatches[regionmatchup][1] += 1
                                else:
                                    regionmatches[regionmatchup] = [0, 1]
                                losses += 1
                                played = True
                            
            if(played):
                print(player.name + " vs. " + opponent.name + "\r\n")
                print(str(wins) + " - " + str(losses))
                    
regionmatches['CT vs. NH'][0] += 1
regionmatches['NH vs. CT'][1] += 1

print(regionmatches)

#indicate the program has completed (typically takes a while, time will
#increase quadratically with more opponents)
print("done")