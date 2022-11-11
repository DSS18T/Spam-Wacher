import config
import asyncio
from Nandha import Nandha
from pyrogram import filters
from pyrogram.types import InputMediaPhoto

@Nandha.on_message(filters.command("pfp",config.CMDS))
async def user_profiles(_, message):
       user_id = message.from_user.id
       reply = message.reply_to_message
       try:
          if reply: uid = reply.from_user.id
          elif not reply: uid = user_id
          x = 0
          loli = []
          async for photo in Nandha.get_chat_photos(uid):
               x += +1
               loli.append(InputMediaPhoto(media=photo.file_id))
          await Nandha.send_media_group(message.chat.id, media=loli, reply_to_message_id=message.id)
       except Exception as e:
          return await message.reply(e)
