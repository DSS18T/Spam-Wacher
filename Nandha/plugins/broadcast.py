import config

from Nandha import Nandha
from pyrogram import filters
from Nandha.help.chatsdb import *
from Nandha.help.usersdb import *


@Nandha.on_message(filters.user(config.OWNER_ID) & filters.command("groupcast",config.CMDS))
async def global_cast(_, message):
      reply = message.reply_to_message
      chat = message.chat  
      if not reply: return await message.reply("Reply to Message to Forward My all Groups")
      success = "**Globally Cast**:\n**Success**: `{}`\n**Failed**: `{}`"
      list = get_chats(); done = 0; fail = 0
      for chat_id in list:
          try:
             await Nandha.forward_messages(chat_id, chat.id, reply.id)
             done +=+1
             await asyncio.sleep(3)
          except: fail +=+1      
      await message.reply(success.format(done, fail))
         
       
