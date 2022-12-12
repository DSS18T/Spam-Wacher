





import config
import random
import re
from Nandha import ( Nandha, mongodb )
from pyrogram import filters
from pyrogram.types import *


db = mongodb.AFK


def afk_users():
    afk_users = []
    for find in db.find():
        afk_users.append(find["user_id"])
    return afk_users


@Nandha.on_message(group=20)
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
    
    
    if message.from_user.id in afk_users():
          find = db.find_one({"user_id": user_id})
          db.delete_one(find)
          return await message.reply_text(f"Welcome Back {name} 🌚!")

@Nandha.on_message(filters.reply , group=20)
async def afk_s(_, message):
    reply = message.reply_to_message
    reply_uid = reply.from_user.id
    reply_uname = reply.from_user.first_name
    if reply_uid in afk_users():
           await message.reply("his offline!")
