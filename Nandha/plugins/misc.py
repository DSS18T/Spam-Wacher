
import aiofiles
import os
import asyncio
import glob
import config
import time
import requests
import pyqrcode, png
from telegraph import upload_file
from Nandha import Nandha , START_TIME
from pyrogram import filters
from pyrogram.types import *
from datetime import datetime
from Nandha.help.paste import spacebin, batbin
from Nandha.help.helper_func import get_readable_time



is_downloading = False



@Nandha.on_message(filters.command("qr",config.CMDS))
async def qr_png(_, message):
      reply = message.reply_to_message
      if reply and reply.text: text = reply.text
      elif reply or not reply and len(message.text.split()) >1: text = message.text.split(None,1)[1]
      else: return await message.reply_text("wrong formatting!")
      m = await message.reply_text("`Processing...`")
      qr_code = pyqrcode.create(text)
      qr_code.png("qr_code.png", scale=5)
      await Nandha.send_photo(chat_id=message.chat.id, photo="qr_code.png", reply_to_message_id=message.id)
      os.remove("qr_code.png")
      return await m.delete()
       

@Nandha.on_message(filters.command("echo",config.CMDS))
async def echo(_, message):
     reply = message.reply_to_message
     chat_id = message.chat.id
     if len(message.text.split()) >1 and reply: return await reply.reply_text(message.text.split(None,1)[1])
     elif reply: return await reply.copy(chat_id, reply_to_message_id=reply.id)
     elif not reply and len(message.text.split()) >1: return await message.reply_text(message.text.split(None,1)[1])
     else: return await message.reply_text("What should I be echo?")



@Nandha.on_message(filters.regex("google"))
@Nandha.on_message(filters.command("gt",config.CMDS))
async def google_it(_, message):
       file_id = "CAACAgUAAx0CXss_8QABB0iVY2ZDrB4YHzW6u1xRqKLuUX7b6sEAAhUAA-VDzTc4Ts7oOpk4nx4E"
       if message.reply_to_message:
            await message.reply_to_message.reply_sticker(sticker=file_id,
           reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔎 Google",url="https://www.google.com/search?")]]))
       else: await message.reply_sticker(sticker=file_id,
           reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔎 Google",url="https://www.google.com/search?")]]))

@Nandha.on_message(filters.command("tm",config.CMDS))
async def telegraph(_, message):
   reply = message.reply_to_message
   if not reply or reply and not reply.media:
          return await message.reply("Reply A Media Upload File Graph.org")
   else:
      telegraph = upload_file(await message.reply_to_message.download())
      for file_id in telegraph:
          url = "https://graph.org" + file_id
      await message.reply(url)



@Nandha.on_message(filters.command("ping",config.CMDS))
async def ping(_, message):
      start = datetime.now()
      end = datetime.now()
      ping = (end - start).microseconds / 1000
      uptime = get_readable_time((time.time() - START_TIME))
      await message.reply_text(
          f"**PING**: `{ping}` ms\n"
          f"**UPTime**: `{uptime}`")


@Nandha.on_message(filters.command("ud",config.CMDS))
async def ud(_, message):
      reply = message.reply_to_message
      if len(message.text.split()) <2:
            return
      query = message.text.split(None,1)[1].lower()
      search = (
                 message.text.split()[1]
                 if len(message.text.split()) <3
                 else message.text.split(None,1)[1].replace(" ","%20")
              )
      try:
           results = requests.get("https://api.urbandictionary.com/v0/define?term="+search).json()
           text = f'**⚠️ Warning: Urban Dictionary does not always provide accurate descriptions**:\n\n**• Result for**: `[{query}]`\n\n**• Result**:\n`{results["list"][0]["definition"]}`\n\n• **Example**:\n`{results["list"][0]["example"]}`'
           if reply and len(message.text.split()) >1:
                 await Nandha.send_message(message.chat.id,text=text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🧠 Google it",url="https://www.google.com/search?q=define%20{}".format(search)),]]),reply_to_message_id=reply.id)
           elif not reply and len(message.text.split()) >1:
                 await Nandha.send_message(message.chat.id,text=text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🧠 Google it",url="https://www.google.com/search?q=define%20{}".format(search)),]]),reply_to_message_id=message.id)
      except Exception as e:
            return await message.reply(f"No Results in > `{query}` <")


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
    link0 = await spacebin(text)
    link1 = await batbin(text)
    await Nandha.send_photo(chat_id,photo=link1,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("BatBin",url=link1), InlineKeyboardButton("SpaceBin",url=link0)]]),reply_to_message_id=message.id)
    
        
__MODULE__ = "Misc"

__HELP__ = """
- `/paste`: paste a text or text document.
- `/ud`: definition the ward
- `/ping`: see ping server.
- `/tm`: upload a image to telegraph.
- `/gt`: google it reply.
- `/echo`: 
( reply to message to reply that message to reply user) 
( reply to user with /echo hi to send message via bot )
- `/qr`: make qr image reply to message
"""


dice_images = [
"https://graph.org/file/0e639cb966ca35317c622.jpg",
"https://graph.org/file/a929afa493ec934bf2f22.jpg",
"https://graph.org/file/f9d32958769878b8ff297.jpg",
"https://graph.org/file/fe302a1d5f4cf09d34b0f.jpg",
"https://graph.org/file/86fc5303dc9493723a39f.jpg",
"https://graph.org/file/dafe4ce12056b277bc63b.jpg",
]


@Nandha.on_message(filters.command("dice"))
async def dice(_, m):
     x = await message.reply("Read for the Dice?")
     await asyncio.sleep(2)
     await x.edit("Let's big in.")
     image = random.choice(dice_images)
     await Nandha.edit_message_media(
          chat_id=m.chat.id,
          message_id=x.id,
          media=InputMediaPhoto(image),)
     await asyncio.sleep(2)
     await Nandha.edit_message_media(
          chat_id=m.chat.id,
          message_id=x.id,
          media=InputMediaPhoto(image),)
     await asyncio.sleep(2)
     await Nandha.edit_message_media(
          chat_id=m.chat.id,
          message_id=x.id,
          media=InputMediaPhoto(image, caption="okay dice completed.\nnow see your dice on photo!"), )
    
    
     
     

