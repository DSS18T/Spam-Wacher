import config

from Nandha import Nandha
from Nandha.help.admin import *
from pyrogram import filters

@Nandha.on_message(filters.command("ban",config.CMDS))
async def bans(_, message):
      user_id = int(message.from_user.id)
      chat_id = int(message.chat.id)
      reply = message.reply_to_message
      if reply and (await can_ban_members(chat_id, user_id)) == True or user_id == config.OWNER_ID:    
           if reply and len(message.command) <2:
                user_id = reply.from_user.id
           elif reply and len(message.command) >2:
                user_id = reply.from_user.id
                reason = message.text.replace("ban", "")
                if (await is_admin(chat_id, config.BOT_ID)) == False:
                      return await message.reply_text("`make you sure I'm Admin!`")
                elif user_id == config.BOT_ID:
                      return await message.reply_text("`I can't ban myself!`")
                elif (await is_admin(chat_id, user_id)) == True:
                      return await message.reply_text("`The User Is Admin! I can't ban!`")
                try:
                   if reply and len(message.command) <2:
                         await Nandha.ban_chat_member(chat_id, user_id)
                         await message.reply_text(f"Successfully BANNED!\n• `{user_id}`")
                   elif reply and len(message.command) >2:
                         await Nandha.ban_chat_member(chat_id, user_id)
                         await message.reply_text(f"Successfully BANNED!\n • `{user_id}`\n\nFollowing Reason:\n`{reason}`")
                except Exception as e:
                     await message.reply(str(e))

      elif not reply and (await can_ban_members(chat_id, user_id)) == True or user_id == config.OWNER_ID:
            if len(message.command) <2:
                 user_id = message.command[1]
            elif len(message.command) >2:
                user_id = message.command[1]
                reason = message.text.split(str(user_id))[1]
            if (await is_admin(chat_id, config.BOT_ID)) == False:
                   return await message.reply_text("`make you sure I'm Admin!`")
            elif user_id == config.BOT_ID:
                  return await message.reply_text("`I can't ban myself!`")
            elif (await is_admin(chat_id, user_id)) == True:
                  return await message.reply_text("`The User Is Admin! I can't ban!`")         
            try:
                 if len(message.command) <2:
                       await Nandha.ban_chat_member(chat_id, user_id)
                       await message.reply_text(f"Successfully BANNED!\n• `{user_id}`")
                 elif len(message.command) >2:
                        await Nandha.ban_chat_member(chat_id, user_id)
                        await message.reply_text(f"Successfully BANNED!\n • `{user_id}`\n\nFollowing Reason:\n`{reason}`")
            except Exception as e:
                    await message.reply(str(e))







