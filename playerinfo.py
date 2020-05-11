import settings

def getPlayersByState(players):
    playersByState = {'MA': [], 'NH': [], 'CT': [], 'RI': [], 'VT': [], 
                       'ME': []}
    for player in players:
        playersByState[player.state].append(player)
    print(playersByState)
    print()
    
def getPlayersByMain(players):
    playersByMain = {}
    for player in players:
        for main in player.mains:
            if(main in playersByMain):
                playersByMain[main].append(player)
            else:
                playersByMain[main] = [player]
    print(playersByMain)
    print()
    
def getPlayersByPR(players):
    playersByPR = {}
    for player in players:
        if(not player.curPRs == None):
            for key in player.curPRs:
                if(key in playersByPR):
                    if(player.curPRs[key] == 'HM'):
                        playersByPR[key][15] = player
                    else:
                        playersByPR[key][player.curPRs[key]] = player
                else:
                    playersByPR[key] = [None for i in range(16)]
                    if(player.curPRs[key] == 'HM'):
                        playersByPR[key][15] = player
                    else:
                        playersByPR[key][player.curPRs[key]] = player
    for key in playersByPR:
        i = 0
        while(i < len(playersByPR[key])):
            if(playersByPR[key][i] == None):
                playersByPR[key].pop(i)
            else:
                i += 1
    print(playersByPR)
    print()
            
def searchPlayers(players, mains, state=None):
    foundPlayers = []
    states = ['MA', 'VT', 'CT', 'RI', 'NH', 'ME']
    
    if(type(mains) != list):
        if(mains.upper() in states):
            s = mains
            mains = state
            state = s
    else:
        mains = sorted(mains)
        mains = map(str.lower(), mains)
    for player in players:
        mainsref = [main.lower() for main in sorted(player.mains)]
        if(mains != None):
            if(state != None):
                if(type(mains) == list):
                    if(mains == mainsref and state.lower() == player.state.lower()):
                        foundPlayers.append(player)
                else:
                    main = mains
                    if(main.lower() in mainsref and state.lower() == player.state.lower()):
                        foundPlayers.append(player)
            else:
                if(type(mains) == list):
                    if(mainsref == mains):
                        foundPlayers.append(player)
                else:
                    main = mains
                    if(main.lower() in mainsref):
                        foundPlayers.append(player)
        else:
            if(state != None):
                if(player.state.lower() == state.lower()):
                    foundPlayers.append(player)
    if(len(foundPlayers) == 0):
        print("No players found")
        print()
    else:
        print(foundPlayers)
        print()
    
players = settings.players

cont = True

userfunc = ''

while(cont):
    print('Select which means to display players by')
    print('State, Main, PR, Search, or Exit?')
    userfunc = input()
    print()

    try:
        userfunc = str(userfunc)
    
    except ValueError:
        print("Invalid input. Please respond with \'state\', \'main\', \'pr\', \'search\', or \'exit\'")
        print()

    else:
        task = userfunc.lower()
        if(task == 'state'):
            getPlayersByState(players)
        elif(task == 'main'):
            getPlayersByMain(players)
        elif(task == 'pr'):
            getPlayersByPR(players)
        elif(task == 'search'):
            cont2 = True
            while(cont2):
                print('Search for players based on main and state, separated by comas, or return')
                searchkeys = input()
                print()
                
                try:
                    searchkeys = str(searchkeys)
                    
                except ValueError:
                    print("Invalid input. Please respond with either a state, a main, \'return\' or in the form \'main\', \'state\'")
                    print()
                
                else:
                    
                    if(searchkeys == 'return'):
                        cont2 = False
                        break
                    else:
                        searchparams = searchkeys.split(',')
                        if(len(searchparams) == 2):
                            searchPlayers(players, searchparams[0].strip(), searchparams[1].strip())
                        elif(len(searchparams) == 1):
                           searchPlayers(players, searchparams[0].strip())
                        else:
                            print("Invalid input. Please respond with either a state, a main, \'return\' or in the form \'main\', \'state\'")
                            print()
                            
        elif(task == 'exit'):
            cont = False
            break
        else:
            print("Invalid input. Please respond with \'state\', \'main\', \'pr\', \'search\', or \'exit\'")
            print()