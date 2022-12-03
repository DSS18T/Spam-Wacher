import time
import requests

import config
from pyrogram import filters
from pyrogram.types import *
from Nandha import Nandha, START_TIME
from Nandha.help.helper_func import get_readable_time


keywards = InlineKeyboardMarkup([[
InlineKeyboardButton("Pfp", switch_inline_query_current_chat="pfp"),
InlineKeyboardButton("Ping", switch_inline_query_current_chat="ping"),
InlineKeyboardButton("Dog Fact", switch_inline_query_current_chat="dogfact"),
],[
InlineKeyboardButton("Anime Typo ➡️", callback_data="AnimeTypo"),]])

anime_kyb = InlineKeyboardMarkup([[
InlineKeyboardButton("Waifu", switch_inline_query_current_chat="waifu"),
InlineKeyboardButton("Neko", switch_inline_query_current_chat="neko"),
InlineKeyboardButton("Husbando", switch_inline_query_current_chat="hbd"),],[
InlineKeyboardButton("back ⬅️", callback_data="inline_kyb"),]])


@Nandha.on_callback_query(filters.regex("AnimeTypo"))
async def AnimeTypo(_, query):
      await Nandha.edit_inline_text(inline_message_id=query.inline_message_id, 
           text="Anime Typo Commands!", reply_markup=anime_kyb)
 
@Nandha.on_callback_query(filters.regex("inline_kyb"))
async def Inline_help(_, query):
      await Nandha.edit_inline_text(inline_message_id=query.inline_message_id, 
           text="Inline Commands!", reply_markup=keywards)     

async def dog_fact():
    answers = []
    for x in range(5):
       api = requests.get("https://some-random-api.ml/animal/cat").json()
       url = api["image"]
       fact = api["fact"]
       answers.append(
             InlineQueryResultPhoto(
             photo_url=url,
             thumb_url=url,
             caption=fact))
    return answers
       

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

async def neko_in():
    images = []
    for x in range(5):
       api = requests.get("https://api.waifu.pics/sfw/neko").json()
       images.append(api["url"])
    answers = []
    for y in images:
      answers.append(InlineQueryResultPhoto(
           photo_url=y,
           thumb_url=y,
           caption="Made by @NandhaBots"))
    return answers

async def husbando_in():
    images = []
    for x in range(5):
       api = requests.get("https://nekos.best/api/v2/husbando").json()
       images.append(api["results"][0]["url"])
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
     Mquery = query.query
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
     elif string.split()[0] == "neko":
          answers = await neko_in()
          await query.answer(answers, cache_time=6)
     elif string.split()[0] == "dogfact":
          answers = await dog_fact()
          await query.answer(answers, cache_time=6)
     elif string.split()[0] == "hbd":
          answers = await husbando_in()
          await query.answer(answers, cache_time=6)
     else:
          return await query.answer(results=[InlineQueryResultArticle("Not Found!",InputTextMessageContent(f"Anything Found > {string} <"))],switch_pm_parameter="Invalid Method!")
