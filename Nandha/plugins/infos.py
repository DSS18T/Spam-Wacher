import config

from pyrogram import filters
from pyrogram import enums
from Nandha import Nandha
from pyrogram.errors import (
PeerIdInvalid,UsernameInvalid, UserNotParticipant)
from pyrogram.raw.functions.users import GetFullUser
from pyrogram.file_id import FileId, FileType, ThumbnailSource

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
        info_user = await Nandha.invoke(GetFullUser(id=(await client.resolve_peer(user.id))))
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
            if info_user[0].photo.has_video == True:
               file_obj = BytesIO()
               profile_vid = info_user.video_sizes[0] if info_user.video_sizes else None
               async for chunk in Nandha.stream_media(
                    message=FileId(
                     file_type=FileType.PHOTO,
                     dc_id=info_user.dc_id,
                     media_id=info_user.id,
                     access_hash=info_user.access_hash,
                     file_reference=info_user.file_reference,
                     thumbnail_source=ThumbnailSource.THUMBNAIL,
                     thumbnail_file_type=FileType.PHOTO,
                     thumbnail_size=profile_vid.type,
                     volume_id=0,
                     local_id=0,
                     ).encode(),
                 ):
                   file_obj.write(chunk)
                   file_obj.name = "profile_vid_.mp4"
                   await message.reply_video(
                   video=file_obj,
                   caption="**Profile Info**:\n"
                f"**ID**: `{user_id}`\n"
                f"**Name**: {user_name}\n"
                f"**Username**: @{user_username}\n"
                f"**Mention**: [user_name](tg://user?id={user_id})\n"
                f"**User DC**: `{user_dc}`")

            elif info_user[0].photo.has_video == False:
                await message.reply_photo(user_photo,caption=
                "**Profile Info**:\n"
                f"**ID**: `{user_id}`\n"
                f"**Name**: {user_name}\n"
                f"**Username**: @{user_username}\n"
                f"**Mention**: [user_name](tg://user?id={user_id})\n"
                f"**User DC**: `{user_dc}`")
            elif not info_user[0].photo:
                await message.reply_text(text=
                "**Profile Info**:\n"
                f"**ID**: `{user_id}`\n"
                f"**Name**: {user_name}\n"
                f"**Username**: @{user_username}\n"
                f"**Mention**: [user_name](tg://user?id={user_id})\n"
                f"**User DC**: `{user_dc}`")
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
                f"**Nick title**: {title}") 
            elif not user.photo:
                 await message.reply_text(text=
                "**Profile Info**:\n"
                f"**ID**: `{user_id}`\n"
                f"**Name**: {user_name}\n"
                f"**Username**: @{user_username}\n"
                f"**Mention**: {user_mention}\n"
                f"**User DC**: `{user_dc}`\n\n"
                f"**Status**: {status}\n"
                f"**Nick title**: {title}")
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
