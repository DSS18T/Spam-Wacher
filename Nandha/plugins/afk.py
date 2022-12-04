





import config
import random
import re
from Nandha import ( Nandha, mongodb )
from pyrogram import filters
from pyrogram.types import *


db = mongodb.AFK

afk_users = []

@Nandha.on_message(group=100)
async def AFK(_, message):
    text = message.text
    try:
       user_id = message.from_user.id
       name = message.from_user.first_name
    except: pass
    if re.search("^afk", text.split(text[0])[1]):
          try:
              afk = message.text.split(None,1)[1]
          except: afk = None
          db.insert_one({"user_id": user_id, "afk": afk})
          return await message.reply_text("Bye {name} Take A Rest! 👻")
    
    for find in db.find():
         afk_users.append(find["user_id"])
    try:
       reply = message.reply_to_message
       reply_uid = reply.from_user.id
       reply_uname = reply.from_user.first_name
    except: pass
    if reply and reply_uid in afk_users:
           find = db.find_one({"user_id": user_id})
           if find["afk"] == None: return await message.reply_text(f"{reply_uname}'s was afk! 🌚")
           else: afk = find["afk"]
           return await message.reply_text(f"{reply_uname}'s was afk!\nreason: {afk}")
    if message.from_user.id in afk_users:
          find = db.find_one({"user_id": user_id})
          db.delete_one(find)
          return await message.reply_text("Welcome Back {name} 🌚!")

