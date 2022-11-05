import config
from Nandha import Nandha
from pyrogram import filters
from pyrogram.types import InputMediaPhoto


@Nandha.on_message(filters.command("pfp",config.CMDS))
async def user_profiles(_, message):
       user_id = message.from_user.id
       x = await Nandha.get_chat_photos_count(user_id)
       async for photo in Nandha.get_chat_photos(user_id):
              file = photo.file_id
       await Nandha.send_media_group(message.chat.id,[
            InputMediaPhoto(file_id)
            InputMediaPhoto(file_id)
        ])
