import config

from pyrogram import filters
from pyrogram import enums
from Nandha import Nandha
from pyrogram.errors import (
PeerIdInvalid,UsernameInvalid )


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
         return await message.reply("`Wrong formatting method read help menu!`")
     if message.chat.type == enums.ChatType.PRIVATE:
        try:
            msg = await message.reply("**Getting Results.**.")
            user = await Nandha.get_users(user_id)
            user_id = user.id
            user_name = user.first_name
            user_mention = user.mention
            user_username = user.username
            user_dc = user.dc_id
            user_photo = await Nandha.download_media(user.photo.big_file_id,file_name=f"{user_name}.jpg")
            await message.reply_document(user_photo,caption=
                "**Profile Info**:\n"
                f"**ID**: `{user_id}`\n"
                f"**Name**: {user_name}\n"
                f"**Username**: @{user_username}\n"
                f"**Mention**: {user_mention}\n"
                f"**User DC**: `{user_dc}`")
            await msg.delete()           
        except Exception as e:
           await msg.edit(e)
     else:
        try:
            msg = await message.reply("**Getting Results.**.")
            m = await message.chat.get_member(user_id)
            user_id = m.user.id
            user_name = m.user.first_name
            user_mention = m.user.mention
            user_username = m.user.username
            user_dc = m.user.dc_id
            user_photo = await Nandha.download_media(m.user.photo.big_file_id,file_name=f"{user_name}.jpg")
            if m.privileges:
                status = "👮 Admin"
            else:
                status = "🧑‍🤝‍🧑 Member"
            await message.reply_document(user_photo,caption=
                "**Profile Info**:\n"
                f"**ID**: `{user_id}`\n"
                f"**Name**: {user_name}\n"
                f"**Username**: @{user_username}\n"
                f"**Mention**: {user_mention}\n"
                f"**User DC**: `{user_dc}`\n\n"
                f"**Status**: {status}")
            await msg.delete()
        except Exception as e:
            await msg.edit(e)


@Nandha.on_message(filters.command("id",config.CMDS))
async def ids(_, message):
      reply = message.reply_to_message
      if reply:
         id = "**Here The IDs**:\n\n"
         id += f"**Chat ID**: `{message.chat.id}`\n"
         id += f"**Replied ID**: `{reply.from_user.id}`\n"
         id += f"**Your ID**: `{message.from_user.id}`\n"
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
         await message.reply(text=(id))
      elif not reply:
              if len(message.text.split()) <2:
                  id = "**Here The IDs**:\n\n"
                  id += f"**Chat ID**: `{message.chat.id}`\n"
                  id += f"**Your ID**: `{message.from_user.id}`\n"
                  return await message.reply(text=(id))
              elif len(message.text.split()) >2:
                  return await message.reply("`wrong input!`")
              username = message.text.split()[1]
              id = "**Here The IDs**:\n\n"
              try:
                 they = await Nandha.get_chat(username)
                 id += f"**They ID**: `{they.id}`\n"
                 id += f"**Chat ID**: `{message.chat.id}`\n"
                 id += f"**Your ID**: `{message.from_user.id}`\n"
                 await message.reply(text=(id))
              except PeerIdInvalid:
                    await message.reply("`forward user msg and reply or direct reply user to get id I can't find the user so!`")
              except UsernameInvalid:
                   await message.reply("`please check the given input. no user found!`")
           
__MODULE__ = "Infos"

__HELP__ = """
**to know the user details!**
- `/info`: reply to user or give username to get info.
- `/id`: reply to user or give username to get id.
"""
