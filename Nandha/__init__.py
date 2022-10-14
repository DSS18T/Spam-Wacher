import logging

from pyrogram import Client



# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()],
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)


APP_ID = 583311
APP_HASH = "c67090d2c0a37d207385d04d9640045c"
TOKEN = "5720769813:AAEMCkgcEB-t0J7MVFr75QG4lshVwMHQ7O8"

Nandha = Client(
"Nandha", 
api_id=int(APP_ID), 
api_hash=str(APP_HASH), 
bot_token=str(TOKEN),
plugins=dict(root="Nandha"))



     
