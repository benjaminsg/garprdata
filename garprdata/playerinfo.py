import config


def get_players_by_state(players):
    players_by_state = {'MA': [], 'NH': [], 'CT': [], 'RI': [], 'VT': [],
                        'ME': []}
    for player in players:
        players_by_state[player.state].append(player)
    print(players_by_state)
    print()


def get_players_by_main(players):
    players_by_main = {}
    for player in players:
        for main in player.mains:
            if main in players_by_main:
                players_by_main[main].append(player)
            else:
                players_by_main[main] = [player]
    print(players_by_main)
    print()


def get_players_by_pr(players):
    players_by_pr = {}
    for player in players:
        if player.cur_prs is not None:
            for key in player.cur_prs:
                if key in players_by_pr:
                    if player.cur_prs[key] == 'HM':
                        players_by_pr[key][15] = player
                    else:
                        players_by_pr[key][player.cur_prs[key]] = player
                else:
                    players_by_pr[key] = [None for i in range(16)]
                    if player.cur_prs[key] == 'HM':
                        players_by_pr[key][15] = player
                    else:
                        players_by_pr[key][player.cur_prs[key]] = player
    for key in players_by_pr:
        i = 0
        while i < len(players_by_pr[key]):
            if players_by_pr[key][i] is None:
                players_by_pr[key].pop(i)
            else:
                i += 1
    print(players_by_pr)
    print()


def search_players(players, mains, state=None):
    found_players = []
    states = ['MA', 'VT', 'CT', 'RI', 'NH', 'ME']

    if type(mains) != list:
        if mains.upper() in states:
            s = mains
            mains = state
            state = s
    else:
        mains = sorted(mains)
        mains = map(str.lower(), mains)
    for player in players:
        mains_ref = [main.lower() for main in sorted(player.mains)]
        if mains is not None:
            if state is not None:
                if type(mains) == list:
                    if mains == mains_ref and state.lower() == player.state.lower():
                        found_players.append(player)
                else:
                    main = mains
                    if main.lower() in mains_ref and state.lower() == player.state.lower():
                        found_players.append(player)
            else:
                if type(mains) == list:
                    if mains_ref == mains:
                        found_players.append(player)
                else:
                    main = mains
                    if main.lower() in mains_ref:
                        found_players.append(player)
        else:
            if state is not None:
                if player.state.lower() == state.lower():
                    found_players.append(player)
    if len(found_players) == 0:
        print("No players found")
        print()
    else:
        print(found_players)
        print()


players = config.players

cont = True

user_func = ''

while cont:
    print('Select which means to display players by')
    print('State, Main, PR, Search, or Exit?')
    user_func = input()
    print()

    try:
        user_func = str(user_func)

    except ValueError:
        print("Invalid input. Please respond with \'state\', \'main\', \'pr\', \'search\', or \'exit\'")
        print()

    else:
        task = user_func.lower()
        if task == 'state':
            get_players_by_state(players)
        elif task == 'main':
            get_players_by_main(players)
        elif task == 'pr':
            get_players_by_pr(players)
        elif task == 'search':
            cont2 = True
            while cont2:
                print('Search for players based on main and state, separated by comas, or return')
                search_key = input()
                print()

                try:
                    search_key = str(search_key)

                except ValueError:
                    print(
                        "Invalid input. Please respond with either a state, a main, \'return\' or in the form "
                        "\'main\', \'state\'")
                    print()

                else:

                    if search_key == 'return':
                        cont2 = False
                        break
                    else:
                        search_params = search_key.split(',')
                        if len(search_params) == 2:
                            search_players(players, search_params[0].strip(), search_params[1].strip())
                        elif len(search_params) == 1:
                            search_players(players, search_params[0].strip())
                        else:
                            print(
                                "Invalid input. Please respond with either a state, a main, \'return\' or in the form "
                                "\'main\', \'state\'")
                            print()

        elif task == 'exit':
            cont = False
            break
        else:
            print("Invalid input. Please respond with \'state\', \'main\', \'pr\', \'search\', or \'exit\'")
            print()
