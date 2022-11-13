import config

from Nandha import Nandha
from pyrogram import filters
from Nandha.help.chatsdb import *
from Nandha.help.usersdb import *


@Nandha.on_message(filters.user(config.OWNER_ID) & filters.command("groupcast",config.CMDS))
async def global_cast(_, message):
      list = get_chats()
      reply = message.reply_to_message
      chat = message.chat
      done = 0
      fail = 0
      if not reply: return await message.reply("Reply to Message to Forward My all Groups")
      success = "**Globally Cast**:\n**Success**: `{}`\n**Failed**: `{}`"
      for chat_id in list:
          try:
             await Nandha.forward_messages(chat.id, chat_id, reply.id)
             done +=+1
             await asyncio.sleep(3)
          except: fail +=+1      
      await message.reply(success.format(done, fail))
         
       
