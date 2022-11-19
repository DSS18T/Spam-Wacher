from pyrogram import filters
from pyrogram.types import *
from Nandha import Nandha


@Nandha.on_inline_query(filters.regex("^pfp"))
async def inline(_, query):
     user_id = query.from_user.id
     async for photo in Nandha.get_chat_photos(user_id):
         await Nandha.answer_inline_query(
         query.id,
         results = [
            InlineQueryResultPhoto(
               title = "Get Profile of Yours!",
               description = "Get Profile Photo",
               photo_file_id=photo.file_id)])
