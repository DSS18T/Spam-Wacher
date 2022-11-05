import config
from Nandha import Nandha
from pyrogram import filters
from pyrogram.types import InputMediaPhoto


@Nandha.on_message(filters.command("pfp",config.CMDS))
async def user_profiles(_, message):
       user_id = message.from_user.id
       file = []
       async for photo in Nandha.get_chat_photos(user_id):
              file.append(photo.file_id)
       for x in file:
          if x == x:
              continue
          await Nandha.send_media_group(message.chat.id,[
                 InputMediaPhoto(pfp),
                 InputMediaPhoto(pfp)])
