class Database(): #class to interact with database files
    def __init__(self):
        self.PlayerDatabase = 'playerinfo.csv' #playerinfo is the database for player stats
        self.BestiaryDatabase = 'bestiary.csv' #bestiary is the database for monster information
        self.SkillDatabase = 'skill.csv' #skill is the database for skill information
        self.ItemDatabase = 'item.csv' #item is the database for item information
        self.BattleItemDatabase = 'battleitem.csv' #battleitem is the database for battleitem information
