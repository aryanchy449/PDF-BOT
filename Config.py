import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6599601498:AAECxMbTH05BYSg0HOT4sR06s1H_CzCFVwc")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23080322"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "b3611c291bf82d917637d61e4a136535")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002111184944"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6214889840"))

#Port
PORT = os.environ.get("PORT", "8080")
