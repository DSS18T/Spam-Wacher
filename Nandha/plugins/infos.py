import config

from pyrogram import filters
from pyrogram import enums
from Nandha import Nandha
from Nandha.help.admin import *

from pyrogram.types import *
from pyrogram.errors import (
PeerIdInvalid,UsernameInvalid, UserNotParticipant)

@Nandha.on_message(filters.command("info",config.CMDS))
async def user_info(_, message):
      " information about users "
      reply = message.reply_to_message
      if reply: user_id = reply.from_user.id
      elif not reply and len(message.text.split()) == 2: user_id = message.text.split()[1]
      elif not reply and len(message.text.split()) == 1: user_id = message.from_user.id
      else: return await message.reply("`somthing wrong reply a user or give me id to find user details!`")
      if message.chat.type == enums.ChatType.PRIVATE:
           msg = await message.reply("`Getting results\nPlease Wait!`")
           try: x = await Nandha.get_chat(user_id)
           except Exception as e: return await message.reply(e)
           text = "<b>Profile Info</b>:\n"
           text += "<b>Name</b>: {}\n".format(x.first_name)
           text += "<b>ID</b>: {}\n".format(x.id)
           text += "<b>Username</b>: @{}\n".format(x.username)
           text += "<b>Mention</b>: {}\n".format(f"[{x.first_name}](tg://user?id={x.first_name})")
           text += "<b>DC ID</b>: <code>{}</code>\n".format(x.dc_id)
           try:
              if x.photo:
                 profile = await Nandha.download_media(x.photo.big_file_id,file_name=f"{x.first_name}.jpg")
                 await message.reply_photo(profile, caption=text)
              else: await message.reply(text)
              await msg.delete()
           except Exception as e: return await message.reply(e)
      else: 
           msg = await message.reply("`Getting results\nPlease Wait!`")
           try: x = await message.chat.get_member(user_id)
           except UserNotParticipant: return await message.reply("This User Is Not Member Here To Give You Info You Can Dm Me To Find His/She Info!")
           except Exception as e: return await message.reply(e)
           text = "<b>Profile Info</b>:\n"
           text += "<b>Name</b>: {}\n".format(x.user.first_name)
           text += "<b>ID</b>: {}\n".format(x.user.id)
           text += "<b>Username</b>: @{}\n".format(x.user.username)
           text += "<b>Mention</b>: {}\n".format(f"[{x.user.first_name}](tg://user?id={x.user.first_name})")
           text += "<b>DC ID</b>: <code>{}</code>\n".format(x.user.dc_id)
           if x.joined_date:
                text += "<b>Join Date</b>: <code>{}</code>\n".format(x.joined_date)
           if x.custom_title:
                 text += "<b>Admin title</b>: <code>{}</code>\n".format(x.custom_title)
           if x.promoted_by:
                 text += "<b>Promote by</b>: <code>{}</code>\n".format(x.promoted_by.first_name)
           if x.privileges:
                 text += "<b>Status</b>: <code>{}</code>\n".format("Group Stuff")
           else: text += "<b>Status</b>: <code>{}</code>\n".format("Group Member")
           try:
                if x.user.photo: 
                    profile = await Nandha.download_media(x.user.photo.big_file_id,file_name=f"{x.user.first_name}.jpg")
                    await message.reply_photo(profile,caption=text)
                else: await message.reply(text)
                await msg.delete() 
           except Exception as e: return await message.reply(e) 
      


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

__HELP__ = """ **to know the user details!**
\n• `/info`: reply to user or give username to get info.
•`/id`: reply to user or give username to get id.
"""
