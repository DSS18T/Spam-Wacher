import time
import requests

import config
from pyrogram import filters
from pyrogram.types import *
from Nandha import Nandha, START_TIME
from Nandha.help.helper_func import get_readable_time
from Nandha.help.encodes import encode, decode
from Nandha.help.paste import batbin


keywards = InlineKeyboardMarkup([[
InlineKeyboardButton("Encode", switch_inline_query_current_chat="encode"),
InlineKeyboardButton("Decode", switch_inline_query_current_chat="decode"),
],[
InlineKeyboardButton("Pfp", switch_inline_query_current_chat="pfp"),
InlineKeyboardButton("Ping", switch_inline_query_current_chat="ping"),
InlineKeyboardButton("Paste", switch_inline_query_current_chat="paste"),
],[
InlineKeyboardButton("Dog Fact", switch_inline_query_current_chat="dogfact"),
InlineKeyboardButton("Cat Fact", switch_inline_query_current_chat="catfact"),
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
       api = requests.get("https://some-random-api.ml/animal/dog").json()
       url = api["image"]
       fact = api["fact"]
       answers.append(
             InlineQueryResultPhoto(
             photo_url=url,
             thumb_url=url,
             caption=fact))
    return answers

async def cat_fact():
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
       

async def encode_string(text: str):
      encode_string = encode(text)
      answers = [ InlineQueryResultArticle("Encode String!",
         InputTextMessageContent(encode_string), 
         thumb_url="https://graph.org/file/97a4fcab86a0efc84a491.jpg",)]
      return answers

async def decode_string(text: str):
      decode_string = decode(text)
      answers = [ InlineQueryResultArticle("Decode String!",
         InputTextMessageContent(decode_string),
         thumb_url="https://graph.org/file/97a4fcab86a0efc84a491.jpg",)]
      return answers

async def paste(text):
      paste = await batbin(text)
      answers = [

 InlineQueryResultPhoto(
         photo_url=paste,
         thumb_url=paste), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Paste link", url=paste)]])
]
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
         thumb_url="https://graph.org/file/f6278ec869dbb1eebfe0e.jpg",
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
     elif string.split()[0] == "catfact":
          answers = await cat_fact()
          await query.answer(answers, cache_time=6)
     elif string.split()[0] == "hbd":
          answers = await husbando_in()
          await query.answer(answers, cache_time=6)
     elif string.split()[0] == "encode":
          answers = await encode_string(string.split(string.split()[0])[1])
          await query.answer(answers, cache_time=2, switch_pm_parameter="Input Me string.")
     elif string.split()[0] == "decode":
          answers = await decode_string(string.split(string.split()[0])[1])
          await query.answer(answers, cache_time=2, switch_pm_parameter="Input Me string.")
     elif string.split()[0] == "paste":
            answers = await paste(string.split(string.split()[0])[1])
            await query.answer(answers, cache_time=2)
     else:
          return await query.answer(results=[InlineQueryResultArticle("Not Found!",InputTextMessageContent(f"Anything Found > {string} <"))],switch_pm_parameter="Invalid Method!")
