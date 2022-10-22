
import aiofiles
import os
import config
import requests

from Nandha import Nandha
from pyrogram import filters
from pyrogram.types import *
from datetime import datetime as time
from Nandha.help.paste import spacebin

@Nandha.on_message(filters.command("ping",config.CMDS))
async def ping(_, message):
      start = time.now()
      end = time.now()
      ping = (end - start).microseconds / 1000
      await message.reply(f"**PING**: `{ping}` ms")


@Nandha.on_message(filters.command("ud",config.CMDS))
async def ud(_, message):
      reply = message.reply_to_message
      if reply and reply.text:
         try:
            search = reply.text
            results = requests.get("https://api.urbandictionary.com/v0/define?term="+search).json()
            text = f'**⚠️ Warning: Urban Dictionary does not always provide accurate descriptions**:\n\n**• Result for**: `[{search}]`\n\n**• Result**:\n`{results["list"][0]["definition"]}`\n\n• **Example**:\n`{results["list"][0]["example"]}`'
            await Nandha.send_message(message.chat.id,text=text,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🧠 Google it",url="https://www.google.com/search?q=define"+search),]]),reply_to_message_id=message.id)
         except Exception as e:
              await message.reply(e)
      elif not reply and len(message.text.split()) >1:
            try:
              search = message.text.split(None,1)[1]
              results = requests.get("https://api.urbandictionary.com/v0/define?term="+search).json()
              text = f'**⚠️ Warning: Urban Dictionary does not always provide accurate descriptions**:\n\n**• Result for**: `[{search}]`\n\n**• Result**:\n`{results["list"][0]["definition"]}`\n\n• **Example**:\n`{results["list"][0]["example"]}`'
              await Nandha.send_message(message.chat.id,text=text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🧠 Google it",url="https://www.google.com/search?q=define"+search),]]),reply_to_message_id=message.id)
            except Exception as e:
                   await message.reply(e)  

@Nandha.on_message(filters.command("paste",config.CMDS))
async def paste(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    if reply and reply.text:
         text = reply.text 
    elif reply and reply.caption:
          text = reply.caption
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
    
        
