import os
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(os.getenv("API_ID", ""))

API_HASH = os.getenv("API_HASH", "")

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    os.getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)

LOGGER_ID = int(os.getenv("LOGGER_ID", ""))

OWNER_ID = int(os.getenv("OWNER_ID", ""))

BOT_USERNAME = os.getenv("BOT_USERNAME" , "")

COMMAND_HANDLER = os.getenv("COMMAND_HANDLER", "! / .").split()

HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

UPSTREAM_REPO = os.getenv(
    "UPSTREAM_REPO",
    "",
)
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "https://github.com/uppermooninfinity/Stellananase")
GIT_TOKEN = os.getenv(
    "GIT_TOKEN", ""
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/dark_musictm")
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/snowy_hometown")

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = os.getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    os.getenv("AUTO_SUGGESTION_TIME", "500"))

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "6fb7e1766693439b86ec57e3deb3c36f")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "da3f94c6a68d49f6b64a7216ec9eb905")



PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    os.getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 21474836480))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 21474836480))



# Get your pyrogram v2 session from @Shsusu_bot on Telegram
STRING1 = os.getenv("STRING_SESSION", "")
STRING2 = os.getenv("STRING_SESSION2", None)
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = os.getenv(
    "START_IMG_URL", "https://files.catbox.moe/k8ix72.jpg"
)
PING_IMG_URL = os.getenv(
    "PING_IMG_URL", "https://files.catbox.moe/k8ix72.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/k8ix72.jpg"
STATS_IMG_URL = "https://files.catbox.moe/k8ix72.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/k8ix72.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/k8ix72.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/k8ix72.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/k8ix72.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/k8ix72.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/k8ix72.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/k8ix72.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/k8ix72.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
