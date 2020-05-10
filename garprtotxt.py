import json
import requests
from datetime import datetime
import time
import settings

players = settings.players
seasonstart = settings.seasonstart
seasonend = settings.seasonend
maxretries = settings.maxretries

#initialize number of retries to access the csv file
numretries = 0

#initialize boolean to determine if we can write to csv file
txtWrite = False

#create loop to try to access file
while(not txtWrite):

    try:
        #open text file to write output to
        results = open("h2hs.txt","a") 
        
        #specify that we can now write
        txtWrite = True
        
    #if a keyboardinterupt occurs abort execution
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        #if we have exceeded the maximum number of retries raise an
        #exception
        if(numretries > maxretries):
            raise Exception("Exceeded maximum number of retries to access the file")
        #otherwise sleep for five seconds and then retry the request
        print("Permission to access txt file denied, please close any programs with the file open")
        print("Waiting to retry write request to file")
        time.sleep(5)
        print("Retrying write request")
                    
        #increment number of retries then retry connection
        numretries += 1
        
        continue

#truncate text file to clear it
results.truncate()

for player in players:
    
    #for each opponent (every other player)
    for opponent in players:
        
        #check to make sure opponent is different from player
        if(player != opponent):
            
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
            
            #boolean to check if players have played during timeframe
            played = False
            
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
                        if(match['result'] == 'win'):
                            wins += 1
                            played = True
                        #check to make sure match isn't excluded (in which case
                        #it would have a result of 'excluded')
                        elif(match['result'] == 'lose'):
                            losses += 1
                            played = True
             
            #handle additional set Slox and DrLobster played OOR               
            if(player == settings.Slox and opponent == settings.DrLobster):
                wins += 1
                played = True
            elif(player == settings.DrLobster and opponent == settings.Slox):
                losses += 1
                played = True    
                
            #if the players have played, print the head-to-head to the console
            #and record the win and loss counts in the playerlist
            if(played):
                print(player.name + " vs. " + opponent.name + "\r\n")
                print(str(wins) + " - " + str(losses))

                #write matchup information to text file
                results.write(player.name + " vs. " + opponent.name + "\r\n")
                results.write(str(wins) + " - " + str(losses) + "\r\n")

#indicate the program has completed (typically takes a while, time will
#increase quadratically with more opponents)
print("done")