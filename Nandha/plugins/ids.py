import config

from pyrogram import filters
from Nandha import Nandha


@Nandha.on_message(filters.command("id",config.CMDS))
async def ids(_, message):
      reply = message.reply_to_message
      if reply:
         forward = "`here the file ids`:\n\n"
         if message.forward_from == None:
             return await message.reply(f"**{forward_sender_name}** `hid his account information in Telegram's privacy settings, so I can't tell you anything about him.`")
         else:
            forward += f"**Forward From ID**:\n`{message.forward_from}`\n"
            forward += f"**Replied ID**: `{reply.from_user.id}`"
            forward += f"**Your ID**: `{message.from_user.id}`\n"
            forward += f"**Chat ID**: `{message.chat.id}`\n"
            await message.reply(text=(forward))
            
             
