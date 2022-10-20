import config
from Nandha import Nandha
from pyrogram import filters

import base64

@Nandha.on_message(filters.command(["encode,decode],config.CMDS))
async def encodes(_, message):
      if not message.reply_to_message or not message.reply_to_message.text:
         return await message.reply("`reply to a message text to encode/decode!`")
      date = message.reply_to_message.text
      try:
          if startswith("en"):
              encodedBytes = base64.b64encode(data.encode("utf-8"))
              encodedStr = str(encodedBytes, "utf-8")
              await message.reply(encodedStr)
          elif ends with("de"):
              decodedBytes = base64.b64decode(str(data))
              decodedStr = str(decodedBytes, "utf-8")
              await message.reply(decodedStr)
      except Exception as e:
         await message.reply(e)
