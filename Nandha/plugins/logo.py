
import io
import os
import config
import random
import requests
from Nandha import Nandha, UB
from pyrogram import filters

from PIL import Image, ImageDraw, ImageFont


LOGO_LINKS = [
"https://graph.org/file/cceab4f58cc41817eb86a.jpg",
"https://graph.org/file/89951db9c7263288928ae.jpg",
"https://graph.org/file/fccc52cb374de86634edf.jpg",
"https://graph.org/file/ebf352d1346ce426fe505.jpg",
]


@UB.on_message(filters.me & filters.command("logo",config.CMDS))
@Nandha.on_message(filters.command("logo",config.CMDS))
async def logo(_, message):
     chat = message.chat
     user = message.from_user
     reply = message.reply_to_message
     if len(message.text.split()) <2: return await message.reply("`Gimme Any logo Name!`")
     msg = await message.reply("`logo Processing...`")
     text = message.text.split(None,1)[1]
     if "graph.org" in message.text:
         link = message.text.split("//")[1]
         img = Image.open(io.BytesIO(requests.get(link).content))
     elif reply:
         path = await reply.download()
         img = Image.open(path)
     else:
         randc = random.choice(LOGO_LINKS)
         img = Image.open(io.BytesIO(requests.get(randc).content))
     draw = ImageDraw.Draw(img)
     image_widthz, image_heightz = img.size
     pointsize = 500
     fillcolor = "black"
     shadowcolor = "blue"
     font = ImageFont.truetype("images/logofont.otf", 140)
     w, h = draw.textsize(text, font=font)
     h += int(h*0.21)
     image_width, image_height = img.size
     draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
     x = (image_widthz-w)/2
     y = ((image_heightz-h)/2+6)
     draw.text((x, y), text, font=font, fill="white", stroke_width=1, stroke_fill="black")
     fname = "logo.png"
     img.save(fname, "png")
     await msg.edit("`logo done!`")
     return await message.reply_document(fname, caption=f"**Req by {user.mention}**")
     os.remove(fname)
     await msg.delete()
