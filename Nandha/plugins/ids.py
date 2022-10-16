import config

from pyrogram import filters
from Nandha import Nandha
from pyrogram.errors import (
PeerIdInvalid,UsernameInvalid )

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
                  return await message.reply("`Input username to get ID else reply!`")
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
           
