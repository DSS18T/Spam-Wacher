import config
from pyrogram import filters
from pyrogram.types import *
from Nandha import Nandha


keywards = [
"ping",
"pfp",
"img",
]


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
     buttons = []
     for x in keywards:
        buttons.append([InlineKeyboardButton(x, switch_inline_query_current_chat=x)])
     answers.append(InlineQueryResultArticle(
         "Help Inline!",
         InputTextMessageContent("inline commands!"),reply_markup=InlineKeyboardMarkup(buttons)))
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
          return await query.answer(switch_pm_parameter="Invalid Inline!")
