import config

from pyrogram import filters
from Nandha import Nandha


@Nandha.on_message(filters.command("id",config.CMDS))
async def ids(_, message):
      reply = message.reply_to_message
      if reply:
         id = "`here the ids`:\n\n"
         id += f"**Chat ID**: `{message.chat.id}`\n"
         id += f"**Replied ID**: `{reply.from_user.id}`\n"
         id += f"**Your ID**: `{message.from_user.id}`\n"
         if reply.forward_from:
             id += f"**Forward From ID**:\n`{reply.forward_from.id}`\n"
         elif reply.forward_from.photo:
             id += f"**Photo ID**:\n`{reply.forward_from.photo.file_id}`"
         elif reply.forward_from.animation:
             id += f"**Animation ID**:\n`{reply.forward_from.animation.file_id}`"
         elif reply.forward_from.audio:
             id += f"**Audio ID**:\n`{reply.forward_from.audio.file_id}`"
         elif reply.forward_from.sticker:
             id += f"**Sticker ID**:\n`{reply.forward_from.sticker.file_id}`"
         elif reply.photo:
             id += f"**Photo ID**:\n`{reply.photo.file_id}`"
         elif reply.animation:
             id += f"**Animation ID**:\n`{reply.animation.file_id}`"
         elif reply.audio:
             id += f"**Audio ID**:\n`{reply.audio.file_id}`"
         elif reply.sticker:
             id += f"**Sticker ID**:\n`{reply.sticker.file_id}`"
         await message.reply(text=(id))

         
           
