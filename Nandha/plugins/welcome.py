import math

from PIL import Image, ImageDraw, ImageFont

from pyrogram import filters
from pyrogram.types import *
from Nandha import Nandha


@Nandha.on_message(filters.new_chat_members)
async def new_member(_, m):
    welcome = Image.open("Nandha/help/utils/download.gif")
    nandha = [welcome.copy()]

    try:
        while 1:
            welcome.seek(welcome.tell() + 4)
            owo = welcome.copy()
            nandha.append(owo)

    except EOFError:
        pass

    nandha[0] = nandha[0]

    text = [f"{m.from_user.first_name} Welcome your are!"]

    s1 = nandha[0].size[0] // 2
    s2 = 250
    font = ImageFont.truetype("Nandha/help/utils/SuisseIntl-Regular.ttf", 20)
    s3 = math.ceil(len(nandha) / len(text))

    for i in range(len(nandha)):
        draw = ImageDraw.Draw(nandha[i])
        s4 = (s1 - len(text[i // s3]) * 5, s2)
        draw.text(s4, text[i // s3], font=font, anchor=None)

    nandha[0].save(
        "welcome.gif",
        save_all=True,
        append_images=nandha[1:],
        optimize=False,
        duration=150,
        loop=0,
    )
    await m.reply_animation(animation="welcome.gif")
