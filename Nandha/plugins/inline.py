import config
from pyrogram import filters
from pyrogram.types import *
from Nandha import Nandha


HELP_INLINE_TEXT = f"""
**Inline for in @{config.USERNAME} .**:

**how to use ?**
  here the example:
     `@{config.USERNAME} pfp`
**copy this and paste your messaging pad**

**Commands**:

- `pfp`: get your all profile pictures.

**all coming sooon.....**
"""
async def pfp_inline(user_id: int):
     answers = []
     async for photo in Nandha.get_chat_photos(user_id):
        answers.append(
            InlineQueryResultCachedPhoto(
                caption="Made by @NandhaBots",
                photo_file_id=photo.file_id
            )
           )
     return answers

async def help_inline():
     answers = []
     answers.append(InlineQueryResultArticle(
         "Help Inline!",
         InputTextMessageContent(HELP_INLINE_TEXT)))
     return answers 


@Nandha.on_inline_query()
async def inline(_, query):
     string = query.query.casefold()
     user_id = query.from_user.id
     if string.strip() == "":
          answers = await help_inline()
          return await query.answer(answers)
     elif string.split()[0] == "pfp":
          answers = await pfp_inline(user_id)
          return await query.answer(answers, cache_time=30)
     else:
          answers = await help_inline()
          return await query.answer(answers)
