





import config
import random
import re
from Nandha import ( Nandha, mongodb )
from pyrogram import filters
from pyrogram.types import *


db = mongodb.AFK


@Nandha.on_message(group=100)
async def AFK(_, message):
    text = message.text
    try:
       user_id = message.from_user.id
       name = message.from_user.first_name
    except: pass
    try:
      if re.search("^afk", text.split(text[0])[1]):
           try:
               afk = message.text.split(None,1)[1]
           except: afk = False
           db.insert_one({"user_id": user_id, "afk": afk})
           return await message.reply_text(f"Bye {name} Take A Rest! 👻")
    except: pass
    
    afk_users = []

    for find in db.find():
         afk_users.append(find["user_id"])

    if message.from_user.id in afk_users:
          find = db.find_one({"user_id": user_id})
          db.delete_one(find)
          return await message.reply_text(f"Welcome Back {name} 🌚!")

@Nandha.on_message(group=100)
async def hmm(_, message):

    afk_users = []

    for find in db.find():
         afk_users.append(find["user_id"])

    reply_uid = reply.from_user.id
    reply_uname = reply.from_user.first_name
    reply = message.reply_to_message

    if reply and reply_uid in afk_users:
           find = db.find_one({"user_id": reply_uid})
           if find["afk"] == False:
                return await message.reply_text(f"{reply_uname}'s was afk! 🌚")
           else: 
                afk = find["afk"]
                return await message.reply_text(f"{reply_uname}'s was afk!\nreason: {afk}")

