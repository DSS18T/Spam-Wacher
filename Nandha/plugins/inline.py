from pyrogram import filters
from pyrogram.types import *
from Nandha import Nandha

async def pfp_inline(user_id; int):
     answers = []
     async for photo in Nandha.get_chat_photos(user_id):
        answers.append(
            InlineQueryResultCachedPhoto(
                caption="Made by @NandhaBots",
                photo_file_id=photo.file_id
            )
           )
     return answers


@Nandha.on_inline_query()
async def inline(_, query):
     string = query.query.casefold()
     user_id = query.from_user.id
     if string.split()[0] == "pfp":
          answers = await pfp_inline(user_id)
          return await query.answer(answers, cache_time=30)
     
