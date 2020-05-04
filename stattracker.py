class team:
    name = str
    players: list
    playrate_data: dict

    def __init__(self, name):
        self.name = name
        self.players = []
        self.playrate_data = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}

class player:
    map_data: dict
    name: str
    team: team
    playtime: dict
    total_playtime: int
    sorting_stat: int

    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.map_data = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}
        self.playtime = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}
        self.total_playtime = 0
        self.sorting_stat = 0

class map_round:
    map_name: str
    map_time: int
    player_dict: dict
    hero_playtime_1: list
    hero_playtime_2: list

    def __init__(self, map_name):
        self.map_name = map_name
        self.player_dict = {}
        self.hero_playtime_1 = []
        self.hero_playtime_2 = []


class match:
    teams: tuple
    score: tuple
    maps: list
    week: int
    
    def __init__(self, teams, score, week):
        self.teams = teams
        self.score = score
        self.maps = []
        self.week = week
        
class Hero:
    time: int
    name: str
    emote: str

    def __init__(self, name, emote):
        self.name = name
        self.time = 0
        self.emote = emote



#PN0, PN1, PN2, PN3, PN4, PN5, PN6, PN7, PN8, PN9, PN10, PN11, Unknown, Global, HUD, HUD Time, Map, Match Time (Seconds), Start Up, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, Team 1 Playtime, Team 2 Playtime
#0  , 1  , 2  , 3  , 4  , 5  , 6  , 7  , 8  , 9  , 10  , 11  , 12     , 13    , 14 , 15      , 16 , 17                  , 18      , 19, 20, 21, 22, 23, 24, 25, 26, 27, 28 , 29 , 30             , 31
#1428.128, Global, Falso, 0.05, La Habana, 1092, Verdadero, {54; 5; 16; 6201.54; 10331.24; 6276.69; 2819.84; 4}, {32; 8; 16; 4792.86; 8974.64; 5321.19; 1951.42; 6}, {80; 15; 16; 12809.45; 0; 12742.20; 4789.30; 5}, {62; 34; 8; 14346.65; 2528.07; 14980.90; 8853.40; 7}, {86; 41; 16; 12892.86; 0; 8031.22; 1880.78; 6}, {68; 22; 18; 14819.60; 2485.36; 8935.03; 4630.26; 7}, {38; 7; 23; 5677.94; 10066.64; 7215.66; 3439.31; 4}, {47; 14; 21; 8695.46; 5307.79; 6679.01; 2402.76; 4}, {60; 22; 21; 15117.47; 0; 15793.74; 6543.80; 7}, {57; 26; 20; 17242.04; 5114.05; 25734.34; 14658.11; 8}, {27; 8; 20; 4240.57; 307.20; 5069.53; 1592.95; 2; 27}, {35; 13; 20; 5275.31; 8385.21; 5332.26; 1720.93; 6}, {0; 0; 0; 0; 1092; 0; 0; 0; 0; 0; 0; 0; 0; 1092; 0; 0; 1092; 1092; 1092; 0; 0; 0; 0; 1092}, {0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 1092; 0; 1092; 0; 0; 1092; 0; 1092; 0; 0; 1092; 0; 1092}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
#{Team 1: [Players], Team 2: [Players]}