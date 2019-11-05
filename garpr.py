import json
import requests
from datetime import datetime

class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
seasonstart = datetime(2019, 3, 24)
seasonend = datetime(2019, 9, 22)

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

players = [Slox, Joyboy, Kalvar, lint, Tiramisu, Palika, Thumbs, BigJoig,
           Warmmer, DrLobster, Ok, Clutch, Ses, Peacecraft, Project]

for player in players:
    
    for opponent in players:
        
        if(player != opponent):
            
            print(player.name + " vs. " + opponent.name)
            
            url = "https://notgarpr.com:3001/newengland/matches/" + player.id + "?opponent=" + opponent.id + "&fbclid=IwAR3V8QosRC1_d-tBrPtSLB7pHKWuwXlea6fuKVjU645bq6dKNEshOvL7tv8"

            response = requests.get(url)
            data = json.loads(response.text)

            wins = 0
            losses = 0

            skip = False

            if(player == Palika and opponent == Clutch):
                skip = True
            elif(player == Thumbs and opponent == DrLobster):
                skip = True
            if(not skip):
                for match in data['matches']:
                    date = datetime.strptime(match['tournament_date'], '%m/%d/%y')
                    if(seasonstart < date < seasonend):
                        if(match['result'] == 'win'):
                            wins +=1
                        else:
                            losses += 1
            print(str(wins) + " - " + str(losses))