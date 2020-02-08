import json
import requests
from datetime import datetime
import csv
import time

#Player class
class Player:
    def __init__(self, id, name):
        #id taken from GARPR player page
        self.id = id
        #name is name that will display in all output formats
        self.name = name
    
#specify maximum number of retries that can occur during request to the server    
maxretries = 20
    
#specify start and endtimes of season to collect data from (can be any timeframe)
seasonstart = datetime(2019, 9, 23)
seasonend = datetime(2020, 3, 22)

#create all players
AdmiralZhao = Player('58cd956a1d41c8259fa1fd0b', 'Admiral Zhao')
Alt = Player('5c65f982421aa93db94e98a5', 'Alt')
Arcade = Player('58cc88171d41c8259fa1fc21', 'Arcade')
Artelind = Player('58d20b761d41c8259fa1ff7b', 'Artelind')
Arty = Player('53c64c738ab65f6e27751221', 'Arty')
Bank = Player('59ed7c721d41c84361b79498', 'Bank')
BeastBoy = Player('5d6a8bb3421aa954d874ad46', 'BeastBoy')
BigJoig = Player('545c83e88ab65f126349d8bb', 'BigJoig')
BigRedAnimeBike = Player('58752d371d41c82e80d558a3', 'BigRedAnimeBike')
Bonfire10 = Player('58c7303b1d41c8259fa1f8dd', 'bonfire10')
BonkCushy = Player('542cf48e8ab65f5dcb8ce4ab', 'BonkCushy')
Clutch = Player('5d698f0b421aa954d874acfb', 'Clutch')
CNIU = Player('58cc8c0f1d41c8259fa1fc49', 'CNIU')
Coach = Player('5c6ef669421aa93db94e9954', 'Coach')
Deadstock = Player('59fdf5cf1d41c84361b79b8e', 'Deadstock')
Dimension = Player('5b16ba781d41c86e982900e4', 'Dimension')
DrewNG = Player('596272821d41c840fdcf8804', 'DrewNG')
DrLobster = Player('5d4e3f57421aa954d874ac18', 'DrLobster')
Dudutsai = Player('58c732681d41c8259fa1f905', 'dudutsai')
Een = Player('59ed70bd1d41c84361b79428', 'Een')
Feo = Player('5d818416421aa954d874aed1', 'Feo')
Ferox = Player('58cc6fc61d41c8259fa1fb6b', 'Ferox')
FutureShock = Player('5ade76ef1d41c852c7240f91', 'Future Shock')
Giraffe = Player('5d423a5a421aa954d874ab76', 'Giraffe')
Glasper = Player('58d09a571d41c8259fa1fe86', 'Glasper')
Glock = Player('5a4ba1961d41c84881946784', 'glock in my toyota')
Golden = Player('58c7303b1d41c8259fa1f8d2', 'Golden')
Guex = Player('58c73fce1d41c8259fa1fa3d', 'Guex')
Guillotine = Player('5d295939421aa90f9fc1bd97', 'Guillotine')
GWM420 = Player('5a4ba23b1d41c84881946788', 'GWM420')
Hexjo = Player('5d6fe5d9421aa954d874adfb', 'Hexjo')
Hysteric = Player('5b633156421aa91fa088af7a', 'Hysteric')
IOA = Player('58c72fd21d41c8259fa1f8c9', 'IOA')
JNaut = Player('58c7317e1d41c8259fa1f8e3', 'JNaut')
Joyboy = Player('58c73c7e1d41c8259fa1f9c5', 'Joyboy')
Kalvar = Player('58c726dd1d41c8259fa1f870', 'Kalvar')
Kikoho = Player('5b40def21d41c8456a883413', 'Kikoho')
Klaps = Player('58cc6fc61d41c8259fa1fb57', 'Klaps')
Kota = Player('58cc6fc61d41c8259fa1fb6a', 'Kota')
Lint = Player('545c8e5f8ab65f12c01061ca', 'lint')
Lochist = Player('5c86c4d1421aa93db94e9ab6', 'Lochist')
Louis = Player('5ba19af6421aa91fa088b641', 'Louis')
Meep = Player('58c73d181d41c8259fa1f9d0', 'Meep')
MrHeat = Player('59ed78aa1d41c84361b7947c', 'Mr. Heat')
Nugget = Player('58c729f41d41c8259fa1f8a2', 'Nugget')
Ok = Player('5d295678421aa90f9fc1bd83', 'WAS | Ok')
Omar = Player('5d16d616421aa90f9fc1bc56', 'Omar')
Palika = Player('58cc88171d41c8259fa1fc20', 'Palika')
Peacecraft = Player('587c636d1d41c82e80d55aaf', 'M. Peacecraft')
PJ = Player('542cf4d08ab65f5e0c6e0751', 'PJ')
Poonpounder = Player('5e2fcf55421aa93e12ba4946', 'Poonpounder')
Project = Player('58cc748e1d41c8259fa1fbb8', 'Project')
PSai = Player('5d82976f421aa954d874af04', 'PSai')
RyuCloud = Player('58c739fa1d41c8259fa1f97f', 'RyuCloud')
Scooby = Player('59ed70bd1d41c84361b79427', 'Scooby')
Serb = Player('58cc6fc61d41c8259fa1fb5d', 'Serb')
Ses = Player('58c72fd21d41c8259fa1f8cc', 'Ses')
Shmeeli = Player('5d818416421aa954d874aecf', 'Shmeeli')
Shuffle = Player('58c727fa1d41c8259fa1f88d', 'Shuffle')
Silver = Player('58c7303b1d41c8259fa1f8dc', 'Silver')
Slox = Player('542ded228ab65f7d9c8294d1', 'Slox')
Spiff = Player('58c7321f1d41c8259fa1f8fe', 'Spiff')
StacysStepdad = Player('5a4ba1961d41c84881946783', 'Stacy\'s Stepdad')
Stus = Player('58c724e61d41c8259fa1f85c', 'Stus')
Swoosh = Player('5d6fe5d9421aa954d874adff', 'Swoosh$')
Takyon = Player('58c73fce1d41c8259fa1fa3c', 'Takyon')
TedGreene = Player('58b6552e1d41c867e937f7e7', 'Ted Greene')
Thumbs = Player('58d082921d41c8259fa1fe0a', 'Thumbs')
Tian = Player('545b23eb8ab65f7a95f74924', 'Tian')
TimTheGuy = Player('58d333ed1d41c8259fa2001f', 'TimTheGuy')
Trail = Player('5a93cebe1d41c80e2802a7fa', 'Trail')
TS420 = Player('59eed00e1d41c84361b795c8', 'TS420')
Twentytwok = Player('58d0968e1d41c8259fa1fe60', '22K')
Twisty = Player('58c729941d41c8259fa1f89b', 'Twisty')
Uma = Player('5a4ba42d1d41c8488194678f', 'Uma')
Warmmer = Player('58f8246c1d41c850b8b0fa54', 'Warmmer')
Woodcutting = Player('5b75ec7e421aa91fa088b1ef', '99 Woodcutting')
Yasu = Player('5a4ba0ba1d41c8488194677a', 'Yasu')
Younger = Player('54af8e44d2994e1346cd31da', 'Younger')

#store all players into a list
players = [Slox, Joyboy, Kalvar, Lint, Palika, Thumbs, BigJoig,
           Warmmer, DrLobster, Ok, Clutch, Ses, Peacecraft, Project, GWM420,
           Bonfire10, Glock, Golden, CNIU, Guillotine, Shuffle, TimTheGuy, 
           Kikoho, DrewNG, Arty, Deadstock, JNaut, Artelind, Meep, RyuCloud, 
           Guex, Trail, Silver, Dimension, Yasu, MrHeat, Younger, Klaps, 
           Dudutsai, Tian, PJ, Hysteric, Spiff, AdmiralZhao, Woodcutting, 
           Shmeeli, PSai, Glasper, Feo, Swoosh, Omar, Ferox, Hexjo, TedGreene, 
           Alt, BonkCushy, Scooby, Twisty, Een, Uma, Twentytwok, Nugget, Serb, 
           Poonpounder, Giraffe, Stus, IOA, BeastBoy, FutureShock, Kota, 
           Takyon, Bank, BigRedAnimeBike, Coach, Arcade, TS420, StacysStepdad, 
           Louis, Lochist]

#uncomment for reading to text file
#results = open("h2hs.txt","a") 

#initialize the results list
resultslist = []

#initialize the list of headings (containing opponent names)
headingslist = ['Players (W / L)']

for player in players:
    
    #add wins and losses vs. player to headings list
    headingslist.append(player.name + ' W')
    headingslist.append(player.name + ' L')
    
    #initialize list of player wins and losses
    playerlist = [player.name]
    
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
                            
            #if the players have played, print the head-to-head to the console
            #and record the win and loss counts in the playerlist
            if(played):
                print(player.name + " vs. " + opponent.name + "\r\n")
                print(str(wins) + " - " + str(losses))
                #uncomment to write to text file
                #results.write(player.name + " vs. " + opponent.name + "\r\n")
                #results.write(str(wins) + " - " + str(losses) + "\r\n")
                playerlist.append(str(wins))
                playerlist.append(str(losses))
            #if the players have not played, append empty strings to the player
            #list to match the desired csv output
            else:
                playerlist.append('')
                playerlist.append('')
        #similarly create empty strings if there is no match data for the given
        #matchup
        else:
            playerlist.append('')
            playerlist.append('')
    #add given player list to end of the results list to create one list of all
    #player data
    resultslist.append(playerlist)
    
#once all matchups have been recorded, insert the completed list of headings
#at the beginning of the resultslist
resultslist.insert(0, headingslist)

#initialize number of retries to access the csv file
numretries = 0

#initialize boolean to determine if we can write to csv file
csvWrite = False

#create loop to try to access file
while(not csvWrite):

    try:
        #open the csv output file and avoid creating extra spacing lines
        csvFile = open("h2hresults.csv", "w", newline='')
        
        #specify that we can now write
        csvWrite = True
        
    #if a keyboardinterupt occurs abort execution
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        #if we have exceeded the maximum number of retries raise an
        #exception
        if(numretries > maxretries):
            raise Exception("Exceeded maximum number of retries to access the file")
        #otherwise sleep for five seconds and then retry the request
        print("Permission to access csv file denied, please close any programs with the file open")
        print("Waiting to retry write request to file")
        time.sleep(5)
        print("Retrying write request")
                    
        #increment number of retries then retry connection
        numretries += 1
        
        continue
    
#truncate the csv file to remove old results
csvFile.truncate()

#write each element in the results list to the csv file
with csvFile:
    csv
    writer = csv.writer(csvFile)
    writer.writerows(resultslist)
csvFile.close()

#indicate the program has completed (typically takes a while, time will
#increase quadratically with more opponents)
print("done")