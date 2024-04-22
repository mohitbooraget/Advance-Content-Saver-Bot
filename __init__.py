#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = config("15344356", default=None, cast=int)
API_HASH = config("69d343189cf755ebe76a6b07f5578402", default=None)
BOT_TOKEN = config("6493917299:AAH0XFz4bvGO4c8Glce3F76BD9oLrIl_M_o", default=None)
SESSION = config("BQDqIuQArGVLTfA_BRLhZeDePogp92ilbEuAxrf1aOrf22s3YS7qBh0i_4ORCleJpm9DK9qLiT60od6JevUWN0Vr8Nx7Hek_lK533BU-Yn4n-QRU1PJECOZRyjLk5TMsO-h7lExsgvnTg7pkhaPucyWbSOsDfH4BWb_zMBaTiO-C1638X3Jij051BIArfTCfQsWztaOyVDDX1HDmnG_kXfRrtjAIw1S7Mn-89Brd9oB7wLjBsTmyOP_ufgdLGmbqygrPrz6zrFqtvhZlQoEQo7908ahAJraLHL23uqgDpFMW_NrNKH2jD6D8R6uSFLsiGIs40_XuwvXSr3UaO-hJtCxLkyZ2hAAAAAGDEVBzAQ", default=None)
FORCESUB = config("imendaxpublic", default=None)
AUTH = config("6594402123", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
