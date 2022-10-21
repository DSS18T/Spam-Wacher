import config
import base64
from Nandha import Nandha
from pyrogram import filters



@Nandha.on_message(filters.command(["decode","encode"],config.CMDS))
async def encodes(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id

      if reply and not reply.text:
          return await message.reply("`reply to message text!`")
      elif reply and reply.text:
           data = reply.text
      elif not reply and len(message.text.split()) <2:
             return await message.reply("`reply to text or give me some text to (en/de) code!`")
      elif not reply and len(message.text.split()) >1:
            data = message.text.split(None,1)[1]
      if message.text.split()[0].startswith("/en"):
           encodedBytes = base64.b64encode(data.encode("utf-8"))
           encode = str(encodedBytes, "utf-8")
           await Nandha.send_message(chat_id, text=encode, reply_to_message_id=message.id)
      elif message.text.split()[0].startswith("/de"):
          decode = base64.b64decode(data).decode("utf-8", "ignore")
          await Nandha.send_message(chat_id, text=decode, reply_to_message_id=message.id)

