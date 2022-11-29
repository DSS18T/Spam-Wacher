import time
import requests

import config
from pyrogram import filters
from pyrogram.types import *
from Nandha import Nandha, START_TIME
from Nandha.help.helper_func import get_readable_time





keywards = InlineKeyboardMarkup([[
InlineKeyboardButton("pfp", switch_inline_query_current_chat="pfp"),
InlineKeyboardButton("ping", switch_inline_query_current_chat="ping"),
InlineKeyboardButton("tm", switch_inline_query_current_chat="tm"),],[
InlineKeyboardButton("Anime Typo", callback_data="Anime typo"),]])



async def waifu_in():
    images = []
    for x in range(5):
       api = requests.get("https://api.waifu.pics/sfw/waifu").json()
       images.append(api["url"])
    answers = []
    for y in images:
      answers.append(InlineQueryResultPhoto(
           photo_url=y,
           thumb_url=y,
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
          InputTextMessageContent(PING_TEXT.format(ping_time, uptime)),
          thumb_url="https://graph.org/file/ae344e920d7fa4e5a2398.jpg",)]
      return answers
     

async def help_in():
      answers = [
         InlineQueryResultArticle("Help Menu!",
         InputTextMessageContent("Inline Commands!"),
         reply_markup=keywards,)]
      return answers

@Nandha.on_inline_query()
async def inline(_, query):
     string = query.query.casefold()
     user_id = query.from_user.id
     if string.strip() == "":
          answers = await help_in()
          return await query.answer(answers)
     elif string.split()[0] == "pfp":
          answers = await pfp_inline(user_id)
          return await query.answer(answers, cache_time=200)
     elif string.split()[0] == "ping":
          answers = await ping_inline()
          return await query.answer(answers)
     elif string.split()[0] == "waifu":
          answers = await waifu_in()
          await query.answer(answers, cache_time=6)
     else:
          return await query.answer(results=[InlineQueryResultArticle("Error Raises!",InputTextMessageContent("Invalid Inline Command! 🧐"))],switch_pm_parameter="Invalid Inline!")
