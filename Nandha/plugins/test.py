import numpy as np 
import cv2
from cv2 import dnn

from Nandha import Nandha
from pyrogram import filters


@Nandha.on_message(filters.command("color"))
async def color(_, m):
      reply = m.reply_to_message
      if not reply or reply and not reply.media: return await m.reply("Reply to Media!")
      img_path = await Nandha.download_media(reply)
      img = cv2.imread(img_path)
      scaled = img.astype("float32") / 255.0
      lab_img = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)
      await m.reply(lab_img)


