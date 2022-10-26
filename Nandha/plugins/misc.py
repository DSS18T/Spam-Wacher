
import aiofiles
import os
import glob
import config
import requests

from Nandha import Nandha
from pyrogram import filters
from pyrogram.types import *
from datetime import datetime as time
from Nandha.help.paste import spacebin
from bing_image_downloader import downloader

is_downloading = False

@Nandha.on_message(filters.command("img",config.CMDS))
async def image(_, message):
    global is_downloading
    if len(message.text.split()) <2:
          return await message.reply("Provide A Query!`")
    elif is_downloading:
          return await message.reply("Another Process Downloading Our Server Please Wait!")
    is_downloading = True
    query = message.text.split(None, 1)[1]
    jit = f'"{query}"'
    msg = await message.reply("Downloading please wait!")
    downloader.download(
        jit,
        limit=6,
        output_dir="store",
    )
    os.chdir(f'./store/"{query}"')
    types = ("*.png", "*.jpeg", "*.jpg")  # the tuple of file types
    files_grabbed = []
    for files in types:
        files_grabbed.extend(glob.glob(files))
    await msg.edit("Uploading please wait!")
    try:
        await Nandha.send_media_group(message.chat.id,[
               InputMediaPhoto(f"{files_grabbed[0]}"),
               InputMediaPhoto(f"{files_grabbed[1]}"),
               InputMediaPhoto(f"{files_grabbed[2]}"),
               InputMediaPhoto(f"{files_grabbed[3]}"),
               InputMediaPhoto(f"{files_grabbed[4]}"),
               InputMediaPhoto(f"{files_grabbed[5]}")],reply_to_message_id=message.id) 
        await msg.delete()
        is_downloading = False
        return
    except Exception as e:
         await msg.edit(e)
         is_downloading = False
    os.chdir("/app")
    os.system("rm -rf store")


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
            query = reply.text.lower()
            if len(message.text.split()) == 0:
                 search = message.text.split()[0]
            else:
                 search = message.text.replace(" ", "%20")
            results = requests.get("https://api.urbandictionary.com/v0/define?term="+search).json()
            text = f'**⚠️ Warning: Urban Dictionary does not always provide accurate descriptions**:\n\n**• Result for**: `[{query}]`\n\n**• Result**:\n`{results["list"][0]["definition"]}`\n\n• **Example**:\n`{results["list"][0]["example"]}`'
            await Nandha.send_message(message.chat.id,text=text,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🧠 Google it",url="https://www.google.com/search?q=define%20"+search),]]),reply_to_message_id=message.id)
         except Exception as e:
              await message.reply(e)
      elif not reply and len(message.text.split()) >1:
            try:
              query = message.text.split(None,1)[1].lower()
              if len(message.text.split()) == 1:
                   search = message.text.split()[1]
              else:
                   search = message.text.replace(" ", "%20")
              results = requests.get("https://api.urbandictionary.com/v0/define?term="+search).json()
              text = f'**⚠️ Warning: Urban Dictionary does not always provide accurate descriptions**:\n\n**• Result for**: `[{query}]`\n\n**• Result**:\n`{results["list"][0]["definition"]}`\n\n• **Example**:\n`{results["list"][0]["example"]}`'
              await Nandha.send_message(message.chat.id,text=text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🧠 Google it",url="https://www.google.com/search?q=define%20"+search),]]),reply_to_message_id=message.id)
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
    await Nandha.send_message(chat_id,f"**Here Paste**:\n{link}",reply_to_message_id=message.id)
    
        
