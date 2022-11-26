import requests
import config
import random
from Nandha import Nandha, UB
from pyrogram import filters
from pyrogram import enums



@Nandha.on_message(filters.private & filters.command("boobs",config.CMDS))
async def boobs(_, message):
    file_id = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    url = "http://media.oboobs.ru/{}"
    await message.reply_photo(url.format(file_id),protect_content=True)



@Nandha.on_message(filters.private & filters.command("porn",config.CMDS))
async def porn(_, message):
      porn_channel_id = "@pornlab_hd"
      chat_id = message.chat.id
      porn_video_ids = []
      async for message in UB.search_messages(porn_channel_id, filter=enums.MessagesFilter.VIDEO, limit=100):
            porn_video_ids.append(message.id)
      random_porn_video = random.choice(porn_video_ids)
      await Nandha.copy_message(
         chat_id=chat_id,
         reply_to_message_id=message.id,
         protect_content=True,
         from_chat_id=porn_channel_id,
         message_id=random_porn_video,
         caption="",)
     
