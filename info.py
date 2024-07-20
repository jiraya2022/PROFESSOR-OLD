import re
from os import environ
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
from time import time

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
PORT = environ.get("PORT", "8080")
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '24579842'))
API_HASH = environ.get('API_HASH', 'ec6105bf1a02c98f837300546dc341d1')
BOT_TOKEN = environ.get('BOT_TOKEN', "7388432028:AAGtDAQzhMYyth98GeC_EhP17kHxA-QCT2E")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS' ,'https://i2f9m2t2.rocketcdn.me/wp-content/uploads/2014/04/shutterstock_175386392.jpg')).split()
BOT_START_TIME = time()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1991522624').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002221041331').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001821560097')
auth_grp = environ.get('AUTH_GROUP', '-1001660893308')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://hhh20:hhh20@cluster0.b9rbm8x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#maximum search result buttos count in number#
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "8"))
START_MESSAGE = environ.get('START_MESSAGE', '<b>Mʏ Nᴀᴍᴇ Is #Mɪɴᴀᴛᴏ. Wᴇ Aʀᴇ Pʀᴏᴠɪᴅᴇ Aɴʏ Mᴏᴠɪᴇ Sᴇʀɪᴇs Aɴɪᴍᴇ.\n\nWᴇ Aʀᴇ A Bʀᴀɴᴅ Wʜᴏ Pʀᴏᴠɪᴅᴇ Aʟʟ Kɪɴᴅ Oғ Cᴏɴᴛᴇɴᴛ Tᴏ Mᴇᴍʙᴇʀs Wɪᴛʜ Nᴏ Cᴏsᴛ.\n\nJᴜsᴛ Sᴇɴᴅ Aɴʏ Mᴏᴠɪᴇ Nᴀᴍᴇ Aɴᴅ Gᴇᴛ Wʜᴀᴛ Yᴏᴜ Dʀᴇᴀᴍ Iɴ Yᴏᴜʀ Lɪғᴇ....</b>')
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", "⚠️ Tʜᴀᴛ's Nᴏᴛ Fᴏʀ Yᴏᴜ. Pʟᴇᴀsᴇ Rᴇᴏ̨ᴜᴇsᴛ Yᴏᴜʀ Oᴡɴ")
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', '<b>Yᴏᴜ Hᴀᴠᴇ Nᴏᴛ Jᴏɪɴᴇᴅ Mʏ Cʜᴀɴɴᴇʟ Sᴏ Pʟᴇᴀsᴇ Jᴏɪɴ Aɴᴅ Gᴇᴛ Wʜᴀᴛ Yᴏᴜ Dʀᴇᴀᴍ Iɴ Yᴏᴜʀ Lɪғᴇ....</b>')
RemoveBG_API = environ.get("RemoveBG_API", "")
WELCOM_PIC = environ.get("WELCOM_PIC", "https://i2f9m2t2.rocketcdn.me/wp-content/uploads/2014/04/shutterstock_175386392.jpg")
WELCOM_TEXT = environ.get("WELCOM_TEXT", "welcome to the happy hour")
PMFILTER = bool(environ.get("PMFILTER", 'True'))
G_FILTER = bool(environ.get("G_FILTER", True))
BUTTON_LOCK = bool(environ.get("BUTTON_LOCK", False))

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1002106576609))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'ThappyHour')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b><a href='https://t.me/ThappyHour'>{file_name}</a></b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "<b><a href='https://t.me/ThappyHour'>{file_name}</a></b>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10</b>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

#log srt
LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"


