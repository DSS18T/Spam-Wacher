
import requests
from Nandha import Nandha as app
from pyrogram import filters
from pyrogram.types import *

from Nandha import mongodb

chatbotdb = mongodb.CHATBOT 


def get_chat():
     chats = []
     for chat_ids in chatbotdb.find():
          chats.append(chat_ids["chat_id"])
     return chats

def addchat(chat_id: int):
    if chat_id in get_chat():
      return
    return chatbotdb.insert_one({"chat_id": chat_id})

def removechat(chat_id: int):
    x = chatbotdb.find_one({"chat_id": chat_id})  
    chatbotdb.delete_one(x)

def is_chat(chat_id: int):
     x = chatbotdb.find_one({"chat_id": chat_id}) 
     if x:
        return True
     return False 

WRONG_FORMAT = "Required! (`on` or `off`)"

@app.on_message(filters.command("ai",["!","/","."]))
async def ai_on_or_off(_, message):
      chat = message.chat
      user = message.from_user
      if len(message.text.split()) <2: return await message.reply(WRONG_FORMAT)
      t = message.text.split()[1]
      if t == "on":
           if is_chat(chat.id) == True: return await message.reply("AI is Already Enabled Here!")
           else: add_chat(chat.id); return await message.reply("Successfully Enabled AI!")
      elif t == "off":
           if is_chat(chat.id) == False: return await message.reply("AI is Already Disabled Here!")
           else: remove_chat(chat.id); return await message.reply("Successfully Disabled AI!")
      else: return await message.reply(WRONG_FORMAT)
      
API_URL = "http://Iseria.up.railway.app/api={}/prompt={}"
API_KEY = "Lunab45e7e91-acd8-43d1-be1f-5a9ebdd472b2"

@app.on_message(filters.text, group=100)
async def ai(_, message):
      chat = message.chat
      reply = message.reply_to_message
      BOT_ID = (await app.get_me()).id
      if is_chat(chat.id) == True:
          if reply.from_user.id == BOT_ID:
                question = message.text
                answer = requests.get(API_URL.format(API_KEY,question)).json()
                return await message.reply(answer)
          
