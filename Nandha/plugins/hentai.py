import requests
import config
from Nandha import Nandha
from pyrogram import filters


@Nandha.on_message(filters.command("boobs",config.CMDS))
async def boobs(_, message):
    file_id = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    url = "http://media.oboobs.ru/{}"
    await message.reply_photo(url.format(file_id))
