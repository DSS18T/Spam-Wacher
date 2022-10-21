import config
import base64
from Nandha import Nandha
from pyrogram import filters



@Nandha.on_message(filters.command("encode",config.CMDS))
async def encodes(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      if reply:
            encodedBytes = base64.b64encode(data.encode("utf-8"))
            encoded = str(encodedBytes, "utf-8")
            await Nandha.send_message(chat_id, text=encoded, reply_to_message_id=message.id)
