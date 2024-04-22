from os import environ 

class Config:
    API_ID = environ.get("API_ID", "15344356")
    API_HASH = environ.get("API_HASH", "69d343189cf755ebe76a6b07f5578402")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6493917299:AAH0XFz4bvGO4c8Glce3F76BD9oLrIl_M_o") 
    BOT_SESSION = environ.get("BOT_SESSION", "BQDqIuQArGVLTfA_BRLhZeDePogp92ilbEuAxrf1aOrf22s3YS7qBh0i_4ORCleJpm9DK9qLiT60od6JevUWN0Vr8Nx7Hek_lK533BU-Yn4n-QRU1PJECOZRyjLk5TMsO-h7lExsgvnTg7pkhaPucyWbSOsDfH4BWb_zMBaTiO-C1638X3Jij051BIArfTCfQsWztaOyVDDX1HDmnG_kXfRrtjAIw1S7Mn-89Brd9oB7wLjBsTmyOP_ufgdLGmbqygrPrz6zrFqtvhZlQoEQo7908ahAJraLHL23uqgDpFMW_NrNKH2jD6D8R6uSFLsiGIs40_XuwvXSr3UaO-hJtCxLkyZ2hAAAAAGDEVBzAQ") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://mendaxtelegram:<y@Va$G_y22rihWt>@atlascluster.0zrjy0r.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5186250641').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
