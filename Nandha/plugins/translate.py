import config

from pyrogram import filters
from pyrogram.types import *

from Nandha import Nandha
from gpytranslate import Translator

trans = Translator()


@Nandha.on_message(filters.command(["tl", "tr"],config.CMDS))
async def translate(_, message) -> None:
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text("Reply to a message to translate it!\n With [translation codes](https://telegra.ph/Lang-Codes-03-19-3)")
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = await trans.detect(to_translate)
            dest = args
    except IndexError:
        source = await trans.detect(to_translate)
        dest = "en"
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    reply = (
        f"**Translated from {source} to {dest}**:\n"
        f"`{translation.text}`"
    )

    await message.reply_text(reply)


__MODULE__ = "Translate"

__HELP__ = """
**translate** is change something written or spoken from one language to another.

list of available code wards for translation: [language codes](https://telegra.ph/Lang-Codes-03-19-3)
"""
