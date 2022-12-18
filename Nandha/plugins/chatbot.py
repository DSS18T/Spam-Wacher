import config
import requests
from Nandha import Nandha, mongodb
from pyrogram import filters
from pyrogram.types import *



db = mongodb.CHATBOT


def list():
   list = []
   for x in db.find():
       list.append(x["chat_id"])
   return list

def add(chat_id: int):
    db.insert_one({"chat_id": chat_id, "chatbot": True})


def off_chatbot(chat_id: int):
    db.update_one({"chat_id": chat_id}, {"$set": {"chatbot": False}})

def on_chatbot(chat_id: int):
    db.update_one({"chat_id": chat_id}, {"$set": {"chatbot": True}})

def action(chat_id: int):
    x = db.find_one({"chat_id": chat_id})
    if x:
       return True
    return False


@Nandha.on_message(filters.command("chatbot"))
async def chatbot_on_off(_, message):
    chat_id = message.chat.id
    if len(message.text.split()) <2:
         oh = action(chat_id)
         return await message.reply_text(
            "None: you don't add a chatbot in ur chat ever.\n"
            "True: chatbot is enabled in ur chat.\n"
            "False: chatbot is disabled in ur chat.\n\n"
            f"This group chatbot is **{oh}**")
    pattern = message.text.split()[1]
    if pattern == "on":
          if chat_id not in list():
               add(chat_id)
               return await message.reply_text("Successfully chatbot Enabled!")
          else:
              on_chatbot(chat_id)
              return await message.reply_text("Successfully chatbot Enabled!")
    elif pattern == "off":
           if chat_id not in list():
               return await message.reply_text("Here is no chatbot Enabled!")
           else:
               off_chatbot(chat_id)
               return await message.reply_text("Successfully chatbot Disabled!")
    else: return await message.reply_text("Format: /chatbot on | off")
          


@Nandha.on_message(filters.text & filters.reply, group=100)
async def chatbot(_, message):
     chat_id = message.chat.id
     hmm = action(chat_id)
     bot_id = Nandha.me.id
     if action:
         if message.reply_to_message.from_user.id == bot_id:
                string = message.text
                if len(string.split()) > 2:
                     question = string.replace(" ", "%20")
                else: 
                     question = string
                text = requests.get("https://apikatsu.otakatsu.studio/api/chatbot/cleverbot?name=Vegeta&owner=Nandha&message="+question).json()["reply"]
                try:
                   await Nandha.send_message(
                        chat_id, 
                        text=text, 
                        reply_to_message_id=message.id)
                except Exception as e: return await message.reply(f"this an error you need contact support group. {e}")


       
