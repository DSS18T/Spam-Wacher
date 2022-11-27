
from Nandha import (
mongodb, Nandha, )

from pyrogram.types import *
from pyrogram import filters 
from Nandha.help.admin import *

db = mongodb["WARNNING"]


WARN_TEXT = """
WARNNING ⚠️
name: {name}
uid: {user_id}

warns: {warns}
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
         reply = message.reply_to_message
         if reply: user_id = reply.from_user.id
         elif not reply and len(message.text.split()) >1: user_id = message.text.split()[1]
         else: return await message.reply_text("Invalid Method!")
         x = db.find_one({"chat_id": chat.id, "user_id": user_id})
         if bool(x):
             n_warn = int(x["warn"])+1
             db.update_one({"chat_id": chat.id, "user_id": user_id}, {"$set": {"warn": n_warn}})
         else:
             ll = {"chat_id": chat.id, "user_id": user.id, "warn": 1}
             db.insert_one(ll)
         user = await Nandha.get_users(user_id)
         y = db.find_one({"chat_id": chat.id, "user_id": user_id})
         warns = int(y["warn"])
         return await message.reply_text(WARN_TEXT.format(name=user.first_name, user_id=user.id, warns=warns))
