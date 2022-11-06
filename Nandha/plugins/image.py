import os
import cv2
import config
from Nandha import (
Nandha, session )
from io import BytesIO
from pyrogram import filters 


async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with session.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

async def make_bw(path):
   image_file = cv2.imread(path)
   grayImage = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)
   cv2.imwrite("brightness.jpg", grayImage)
   return "brightness.jpg"
   

@Nandha.on_message(filters.command(["cb","carbon"],config.CMDS))
async def make_carbon_image(_, message):
      reply = message.reply_to_message
      if reply and reply.text or reply and reply.caption:
           text = reply.text or reply.caption
      elif not reply and len(message.text.split()) >1:
           text = message.text.split(None,1)[1]
      else: return await message.reply("`Reply to text or give a text to make carbon!`")
      msg = await message.reply("`Please Wait!`")
      carbon = await make_carbon(text)
      await message.reply_photo(carbon)
      await msg.delete()


@Nandha.on_message(filters.command("bw",config.CMDS))
async def black_white(_, message):
    reply = message.reply_to_message
    try:
       if not reply or reply and not reply.media: return await message.reply("Reply to media")
       elif reply.media:
             msg = await message.reply("downloading...")
             path = await Nandha.download_media(reply)
             await msg.edit("scanning image.....")
             image = await make_bw(path)
             await msg.edit("uploading....")
             await message.reply_photo(photo=image, quote=True)
             await msg.delete()
             os.remove("brightness.jpg")
    except Exception as e: return await message.reply(e)
    os.remove("brightness.jpg")

@Nandha.on_message(filters.command("sticker"))
async def sticker(_, message):
    reply = message.reply_to_message
    try:
       if not reply or reply and not reply.media: return await message.reply("Reply to Media!")
       elif reply.media:
            path = await Nandha.download_media(reply)
            sticker = "image" + "/" + "sticker.webp"
            os.rename(path, sticker)
            await message.reply_sticker(sticker=sticker)
            os.remove(sticker)
    except Exception as e: return await message.reply(e)
            



