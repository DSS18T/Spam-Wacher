import logging

from pymongo import MongoClient 
from pyrogram import Client
from aiohttp import ClientSession



# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()],
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)


APP_ID = 583311
APP_HASH = "c67090d2c0a37d207385d04d9640045c"
TOKEN = "5720769813:AAFWumamWPt-2TnK-ZJyJSy-R_i5ImSVXis"


plugins = dict(root="Nandha")

Nandha = Client("Nandha", 
api_id=APP_ID, 
api_hash=APP_HASH,
bot_token=TOKEN,
plugins=plugins)



     
session = ClientSession()

MONGO = "mongodb+srv://bikashhalder1234444:bikash890@cluster0.c7hlkrv.mongodb.net/?retryWrites=true&w=majority"
mongo = MongoClient(MONGO)
mongodb = mongo.NANDHA
