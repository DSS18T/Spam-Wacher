import config

from pyrogram import filters
from pyrogram import enums
from Nandha import Nandha
from Nandha.help.admin import *

from pyrogram.types import *
from pyrogram.errors import (
PeerIdInvalid,UsernameInvalid, UserNotParticipant)


@Nandha.on_message(filters.command("info",config.CMDS))
async def info(_, message):
     reply = message.reply_to_message
     if reply:
          user_id = reply.from_user.id
     elif not reply and len(message.command) == 2:
          user_id = message.text.split()[1]
     elif not reply and len(message.command) == 1:
          user_id = message.from_user.id
     else:
         return await message.reply("`Wrong formatting Method Read help Menu!`")
     msg = await message.reply("**Getting Results.**.")
     try:
        user = await Nandha.get_users(user_id)
        user_id = user.id
        user_name = user.first_name
        user_mention = user.mention
        user_username = user.username
        user_dc = user.dc_id
        if user.photo:
            user_photo = await Nandha.download_media(user.photo.big_file_id,file_name=f"{user_name}.jpg")
     except Exception as e:
          await msg.edit(e)
     if message.chat.type == enums.ChatType.PRIVATE:
        try:
            if user.photo:
                await message.reply_photo(user_photo,caption=
                "**Profile Info**:\n"
                f"**ID**: `{user_id}`\n"
                f"**Name**: {user_name}\n"
                f"**Username**: @{user_username}\n"
                f"**Mention**: [{user_name}](tg://user?id={user_id})\n"
                f"**User DC**: `{user_dc}`",reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("More 📒", callback_data=f"userinfo:{user_id}"),
InlineKeyboardButton("❌", callback_data=f"delete:{user_id}")]]))
            elif not user.photo:
                await message.reply_text(text=
                "**Profile Info**:\n"
                f"**ID**: `{user_id}`\n"
                f"**Name**: {user_name}\n"
                f"**Username**: @{user_username}\n"
                f"**Mention**: [{user_name}](tg://user?id={user_id})\n"
                f"**User DC**: `{user_dc}`",reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("More 📒", callback_data=f"userinfo:{user_id}"),
InlineKeyboardButton("❌", callback_data=f"delete:{user_id}")]]))
            await msg.delete()           
        except Exception as e:
           await msg.edit(e)
     else:
        try:
            m = await message.chat.get_member(user_id)
            if m.custom_title:
               title = m.custom_title
            else: title = None
            if m.privileges:
                status = "Admin"
            else:
                status = "Member"
        except UserNotParticipant:
                status = "Not Member"
        try:        
            if user.photo:
               await message.reply_photo(user_photo,caption=
                "**Profile Info**:\n"
                f"**ID**: `{user_id}`\n"
                f"**Name**: {user_name}\n"
                f"**Username**: @{user_username}\n"
                f"**Mention**: {user_mention}\n"
                f"**User DC**: `{user_dc}`\n\n"
                f"**Status**: {status}\n"
                f"**Nick title**: {title}",reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("More 📒", callback_data=f"userinfo:{user_id}"),
InlineKeyboardButton("❌", callback_data=f"delete:{user_id}")]]))
            elif not user.photo:
                 await message.reply_text(text=
                "**Profile Info**:\n"
                f"**ID**: `{user_id}`\n"
                f"**Name**: {user_name}\n"
                f"**Username**: @{user_username}\n"
                f"**Mention**: {user_mention}\n"
                f"**User DC**: `{user_dc}`\n\n"
                f"**Status**: {status}\n"
                f"**Nick title**: {title}",reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("More 📒", callback_data=f"userinfo:{user_id}"),
InlineKeyboardButton("❌", callback_data=f"delete:{user_id}")]]))
            await msg.delete()
        except Exception as e:
           await msg.edit(e)


@Nandha.on_message(filters.command("id",config.CMDS))
async def ids(_, message):
      reply = message.reply_to_message
      if reply:
         id = ""
         id += f"**[Chat ID]({message.link})**: `{message.chat.id}`\n"
         id += f"**[Replied ID](tg://user?id={reply.from_user.id})**: `{reply.from_user.id}`\n"
         id += f"**[Your ID](tg://user?id={message.from_user.id})**: `{message.from_user.id}`\n"
         if reply.forward_from:
             id += f"**Forward From ID**:\n`{reply.forward_from.id}`\n"
         elif reply.left_chat_member:
             id += f"**left Member ID**: `{reply.left_chat_member.id}`\n"
         elif reply.new_chat_members:
             for new_member in reply.new_chat_members:
                   id += f"**New Member ID**: `{new_member.id}`\n"
         elif reply.photo:
             id += f"**Sent Photo ID**:\n`{reply.photo.file_id}`"
         elif reply.animation:
             id += f"**Sent Animation ID**:\n`{reply.animation.file_id}`"
         elif reply.audio:
             id += f"**Sent Audio ID**:\n`{reply.audio.file_id}`"
         elif reply.sticker:
             id += f"**Sent Sticker ID**:\n`{reply.sticker.file_id}`"
         await message.reply(text=(id),disable_web_page_preview=True)
      elif not reply:
              if len(message.text.split()) <2:
                  id = ""
                  id += f"**[Chat ID]({message.link})**: `{message.chat.id}`\n"
                  id += f"**[Your ID](tg://user?id={message.from_user.id})**: `{message.from_user.id}`\n"
                  return await message.reply(text=(id),disable_web_page_preview=True)
              elif len(message.text.split()) >2:
                  return await message.reply("`wrong input!`")
              username = message.text.split()[1]
              id = ""
              try:
                 they = await Nandha.get_chat(username)
                 id += f"**[They ID](tg://user?id={they.id})**: `{they.id}`\n"
                 id += f"**[Chat ID]({message.link})**: `{message.chat.id}`\n"
                 id += f"**[Your ID](tg://user?id={message.from_user.id})**: `{message.from_user.id}`\n"
                 await message.reply(text=(id), disable_web_page_preview=True)
              except PeerIdInvalid:
                    await message.reply("`forward user msg and reply or direct reply user to get id I can't find the user so!`")
              except UsernameInvalid:
                   await message.reply("`please check the given input. no user found!`")

@Nandha.on_callback_query(filters.regex("userinfo"))
async def userinfo_query(_, query):
       user_id = query.data.split(":")[1]
       try: user = await Nandha.get_users(user_id) 
       except Exception as e: return await message.reply(e)
       is_deleted = user.is_deleted
       is_bot = user.is_bot
       is_verified = user.is_verified
       is_restricted = user.is_restricted
       is_scam = user.is_scam
       is_fake = user.is_fake
       is_support = user.is_support
       is_premium = user.is_premium
       language_code = user.language_code
       await query.message.edit(text=
          f"**is_deleted**: `{is_deleted}`\n"
          f"**is_bot**: `{is_bot}`\n"
          f"**is_verified**: `{is_verified}`\n"
          f"**is_restricted**: `{is_restricted}`\n"
          f"**is_scam**: `{is_scam}`\n"
          f"**is_fake**: `{is_fake}`\n"
          f"**is_support**: `{is_support}`\n"
          f"**is_premium**: `{is_premium}`\n"
          f"**language_code**: `{language_code}`\n",reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("Return ◀️", callback_data=f"info:{user_id}"),
InlineKeyboardButton("❌", callback_data=f"delete:{user_id}")]]))


@Nandha.on_callback_query(filters.regex("info"))
async def info_query(_, query):
     user_id = query.data.split(":")[1]
     try: user = await Nandha.get_users(user_id) 
     except Exception as e: return await message.reply(e) 
     user_id = user.id
     user_name = user.first_name
     user_mention = user.mention
     user_username = user.username
     user_dc = user.dc_id
     if query.message.chat.type == enums.ChatType.PRIVATE:
        await query.message.edit(text=
                "**Profile Info**:\n"
                f"**ID**: `{user_id}`\n"
                f"**Name**: {user_name}\n"
                f"**Username**: @{user_username}\n"
                f"**Mention**: [{user_name}](tg://user?id={user_id})\n"
                f"**User DC**: `{user_dc}`",reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("More 📒", callback_data=f"userinfo:{user_id}"),
InlineKeyboardButton("❌", callback_data=f"delete:{user_id}")]]))
     else: 
        try:
            m = await query.message.chat.get_member(user_id)
            if m.custom_title:
               title = m.custom_title
            else: title = None
            if m.privileges:
                status = "Admin"
            else:
                status = "Member"
        except UserNotParticipant:
                status = "Not Member"
        await query.message.edit(text=
                "**Profile Info**:\n"
                f"**ID**: `{user_id}`\n"
                f"**Name**: {user_name}\n"
                f"**Username**: @{user_username}\n"
                f"**Mention**: {user_mention}\n"
                f"**User DC**: `{user_dc}`\n\n"
                f"**Status**: {status}\n"
                f"**Nick title**: {title}",reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("More 📒", callback_data=f"userinfo:{user_id}"),
InlineKeyboardButton("❌", callback_data=f"delete:{user_id}")]]))


@Nandha.on_callback_query(filters.regex("delete"))
async def delete(_, query):
     user_id = query.data.split(":")[1]
     if query.message.chat.type == enums.ChatType.PRIVATE:
          await query.message.delete()
     else: 
        if (await is_admin(query.message.chat.id,query.from_user.id)) == True or user_id == query.from_user.id:
              await query.message.delete()
        else: return await query.answer("You Can't Delete!", show_alert=True)


 
  
__MODULE__ = "Infos"

__HELP__ = """
**to know the user details!**
- `/info`: reply to user or give username to get info.
- `/id`: reply to user or give username to get id.
"""
