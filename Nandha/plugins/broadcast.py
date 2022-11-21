import config
import asyncio
from Nandha import Nandha
from pyrogram import filters
from Nandha.help.chatsdb import *
from Nandha.help.usersdb import *


@Nandha.on_message(filters.user(config.OWNER_ID) & filters.command(["groupcast","pgroupcast"],config.CMDS))
async def group_cast(_, message):
      reply = message.reply_to_message
      chat = message.chat  
      if not reply: return await message.reply("Reply to Message to Brodcast!")
      success = "**Group Brodcast**:\n**Success**: `{}`\n**Failed**: `{}`"
      msg = await message.reply("`Please wait Some Minutes!`", quote=True)      
      chat_id = []
      for id in get_chats():
         chat_id.append(id)
      done = 0
      for ids in chat_id:
          try:
             cast = await Nandha.copy_message(ids, chat.id, reply.id)
             done +=+1
             if message.text[1].casefold() == "p":
                 try: await cast.pin()
                 except: pass
             await asyncio.sleep(3)
          except: fail = len(chat_id)-done    
      return await msg.edit(success.format(done, fail))
         
       
@Nandha.on_message(filters.user(config.OWNER_ID) & filters.command(["usercast","pusercast"],config.CMDS))
async def user_cast(_, message):
      reply = message.reply_to_message
      chat = message.chat  
      if not reply: return await message.reply("Reply to Message to Brodcast!")
      success = "**User Brodcast**:\n**Success**: `{}`\n**Failed**: `{}`"
      msg = await message.reply("`Please wait Some Minutes!`", quote=True)      
      chat_id = []
      for id in get_users():
         chat_id.append(id)
      done = 0
      for ids in chat_id:
          try:
             cast = await Nandha.copy_message(ids, chat.id, reply.id)
             done +=+1
             if message.text[1].casefold() == "p":
                 try: await cast.pin()
                 except: pass
             await asyncio.sleep(3)
          except: fail = len(chat_id)-done    
      return await msg.edit(success.format(done, fail))
         
       
