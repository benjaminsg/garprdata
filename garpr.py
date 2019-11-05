import json
import requests
from datetime import datetime

class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
seasonstart = datetime(2019, 9, 24)
seasonend = datetime(2020, 3, 22)

Slox = Player('542ded228ab65f7d9c8294d1', 'Slox')
Joyboy = Player('58c73c7e1d41c8259fa1f9c5', 'Joyboy')
Kalvar = Player('58c726dd1d41c8259fa1f870', 'Kalvar')
lint = Player('545c8e5f8ab65f12c01061ca', 'lint')
Tiramisu = Player('58d08cd91d41c8259fa1fe3b', 'Tiramisu')
Palika = Player('58cc88171d41c8259fa1fc20', 'Palika')
Thumbs = Player('58d082921d41c8259fa1fe0a', 'Thumbs')
BigJoig = Player('545c83e88ab65f126349d8bb', 'BigJoig')
Warmmer = Player('545c83e88ab65f126349d8bb', 'Warmmer')
DrLobster = Player('5d4e3f57421aa954d874ac18', 'DrLobster')
Ok = Player('5d295678421aa90f9fc1bd83', 'WAS | Ok')
Clutch = Player('5d698f0b421aa954d874acfb', 'Clutch')
Ses = Player('58c72fd21d41c8259fa1f8cc', 'Ses')
Peacecraft = Player('587c636d1d41c82e80d55aaf', 'M. Peacecraft')
Project = Player('58cc748e1d41c8259fa1fbb8', 'Project')
Slox = Player('542ded228ab65f7d9c8294d1', 'Slox')
Joyboy = Player('58c73c7e1d41c8259fa1f9c5', 'Joyboy')
Kalvar = Player('58c726dd1d41c8259fa1f870', 'Kalvar')
lint = Player('545c8e5f8ab65f12c01061ca', 'lint')
Tiramisu = Player('58d08cd91d41c8259fa1fe3b', 'Tiramisu')
Palika = Player('58cc88171d41c8259fa1fc20', 'Palika')
Thumbs = Player('58d082921d41c8259fa1fe0a', 'Thumbs')
BigJoig = Player('545c83e88ab65f126349d8bb', 'BigJoig')
Warmmer = Player('58f8246c1d41c850b8b0fa54', 'Warmmer')
DrLobster = Player('5d4e3f57421aa954d874ac18', 'DrLobster')
Ok = Player('5d295678421aa90f9fc1bd83', 'WAS | Ok')
Clutch = Player('5d698f0b421aa954d874acfb', 'Clutch')
Ses = Player('58c72fd21d41c8259fa1f8cc', 'Ses')
Peacecraft = Player('587c636d1d41c82e80d55aaf', 'M. Peacecraft')
Project = Player('58cc748e1d41c8259fa1fbb8', 'Project')
GWM420 = Player('5a4ba23b1d41c84881946788', 'GWM420')
Rasen = Player('59ed94891d41c84361b79506', 'Rasen')
bonfire10 = Player('58c7303b1d41c8259fa1f8dd', 'bonfire10')
glock = Player('5a4ba1961d41c84881946784', 'glock in my toyota')
Golden = Player('58c7303b1d41c8259fa1f8d2', 'Golden')
CNIU = Player('58cc8c0f1d41c8259fa1fc49', 'CNIU')
Guillotine = Player('5d295939421aa90f9fc1bd97', 'Guillotine')
Shuffle = Player('58c727fa1d41c8259fa1f88d', 'Shuffle')
TimTheGuy = Player('58d333ed1d41c8259fa2001f', 'TimTheGuy')
Kikoho = Player('5b40def21d41c8456a883413', 'Kikoho')
DrewNG = Player('596272821d41c840fdcf8804', 'DrewNG')
Arty = Player('53c64c738ab65f6e27751221', 'Arty')
JNaut = Player('58c7317e1d41c8259fa1f8e3', 'JNaut')
Artelind = Player('58d20b761d41c8259fa1ff7b', 'Artelind')
Meep = Player('58c73d181d41c8259fa1f9d0', 'Meep')
Guex = Player('58c73fce1d41c8259fa1fa3d', 'Guex')
Silver = Player('58c7303b1d41c8259fa1f8dc', 'Silver')
Dimension = Player('5b16ba781d41c86e982900e4', 'Dimension')
Yasu = Player('5a4ba0ba1d41c8488194677a', 'Yasu')
MrHeat = Player('59ed78aa1d41c84361b7947c', 'Mr. Heat')
Shmeeli = Player('5d818416421aa954d874aecf', 'Shmeeli')
Swoosh = Player('5d6fe5d9421aa954d874adff', 'Swoosh$')
Unlucky = Player('58d1fa411d41c8259fa1febb', 'Unlucky')
Woodcutting = Player('5b75ec7e421aa91fa088b1ef', '99 Woodcutting')
Bank = Player('59ed7c721d41c84361b79498', 'Bank')
Spiff = Player('58c7321f1d41c8259fa1f8fe', 'Spiff')
Scooby = Player('59ed70bd1d41c84361b79427', 'Scooby')
PJ = Player('542cf4d08ab65f5e0c6e0751', 'PJ')
SDHB = Player('5d818416421aa954d874aed1', 'SDHB')
BonkCushy = Player('542cf48e8ab65f5dcb8ce4ab', 'BonkCushy')
Hysteric = Player('5b633156421aa91fa088af7a', 'Hysteric')
Ferox = Player('58cc6fc61d41c8259fa1fb6b', 'Ferox')
PSai = Player('5d82976f421aa954d874af04', 'PSai')
AdmiralZhao = Player('58cd956a1d41c8259fa1fd0b', 'Admiral Zhao')
Glasper = Player('58d09a571d41c8259fa1fe86', 'Glasper')
F4X = Player('5d8187ec421aa954d874aede', 'F4X')
StacysStepdad = Player('5a4ba1961d41c84881946783', 'Stacy\'s Stepdad')
Louis = Player('5ba19af6421aa91fa088b641', 'Louis')

players = [Slox, Joyboy, Kalvar, lint, Tiramisu, Palika, Thumbs, BigJoig,
           Warmmer, DrLobster, Ok, Clutch, Ses, Peacecraft, Project, GWM420,
           Rasen, bonfire10,glock, Golden, CNIU, Guillotine, Shuffle, 
           TimTheGuy, Kikoho, DrewNG, Arty, JNaut, Artelind, Meep, Guex, 
           Silver, Dimension, Yasu, MrHeat, Shmeeli, Swoosh, Unlucky, 
           Woodcutting, Bank, Spiff, Scooby, PJ, SDHB, BonkCushy, Hysteric, 
           Ferox, PSai, AdmiralZhao, Glasper, F4X, StacysStepdad, Louis]

results = open("h2hs.txt","a") 

for player in players:
    
    for opponent in players:
        
        if(player != opponent):
            
            #print(player.name + " vs. " + opponent.name)
            
            url = "https://notgarpr.com:3001/newengland/matches/" + player.id + "?opponent=" + opponent.id + "&fbclid=IwAR3V8QosRC1_d-tBrPtSLB7pHKWuwXlea6fuKVjU645bq6dKNEshOvL7tv8"

            response = requests.get(url)
            data = json.loads(response.text)

            wins = 0
            losses = 0

            played = False
            
            if('matches' in data):
                for match in data['matches']:
                    date = datetime.strptime(match['tournament_date'], '%m/%d/%y')
                    if(seasonstart < date < seasonend):
                        if(match['result'] == 'win'):
                            wins += 1
                            played = True
                        else:
                            losses += 1
                            played = True
                            
            if(played):
                print(player.name + " vs. " + opponent.name + "\r\n")
                print(str(wins) + " - " + str(losses))
                results.write(player.name + " vs. " + opponent.name + "\r\n")
                results.write(str(wins) + " - " + str(losses) + "\r\n")