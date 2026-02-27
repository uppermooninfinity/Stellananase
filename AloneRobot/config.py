
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "27795164" # integer value, dont use ""
    API_HASH = "b1c9ba3d6180a099e35d6498d8434bf0"
    TOKEN = "8593679944:AAEKHMwu0U_ngZ6eV48ZlSUA-K3UP6uMIhg"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 7651303468 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "snowy_hometown"  # Your own group for support, do not add the @
    START_IMG = "https://files.catbox.moe/74w3rx.jpg"
    EVENT_LOGS = (-1003634796457)# Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # RECOMMENDED
    DATABASE_URL = "postgres://avnadmin:AVNS_GGDm9qRk_Ng-cSB8fTh@pg-32f48f85-vezinfinity-a3fe.i.aivencloud.com:19650/defaultdb?sslmode=require"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "43Q2WQ4GWIDQIAAD"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "JW2836G01FZE"
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    CHATBOT_API="" # get it from @FallenChat_Bot using /token
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [7487670897,8409591285,8593679944]  # User id of sudo users
    DEV_USERS = [7487670897,8409591285,8593679944]  # User id of dev users
    DEMONS = [7487670897,8409591285,8593679944]  # User id of support users
    TIGERS = [7487670897,8409591285,8593679944]  # User id of tiger users
    WOLVES = [7487670897,8409591285,8593679944]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
