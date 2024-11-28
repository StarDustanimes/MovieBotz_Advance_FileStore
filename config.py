#(©) WeekendsBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7853494677:AAEN5a7q9dqFtHdbaVpkFKJXf5iTO5BSk20")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23579843"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "813614877521e3b94bed3d1562192fdd")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002201109564"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5548954124"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://jeffreymosesdj:Jeffrey@cluster2.cuiux.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster2")


JOIN_REQUEST_ENABLE = os.environ.get("JOIN_REQUEST_ENABLED", None)
#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1002076989748"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1002145840070"))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "-1002159732062"))
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "-1002493732967"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_PIC = os.environ.get("START_PIC","")
START_MSG = os.environ.get("START_MESSAGE", "ᴋᴏɴɪᴄʜɪᴡᴀ {mention}\n\n<blockquote>ᴋᴏɴɪᴄʜɪᴡᴀ ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴀɴɪᴍᴇ/ᴍᴏᴠɪᴇ ғɪʟᴇs ɪɴ @Anime_Weekends ᴄʜᴀɴɴᴇʟ  ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</blockquote>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5548954124 7393478297 7378365553 6465096751 1309776707 7186887048").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_PIC = os.environ.get("FORCE_PIC", "")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ᴀʀᴀ ᴀʀᴀ!! {mention}\n\n<b><blockquote>ᴀʀᴀ ʏᴏᴜ'ʀᴇ ᴍɪssɪɴɢ ᴏᴜᴛ ᴏɴ sᴏᴍᴇ sᴇʀɪᴏᴜs ᴀᴄᴛɪᴏɴ.ᴛo ᴜɴʟᴏᴄᴋ ᴀʟʟ ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ᴀᴄᴄᴇss ғɪʟᴇs, ᴊᴏɪɴ ᴀʟʟ of ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʙᴇʟᴏᴡ: !</blockquote></b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("@Movies_Stardust")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Auto delete time in seconds.
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "600"))
AUTO_DELETE_MSG = os.environ.get("AUTO_DELETE_MSG", "⚠️ Dᴜᴇ ᴛᴏ Cᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs....\n\n<blockquote>This file will be automatically deleted in {time} seconds. Please ensure you have saved any necessary content before this time.</blockquote>")
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", "<blockquote>уσυя fιℓє нαѕ вєєи ѕυccєѕѕfυℓℓу ∂єℓєтє∂! ♻️</blockquote>")

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b><blockquote>BOT UPTIME</b>\n{uptime}</blockquote>"
USER_REPLY_TEXT = "<blockquote>ᴀʀᴀ!! ᴀʀᴀ!! ɪᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ғᴏʀ ᴍʏ ʟᴏᴠᴇʟʏ ᴋᴀᴡᴀɪɪ 🥰 @chathub_stardust !</blockquote>"

ADMINS.append(OWNER_ID)
ADMINS.append(5548954124)

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
