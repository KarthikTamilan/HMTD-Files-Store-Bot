import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5487241899:AAF1MW4eqQeqbQR1rkowsxevJAFrkNBOPvI)

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "11973721"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001518309911"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1391556668"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgres://skffzecjlcrksg:930b5156b2dcba59f46fe84a9f542e8c621e6c719eff94a03966b1d869e68303@ec2-3-216-181-219.compute-1.amazonaws.com:5432/d4np452b96lpuq")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001436081117"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello 👋 {first}💗</b>\n\n<b>I'm an HMTD Official Files Store Bot Maintained by @HMTD_Links. Send me any File I will Give you a Permanent Sharable Link. I Can Store Files Upto 4GB File. Keep me Join to Our Official Channel to Receive Bot & Movies Updates in @HMTD_Links. Users Can Access Multiple Files or Posts by Creating Batch Links. Check '😊 About me' Button.</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5162208212").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Hello 👋 {first}💗</b>\n\n<b>You Need to Join Our Channel to Use me\n\nKindly Please Join Our Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>Bot Uptime Status</b>\n<b>{uptime}</b>"
USER_REPLY_TEXT = "<b>❌ Invalid Comment..! This Comment Only Access Owner or Admins So you Can Get File Links From : hmtd-movies.blogspot.com or @HMTD_Links</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(1391556668)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
