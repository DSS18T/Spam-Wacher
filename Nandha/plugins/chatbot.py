import requests

import config
from Nandha import Nandha
from pyrogram import filters


ACTIVE_CHAT = [
123456789,
987654321,]

@Nandha.on_message(filters.command("chatbot",config.CMDS))
async def chatbot(_, message):
    reply = message.reply_to_message
    if not message.chat.id in ACTIVE_CHAT:
            ACTIVE_CHAT.append(message.chat.id)
            await message.reply("ChatBot Successfully Active!")
            return
    if message.chat.id in ACTIVE_CHAT:
         if message.text:
               if reply.from_user.id == config.BOT_ID:
                   Message = message.text
                   API = requests.get(f"https://merissachatbot.tk/api/apikey=1491497760-MERISSAri2hds2WK4/groupprotectionbot/nandhaxd/message="+Message).json()
                   await message.reply(API["reply"])
