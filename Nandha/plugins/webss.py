import requests

import config

from Nandha import Nandha
from pyrogram import filters


async def cssworker_url(target_url: str):
    url = "https://htmlcsstoimage.com/demo_run"
    my_headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
    }

    data = {
        "url": target_url,
        # Sending a random CSS to make the API to generate a new screenshot.
        "css": f"random-tag: {uuid.uuid4()}",
        "render_when_ready": False,
        "viewport_width": 1280,
        "viewport_height": 720,
        "device_scale": 1,
    }

    try:
        resp = await requests.post(url, headers=my_headers, json=data)
        return resp.json()
    except:
        return None



@Nandha.on_message(filters.command("webss",config.CMDS))
async def take_short(_, message):
      url = message.text.split(None,1)[1]
      res_json = await cssworker_url(url)
      if res_json:
            image_url = res_json["url"]
            await message.reply_photo(image_url)
      else: return await message.reply("`can't find anything!`")


