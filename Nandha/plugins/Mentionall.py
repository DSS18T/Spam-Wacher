import config
import asyncio

from pyrogram import filters
from pyrogram.types import * 
from pyrogram.enums import ChatType

from Nandha import Nandha
from Nandha.help.admin import is_owner


@Nandha.on_message(filters.command("all",config.CMDS))
async def MentionAll(_, message):
      user_id = message.from_user.id
      chat_id = message.chat.id

      replied = message.reply_to_message

      if message.chat.type == ChatType.PRIVATE:
           return await message.reply_text("Sorry you can use This command only in groups!")
           
      if (await is_owner(chat_id,user_id)) == True:
             MembersID = []
             async for a in Nandha.get_chat_members(chat_id):
                     MembersID.append(a.user.id)
             
             
             if replied:
                   string = ""
                   for x in MembersID:
                       k = await Nandha.get_users(x)
                       string += f"[{k.first_name}](tg://user?id={k})"
                   await message.reply_to_message.reply_text(string)
             else:
                   string = ""
                   for x in MembersID:
                       k = await Nandha.get_users(x)
                       string += f"[{k.first_name}](tg://user?id={k})"
                   await message.reply_text(string)
                    
      return await message.reply_text("Sorry Group Owner Only Can Mention All!")
