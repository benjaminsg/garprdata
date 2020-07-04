from datetime import datetime

# specify maximum number of retries that can occur during request to the server    
maxRetries = 20

# specify start and end times of season to collect data from (can be any time frame)
seasonStart = datetime(2019, 9, 23)
seasonEnd = datetime(2020, 3, 15)

# specify start and end times of previous season
prevSeasonStart = datetime(2019, 3, 24)
prevSeasonEnd = datetime(2019, 9, 22)


# Player class
class Player:
    def __init__(self, id, name, state, mains=None, cur_prs=None):
        # id taken from GARPR player page
        self.id = id
        # name is name that will display in all output formats
        self.name = name
        # state is the state the player is from
        self.state = state
        # mains are the characters the player mains
        if type(mains) == list:
            self.mains = mains
        else:
            self.mains = [mains]
        # cur_prs are the PR rankings the player currently has
        self.cur_prs = cur_prs

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


# create all players
AdmiralZhao = Player('58cd956a1d41c8259fa1fd0b', 'Admiral Zhao', 'MA', 'Samus')
Alt = Player('5c65f982421aa93db94e98a5', 'Alt', 'MA', 'Fox')
Arcade = Player('58cc88171d41c8259fa1fc21', 'Arcade', 'MA', 'Captain Falcon', {'UMA': 3})
Artelind = Player('58d20b761d41c8259fa1ff7b', 'Artelind', 'RI', 'Samus', {'RI': 3})
Arty = Player('53c64c738ab65f6e27751221', 'Arty', 'CT', 'Peach', {'CT': 8})
Bank = Player('59ed7c721d41c84361b79498', 'Bank', 'MA', 'Marth')
Beansoup = Player('5e444f96421aa93e12ba4f9e', 'beansoup', 'MA', 'Falco')
BeastBoy = Player('5d6a8bb3421aa954d874ad46', 'BeastBoy', 'MA', 'Falco')
Ben = Player('5dbb8aca421aa97778f4f808', 'Ben', 'NH', 'Sheik')
BigJoig = Player('545c83e88ab65f126349d8bb', 'BigJoig', 'MA', 'Falco')
BigRedAnimeBike = Player('58752d371d41c82e80d558a3', 'BigRedAnimeBike', 'MA', ['Fox', 'Sheik'])
Bonfire10 = Player('58c7303b1d41c8259fa1f8dd', 'bonfire10', 'NH', 'Sheik', {'NH': 5, 'NE': 'HM'})
BonkCushy = Player('542cf48e8ab65f5dcb8ce4ab', 'BonkCushy', 'MA', 'Pikachu')
Clutch = Player('5d698f0b421aa954d874acfb', 'Clutch', 'MA', 'Marth', {'MA': 4})
CNIU = Player('58cc8c0f1d41c8259fa1fc49', 'CNIU', 'NH', 'Fox')
Coach = Player('5c6ef669421aa93db94e9954', 'Coach', 'MA', 'Fox')
Dimension = Player('5b16ba781d41c86e982900e4', 'Dimension', 'MA', 'Marth', {'MA': 2, 'NE': 13, 'BC': 1})
DrewNG = Player('596272821d41c840fdcf8804', 'DrewNG', 'CT', 'Fox', {'CT': 9})
DrLobster = Player('5d4e3f57421aa954d874ac18', 'DrLobster', 'NH', 'Sheik', {'NH': 2, 'NE': 4})
Dudutsai = Player('58c732681d41c8259fa1f905', 'dudutsai', 'MA', 'Jigglypuff')
Een = Player('59ed70bd1d41c84361b79428', 'Een', 'MA', 'Peach')
Elen = Player('5e444f96421aa93e12ba4f9d', 'Elen', 'MA', 'Fox')
Feo = Player('5d818416421aa954d874aed1', 'Feo', 'MA', 'Falco')
Ferox = Player('58cc6fc61d41c8259fa1fb6b', 'Ferox', 'MA', 'Fox', {'NEU': 5})
FutureShock = Player('5ade76ef1d41c852c7240f91', 'Future Shock', 'MA', 'Captain Falcon')
Giraffe = Player('5d423a5a421aa954d874ab76', 'Giraffe', 'MA', 'Captain Falcon')
Glasper = Player('58d09a571d41c8259fa1fe86', 'Glasper', 'MA', ['Fox', 'Captain Falcon'])
Glock = Player('5a4ba1961d41c84881946784', 'glock in my toyota', 'NH', 'Mr. Game & Watch', {'NH': 3, 'NE': 10})
Golden = Player('58c7303b1d41c8259fa1f8d2', 'Golden', 'NH', 'Captain Falcon', {'NH': 4, 'NE': 14})
Guex = Player('58c73fce1d41c8259fa1fa3d', 'Guex', 'MA', 'Yoshi')
Guillotine = Player('5d295939421aa90f9fc1bd97', 'Guillotine', 'NH', 'Sheik', {'NH': 7})
GWM420 = Player('5a4ba23b1d41c84881946788', 'GWM420', 'NH', 'Fox', {'NH': 6})
Hexjo = Player('5d6fe5d9421aa954d874adfb', 'Hexjo', 'MA', 'Fox')
Hysteric = Player('5b633156421aa91fa088af7a', 'Hysteric', 'MA', 'Jigglypuff', {'MA': 10})
IOA = Player('58c72fd21d41c8259fa1f8c9', 'IOA', 'MA', ['Fox', 'Marth'])
JNaut = Player('58c7317e1d41c8259fa1f8e3', 'JNaut', 'RI', 'Sheik', {'RI': 2, 'NE': 11})
Joyboy = Player('58c73c7e1d41c8259fa1f9c5', 'Joyboy', 'RI', 'Fox', {'RI': 1, 'NE': 3})
Kalvar = Player('58c726dd1d41c8259fa1f870', 'Kalvar', 'NH', 'Marth', {'NH': 1, 'NE': 2})
Kikoho = Player('5b40def21d41c8456a883413', 'Kikoho', 'CT', 'Marth', {'CT': 6, 'NE': 12})
Klaps = Player('58cc6fc61d41c8259fa1fb57', 'Klaps', 'MA', 'Captain Falcon', {'MA': 6})
Kota = Player('58cc6fc61d41c8259fa1fb6a', 'Kota', 'MA', 'Falco')
Lint = Player('545c8e5f8ab65f12c01061ca', 'lint', 'CT', 'Falco', {'CT': 2, 'NE': 5})
Lochist = Player('5c86c4d1421aa93db94e9ab6', 'Lochist', 'VT', ['Falco', 'Young Link'], {'VT': 2})
Louis = Player('5ba19af6421aa91fa088b641', 'Louis', 'VT', 'Falco', {'VT': 1, 'NE': 15})
Meep = Player('58c73d181d41c8259fa1f9d0', 'Meep', 'RI', 'Sheik', {'RI': 4})
MrHeat = Player('59ed78aa1d41c84361b7947c', 'Mr. Heat', 'MA', ['Falco', 'Sheik'], {'MA': 5})
Nugget = Player('58c729f41d41c8259fa1f8a2', 'Nugget', 'MA', 'Fox')
Omar = Player('5d16d616421aa90f9fc1bc56', 'Omar', 'MA', 'Falco')
Palika = Player('58cc88171d41c8259fa1fc20', 'Palika', 'CT', 'Dr. Mario', {'CT': 4, 'NE': 7})
Peacecraft = Player('587c636d1d41c82e80d55aaf', 'M. Peacecraft', 'CT', ['Marth', 'Fox', 'Sheik'])
PJ = Player('542cf4d08ab65f5e0c6e0751', 'PJ', 'MA', 'Falco', {'MA': 9})
Poonpounder = Player('5e2fcf55421aa93e12ba4946', 'Poonpounder', 'MA', 'Fox', {'BU': 2})
Project = Player('58cc748e1d41c8259fa1fbb8', 'Project', 'MA', 'Fox', {'MA': 1, 'NE': 9})
PSai = Player('5d82976f421aa954d874af04', 'PSai', 'MA', 'Sheik', {'BU': 1})
Ricky = Player('58cc88171d41c8259fa1fc23', 'Ricky', 'CT', 'Fox')
RyuCloud = Player('58c739fa1d41c8259fa1f97f', 'RyuCloud', 'RI', ['Marth', 'Fox'], {'RI': 5})
Scooby = Player('59ed70bd1d41c84361b79427', 'Scooby', 'MA', 'Sheik')
Serb = Player('58cc6fc61d41c8259fa1fb5d', 'Serb', 'MA', 'Ice Climbers')
Ses = Player('58c72fd21d41c8259fa1f8cc', 'Ses', 'MA', 'Fox')
Shmeeli = Player('58811d861d41c82e80d55b56', 'Shmeeli', 'MA', 'Falco', {'NEU': 2})
Silver = Player('58c7303b1d41c8259fa1f8dc', 'Silver', 'MA', ['Falco', 'Fox'], {'UMA': 1})
Slox = Player('542ded228ab65f7d9c8294d1', 'Slox', 'CT', 'Fox', {'CT': 1, 'NE': 1})
Spiff = Player('58c7321f1d41c8259fa1f8fe', 'Spiff', 'MA', 'Sheik')
StacysStepdad = Player('5a4ba1961d41c84881946783', 'Stacy\'s Stepdad', 'ME', 'Peach')
Stus = Player('58c724e61d41c8259fa1f85c', 'Stus', 'MA', 'Falco')
Swoosh = Player('5d6fe5d9421aa954d874adff', 'Swoosh$', 'MA', 'Fox')
Takyon = Player('58c73fce1d41c8259fa1fa3c', 'Takyon', 'MA', 'Falco')
TedGreene = Player('58b6552e1d41c867e937f7e7', 'Ted Greene', 'MA', 'Fox')
Thumbs = Player('58d082921d41c8259fa1fe0a', 'Thumbs', 'CT', 'Falco', {'CT': 3, 'NE': 6})
Tian = Player('545b23eb8ab65f7a95f74924', 'Tian', 'MA', 'Sheik', {'MA': 8})
TimTheGuy = Player('58d333ed1d41c8259fa2001f', 'TimTheGuy', 'CT', 'Marth', {'CT': 7})
Trail = Player('5a93cebe1d41c80e2802a7fa', 'Trail', 'MA', ['Ice Climbers', 'Ganondorf'], {'MA': 7})
TS420 = Player('59eed00e1d41c84361b795c8', 'TS420', 'ME', 'Marth')
Twentytwok = Player('58d0968e1d41c8259fa1fe60', '22K', 'MA', 'Sheik')
Twisty = Player('58c729941d41c8259fa1f89b', 'Twisty', 'MA', 'Jigglypuff')
Uma = Player('5a4ba42d1d41c8488194678f', 'Uma', 'MA', 'Fox')
Warmmer = Player('58f8246c1d41c850b8b0fa54', 'Warmmer', 'CT', 'Falco', {'CT': 5, 'NE': 8})
Woodcutting = Player('5b75ec7e421aa91fa088b1ef', '99 Woodcutting', 'MA', 'Sheik', {'NEU': 1})
Yasu = Player('5a4ba0ba1d41c8488194677a', 'Yasu', 'MA', 'Marth', {'MA': 3})
Younger = Player('54af8e44d2994e1346cd31da', 'Younger', 'MA', 'Falco', {'MA': 'HM'})

# store all players into a list
players = [Slox, Joyboy, Kalvar, Lint, Palika, Thumbs, BigJoig, Warmmer, DrLobster, Clutch, Ses, Peacecraft, Project,
           GWM420, Bonfire10, Glock, Golden, CNIU, Guillotine, Ben, TimTheGuy, Kikoho, DrewNG, Arty, Ricky, JNaut,
           Artelind, Meep, RyuCloud, Guex, Trail, Silver, Dimension, Yasu, MrHeat, Younger, Klaps, Dudutsai, Tian, PJ,
           Hysteric, Spiff, AdmiralZhao, Woodcutting, Shmeeli, PSai, Glasper, Feo, Swoosh, Omar, Ferox, Hexjo,
           TedGreene, Alt, BonkCushy, Scooby, Twisty, Elen, Beansoup, Een, Uma, Twentytwok, Nugget, Serb, Poonpounder,
           Giraffe, Stus, IOA, BeastBoy, FutureShock, Kota, Takyon, Bank, BigRedAnimeBike, Coach, Arcade, TS420,
           StacysStepdad, Louis, Lochist]
