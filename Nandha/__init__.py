import time
import config
import logging
import asyncio
import pyromod.listen
from pymongo import MongoClient 
from pyrogram import Client , idle
from aiohttp import ClientSession
from pyrogram.enums import ParseMode

MOD_LOAD = []
MOD_NOLOAD = []
START_TIME = time.time()


# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()],
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)


plugins = dict(root="Nandha")



Nandha = Client("NandhaBOT",
api_id=config.APP_ID, 
api_hash=config.APP_HASH,
bot_token=config.TOKEN,
plugins=plugins,
parse_mode=ParseMode.DEFAULT)
       

session = ClientSession()

MONGO = "use your own db url #hehe"
mongo = MongoClient(MONGO)
mongodb = mongo.NANDHA
