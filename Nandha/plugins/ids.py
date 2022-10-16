import config

from pyrogram import filters
from Nandha import Nandha


@Nandha.on_message(filters.command("id",config.CMDS))
async def ids(_, message):
      reply = message.reply_to_message
      if reply:
         id = "`Here The IDs`:\n\n"
         id += f"**Chat ID**: `{message.chat.id}`\n"
         id += f"**Replied ID**: `{reply.from_user.id}`\n"
         id += f"**Your ID**: `{message.from_user.id}`\n"
         if reply.forward_from:
             id += f"**Forward From ID**:\n`{reply.forward_from.id}`\n"
         elif reply.left_chat_member:
             id += f"**left User ID**: `{reply.left_chat_member.id}`\n"
         elif reply.new_chat_members:
             id += f"**New User ID**: `{reply.new_chat_members.id}`\n"
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
                  return await message.reply("`Input username to get ID else reply!`")
              username = message.text.split()[1]
              try:
                 id = "`Here The IDs`:\n\n"
                 they = await Nandha.get_users(username)
                 id += f"**They ID**: `{they.id}`\n"
                 id += f"**Chat ID**: `{message.chat.id}`\n"
                 id += f"**Your ID**: `{message.from_user.id}`\n"
              except Exception as e:
                   await message.reply(e)
           
