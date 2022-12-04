





import config
import random

from Nandha import ( Nandha, mongodb )
from pyrogram import filters
from pyrogram.types import *


db = mongodb.AFK

afk_users = []


@Nandha.on_message(filters.command("afk",config.CMDS))
async def AFK_set(_, message):
   user_id = message.from_user.id
   try: afk = message.text.split(None,1)[1]
   except: afk = None
   db.insert_one({"user_id": user_id, "afk": afk})
   name = message.from_user.first_name
   return await message.reply_text("{} was AFK Now Bye Take A Reset 🤗".format(name))
   
   
@Nandha.on_message(group=100)
async def back_to_afk(_, message):
    try:
       user_id = message.from_user.id
       name = message.from_user.first_name
    except: pass
    is_db = db.find_one({"user_id": user_id})
    if is_db:
        db.delete_one(is_db)
        return await message.reply_text(f"welcome back {name} 🌚")
       
   
@Nandha.on_message(group=100)
async def afk(_, message):
     reply = message.reply_to_message
     try:
       user_id = message.from_user.id
       name = message.from_user.first_name
     except: pass
     for uid in db.find():
         afk_users.append(uid["user_id"])
     if reply and reply.from_user.id in afk_users:
           find = db.find_one({"user_id": user_id})
           afk = find["afk"]
           if afk == None:
             return await message.reply_text(
                 f"hey {name} was afk now!")
           else: return await message.reply(
                f"hey {name} was afk!\n reason: {afk}")
                                    
