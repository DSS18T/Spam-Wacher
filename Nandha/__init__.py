import logging
import pyromod.listen
from pymongo import MongoClient 
from pyrogram import Client
from aiohttp import ClientSession
from pyrogram.enums import ParseMode

MOD_LOAD = []
MOD_NOLOAD = []


# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()],
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)


APP_ID = 583311
APP_HASH = "c67090d2c0a37d207385d04d9640045c"
TOKEN = "5561055962:AAGfx5ln_s6PHjFEZ1w2SSc1Z4yIdk3JxZ4"


plugins = dict(root="Nandha")

Nandha = Client("Nandha", 
api_id=APP_ID, 
api_hash=APP_HASH,
bot_token=TOKEN,
plugins=plugins,
parse_mode=ParseMode.DEFAULT)


UB = Client("UB",
api_id =APP_ID,
api_hash=APP_HASH,
session_string=config.SESSION)

async def main():
    await UB.start()
    await UB.stop()


UB.run(main())

     
session = ClientSession()

MONGO = "mongodb+srv://nandhaxd:rw5T7YJRjsE3fmk3@cluster0.80igexg.mongodb.net/?retryWrites=true&w=majority"
mongo = MongoClient(MONGO)
mongodb = mongo.NANDHA
