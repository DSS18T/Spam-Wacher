import requests

import config
from Nandha import Nandha
from pyrogram import filters


ACTIVE_CHAT = [
123456789,
987654321,]



@Nandha.on_message(filters.command("addchatbot",config.CMDS))
async def addchatbot(_, message):
    reply = message.reply_to_message
    if not message.chat.id in ACTIVE_CHAT:
            ACTIVE_CHAT.append(message.chat.id)
            await message.reply("Successfully ChatBot Active!")
            return
    else:
        await message.reply("This Chat Already Enabled ChatBot!")
    
@Nandha.on_message(filters.text, group=200)
async def chatbot(_, message):
     if message.chat.id in ACTIVE_CHAT:
          if message.reply_to_message.from_user.id == config.BOT_ID:
               Message = message.text
               API = requests.get("https://merissachatbot.tk/api/apikey=1491497760-MERISSAri2hds2WK4/groupprotectionbot/nandhaxd/message="+Message).json()
               await message.reply(API["reply"])
