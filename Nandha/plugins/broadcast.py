import config
import asyncio
from Nandha import Nandha
from pyrogram import filters
from Nandha.help.chatsdb import *
from Nandha.help.usersdb import *


@Nandha.on_message(filters.user(config.OWNER_ID) & filters.command("groupcast",config.CMDS))
async def global_cast(_, message):
      reply = message.reply_to_message
      chat = message.chat  
      if not reply: return await message.reply("Reply to Message to Brodcast!")
      success = "**Global Brodcast**:\n**Success**: `{}`\n**Failed**: `{}`"
      msg = await message.reply("`Please wait Some Minutes!`", quote=True)
      list_1 = get_chats()
      list_2 = get_users()
      chat_id = []
      for id in list_1:
         chat_id.append(id)
      for id in list_2:
         chat_id.append(id)
      done = 0
      for ids in chat_id:
          try:
             await Nandha.copy_message(ids, chat.id, reply.id)
             done +=+1
             await asyncio.sleep(3)
          except: fail = len(chat_id)-done    
      return await msg.edit(success.format(done, fail))
         
       
