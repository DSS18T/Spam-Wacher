import config

from Nandha import Nandha
from Nandha.help.admin import *
from pyrogram import filters

@Nandha.on_message(filters.command("ban",config.CMDS))
async def bans(_, message):
      user_id = int(message.from_user.id)
      chat_id = int(message.chat.id)
      reply = message.reply_to_message
      if reply and (await can_ban_members(chat_id,user_id)) == True: 
          await message.reply_text("yeh banning....")
          if len(message.command) <2:
             ban_id = reply.from_user.id
          elif len(message.command) >2:
              ban_id = reply.from_user.id
              reason = message.text.split(None, 1)[1]
              if (await is_admin(chat_id, config.BOT_ID)) == False:
                   return await message.reply_text("`Make you sure I'm Admin!`")
              elif ban_id == config.BOT_ID:
                   return await message.reply_text("`I can't ban myself!`")
              elif (await is_admin(chat_id, ban_id)) == True:
                   return await message.reply_text("`The User Is Admin! I can't ban!`")
              else:
                  if len(message.command) <2:
                          await Nandha.ban_chat_member(chat_id, ban_id)
                          await message.reply_text(f"Successfully BANNED!\n• `{ban_id}`")
                  elif len(message.command) >2:
                          await Nandha.ban_chat_member(chat_id, ban_id)
                          await message.reply_text(f"Successfully BANNED!\n • `{ban_id}`\n\nFollowing Reason:\n`{reason}`")
              
