import config

from Nandha import (
mongodb, Nandha, )

from pyrogram.types import *
from pyrogram import filters 
from Nandha.help.admin import *

db = mongodb["WARNNING"]


WARN_TEXT = """
WARNING!
name: {name}
uid: [`{user_id}`]
warn by {admin}
total warns: [`{warns}`]
"""
WARN_B_TEXT = """
BANNED!
name: {name}
uid: [`{user_id}`]
warn by {admin}
total warns: [`{warns}`]
"""

@Nandha.on_message(filters.command("warn"))
async def warn(_, message):
     user = message.from_user
     chat = message.chat
     if await is_admin(chat_id=chat.id, user_id=user.id) == False:
           return await message.reply_text("Admins Only Can Warn Members!")
     elif await can_ban_members(chat_id=chat.id, user_id=user.id) == False:  
           return await message.reply_text("You Needs a can_restrict_members Rights!")
     else:
         if await is_admin(chat_id=chat.id, user_id=config.BOT_ID) == False:
              return await message.reply_text("Make Me Admin First Baka!")
         elif await can_ban_members(chat_id=chat.id, user_id=config.BOT_ID) == False:  
              return await message.reply_text("I Needs a can_restrict_members Rights!")
         reply = message.reply_to_message
         if reply: user_id = reply.from_user.id
         elif not reply and len(message.text.split()) >1: user_id = message.text.split()[1]
         else: return await message.reply_text("Invalid Method!")
         x = db.find_one({"chat_id": chat.id, "user_id": user_id})
         user = await Nandha.get_users(user_id)
         elif bool(x):
             n_warn = int(x["warn"])+1
             db.update_one({"chat_id": chat.id, "user_id": user_id}, {"$set": {"warn": n_warn}})
             if n_warn == 3:
                  await Nandha.ban_chat_member(chat.id, user_id)
                  await message.reply_text(WARN_B_TEXT.format(name=user.mention, user_id=user.id,admin=message.from_user.mention, warns=warns))
                  return
         else:
             ll = {"chat_id": chat.id, "user_id": user_id, "warn": 1}
             db.insert_one(ll)
         x = db.find_one({"chat_id": chat.id, "user_id": user_id})
         warns = int(x["warn"])
         return await message.reply_text(WARN_TEXT.format(name=user.mention, user_id=user.id,admin=message.from_user.mention, warns=warns))
