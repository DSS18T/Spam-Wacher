
import aiofiles
import os
import config

from Nandha import Nandha
from pyrogram import filters
from datetime import datetime as time
from Nandha.help.paste import spacebin

@Nandha.on_message(filters.command("ping",config.CMDS))
async def ping(_, message):
      start = time.now()
      end = time.now()
      ping = (end - start).microseconds / 1000
      await message.reply(f"**PING**: `{ping}` ms")

@Nandha.on_message(filters.command("paste",config.CMDS))
async def paste(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    if reply and reply.text or reply.caption:
         text = reply.text or reply.caption
    elif reply and reply.document:
          doc = await reply.download()
          async with aiofiles.open(doc, mode="r") as f:
               text = await f.read()
          os.remove(doc)
    elif not reply and len(message.text.split()) <2:
         return await message.reply("`please reply to (text/file) or give text to paste!`")
    elif not reply and len(message.text.split()) >1:
         text = message.text.split(None, 1)[1]
    link = await spacebin(text)
    await Nandha.send_message(chat_id,f"here paste:\n`{link}`",reply_to_message_id=message.id)
    
        
