import config

from Nandha import (
mongodb, Nandha, )

from pyrogram.types import *
from pyrogram import filters 
from Nandha.help.admin import *

db = mongodb["WARNING"]


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


async def is_warn_user(chat_id: int, user_id: int):
      x = db.find_one({"chat_id": chat.id, "user_id": user_id})
      if bool(x):
         return True
      else: return False

async def get_warn_count(chat_id: int, user_id: int):
    x = db.find_one({"chat_id": chat.id, "user_id": user_id})
    warns = x["warn"]
    return warns

@Nandha.on_message(filters.command("clearwarn",config.CMDS))
async def clear_warns(_, message):
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
       user = await Nandha.get_users(user_id)
       if bool(x):
            db.delete_one(x)
            await message.reply_text("{} Successfully Warns Cleared!".format(user.mention))
            return
       else: return await message.reply_text("No Warns Restored in that ID!")

@Nandha.on_message(filters.command("warn",config.CMDS))
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
         if bool(x):
             n_warn = int(x["warn"])+1
             db.update_one({"chat_id": chat.id, "user_id": user_id}, {"$set": {"warn": n_warn}})
             if n_warn > 2:
                  await Nandha.ban_chat_member(chat_id=chat.id, user_id=user.id)
                  await message.reply_text(WARN_B_TEXT.format(name=user.mention, user_id=user.id,admin=message.from_user.mention, warns=n_warn))
                  db.delete_one(x)
                  return
         else:
             ll = {"chat_id": chat.id, "user_id": user_id, "warn": 1}
             db.insert_one(ll)
         x = db.find_one({"chat_id": chat.id, "user_id": user_id})
         warns = int(x["warn"])
         return await message.reply_text(WARN_TEXT.format(name=user.mention, user_id=user.id,admin=message.from_user.mention, warns=warns))
