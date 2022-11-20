import time
import requests

import config
from pyrogram import filters
from pyrogram.types import *
from Nandha import Nandha, START_TIME
from Nandha.help.helper_func import get_readable_time



keywards = [
"ping",
"pfp",
"img",
]


async def img_inline(search: str):
    API = "https://apibu.herokuapp.com/api/y-images?query={}".format(search)
    result = requests.get(API).json()["result"][:30]
    answers = []
    for url in result:      
        answers.append(
        InlineQueryResultDocument(
           title = f"Result for {search}",
           document_url=url,
           thumb_url=url,
           caption="Made by @NandhaBots"))
    return answers
    
      

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


PING_TEXT = """
**Pong!** `{}`
**Uptime!** `{}`
"""

async def ping_inline():
      start = time.time()
      end = time.time()
      ping_time = round((end - start) * 1000, 3)
      uptime = get_readable_time((time.time() - START_TIME))
      answers = [
          InlineQueryResultArticle("Server Ping!",
          InputTextMessageContent(PING_TEXT.format(ping_time, uptime)))]
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
          return await query.answer(answers, cache_time=200)
     elif string.split()[0] == "ping":
          answers = await ping_inline()
          return await query.answer(answers)
     elif string.split()[0] == "img":
          search = string.split(string.split()[0])[1]
          answers = await img_inline(search)
          await query.answer(answers, cache_time=200)
          return os.system("rm -rf wall_images")
     else:
          return await query.answer(results=[InlineQueryResultArticle("Error Raises!",InputTextMessageContent("Invalid Inline Command! 🧐"))],switch_pm_parameter="Invalid Inline!")
