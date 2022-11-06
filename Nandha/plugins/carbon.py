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
    try:
       reply = message.reply_to_message
       if not reply or reply and not reply.media: return await message.reply("Reply to media")
       elif reply.media:
             msg = await message.reply("downloading...")
             photo = await reply.download()
             await msg.edit("Processing Image.")
             image_file = cv2.imread(photo)
             grayImage = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)
             cv2.imwrite(edit_img_loc, grayImage)
             await message.reply_photo(photo=f"edit_img_loc", quote=True)
             await msg.delete()
    except Exception as e: return await message.reply(e)
