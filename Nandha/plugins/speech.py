import os
import wget
import requests
import config
import traceback
from asyncio import get_running_loop
from io import BytesIO
from Nandha import Nandha
from gpytranslate import Translator
from gtts import gTTS


def convert(text):
    audio = BytesIO()
    i = Translator().translate(text, dest="en")
    lang = i.src
    tts = gTTS(text, lang=lang)
    audio.name = lang + ".mp3"
    tts.write_to_fp(audio)
    return audio



@Nandha.on_message(filters.me & filters.command(["tts"], config.CMDS))
async def text_to_speech(_, message):
    if not message.reply_to_message:
        return await message.reply_text("REPLY TO SOME TEXT !")
    if not message.reply_to_message.text:
        return await message.reply_text("REPLY TO SOME TEXT !")
    m = await message.reply_text("🔁 PROCESSING...")
    text = message.reply_to_message.text
    try:
        loop = get_running_loop()
        audio = await loop.run_in_executor(None, convert, text)
        await message.reply_audio(audio)
        await m.delete()
        audio.close()
    except Exception as e:
        await m.edit(str(e))
        es = traceback.format_exc()
        print(es)
