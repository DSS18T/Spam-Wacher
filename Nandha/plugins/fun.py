import requests
from Nandha import Nandha
from pyrogram import filters



@Nandha.on_message(filters.regex("baka"))
async def baka(_, message):
       reply = message.reply_to_message
       api = requests.get("https://nekos.best/api/v2/baka").json()
       url = api["results"][0]['url']
       anime = api["results"][0]["anime_name"]
       name = message.from_user.first_name
       if reply:
            await reply.reply_animation(url,caption="**• {}**\n**Baka! {}**".format(anime, name))
       else:
           await message.reply_animation(url,caption="**• {}**\n**Baka! {}**".format(anime, name))
