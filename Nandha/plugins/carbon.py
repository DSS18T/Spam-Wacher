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
      if reply and reply.text or reply.caption:
           msg = await message.reply("`please wait making a carbon!`")
           carbon = await make_carbon(reply.text or reply.caption)
      elif not reply and len(message.text.split()) >1:
           msg = await message.reply("`please wait making a carbon!`")
           carbon = await make_carbon(message.text.split(None,1)[1])
      else: return await message.reply("`Reply to text or give a text to make carbon!`")
      await message.reply_photo(carbon)
      await msg.delete()
