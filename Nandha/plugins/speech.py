import os
import wget
import requests
import config

from pyrogram import filters
from Nandha import Nandha

api_key = "abe3d449e4024b978438f0a0b10f1859"
api_url = "http://api.voicerss.org/"

@Nandha.on_message(filters.command("tts",config.CMDS))
async def text_to_speech(_, message):
     reply = message.reply_to_message
     if reply:
         audio = reply.text
         lang_code = message.text.split()[1]
     elif not reply and len(message.command) >1:
          audio = message.text.split(":")[1]
          lang_code = message.text.split()[1].replace(":","")
     else: return await message.reply("`Wrong Method!`")
     msg = await message.reply("processing...")
     try:
         response = requests.get(api_url + "?key=" + api_key + f"&hl={lang_code}&c=MP3&src=" + audio)
         with open(f"{audio}.mp3", "wb") as audio_file:
              audio_file.write(response.content)
         thumb = wget.download("https://c.top4top.io/s_24730ldbx1.jpg")
         await message.reply_audio(
             f"{audio}.mp3",
             title=audio,
             caption=audio,
             thumb=thumb,
              )
         await msg.delete()
         os.remove(f"{audio}.mp3")
         os.remove(thumb)
     except Exception as e:
       await msg.edit(e)

__MODULE__ = "Tts"

__HELP__ = """

**Text to speech**:

following languages:
ar-eg Arabic (Egypt)
ar-sa Arabic (Saudi Arabia)
bg-bg  Bulgarian
ca-es Catalan
zh-cn Chinese (Hong Kong)
zh-tw Chinese (Taiwan)
hr-hr Croatian
cs-cz Czech
da-dk Danish
nl-be Dutch (Belgium)
nl-nl Dutch (Netherlands)
en-au English (Australia)
en-ca English (Canada)
en-gb English (Great Britain)
en-in English (India)
en-ie English (Ireland)
en-us English (United States)
fi-fi Finnish
hi-in hu-hu
id-id Indonesian
ja-jp Japanese
ko-kr Korean
ru-ru Russian
es-mx Spanish (Mexico)
ta-in Tamil
tr-tr Turkish
vi-vn Vietnamese
ro-ro Romanian
pt-pt Portuguese (Portugal)
"""
