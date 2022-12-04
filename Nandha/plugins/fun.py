import config
import asyncio
import re
import random
import requests
from Nandha import Nandha
from pyrogram import filters

from telegraph import upload_file

async def graph(media):
     telegraph = upload_file(media)
     for file_id in telegraph:
          url = "https://graph.org" + file_id
     return url


@Nandha.on_message(filters.command("ytc",config.CMDS))
async def youtube_comment(_, message):
       if message.reply_to_message and message.reply_to_message.media:
           try:
              username_txt = message.text.split("-u")[1].split("-c")[0]
              comment_txt = message.text.split("-c")[1]
           except: 
               return await message.reply_text("Format: /ytc -u Nandha -c hello world")
           x = await message.reply_text("downloading media!")
           media = await Nandha.download_media(message.from_user.photo.big_file_id)
           await x.edit("complete download!")
           await x.edit("Uploading graph!")
           url = await graph(media)
           await x.edit("done graph upload!")
       else:
          try:
              username_txt = message.from_user.username
              comment_txt = message.text.split(None,1)[1]
          except: 
              return await message.reply_text("Format: /ytc hello world")
          x = await message.reply_text("downloading media!")
          media = await Nandha.download_media(message.from_user.photo.big_file_id)
          await x.edit("complete download!")
          await x.edit("Uploading graph!")
          url = await graph(media)
          await x.edit("done graph upload!") 
       if len(username_txt.split()) > 1:
              username = username_txt.replace(" ", "%20")
       else: username = username_txt
       if len(comment_txt.split()) > 1:
              comment = comment_txt.replace(" ", "%20")
       else: comment = comment_txt   
       p_url= f"https://some-random-api.ml/canvas/youtube-comment?username={username}&comment={comment}&avatar={url}&dark=true​"
       photo_url = p_url.encode('ascii', 'ignore').decode('ascii')
       return await message.reply_photo(photo_url, caption="Made By @NandhaBots")
        
          

@Nandha.on_message(filters.command(["cat","kitty"],config.CMDS))
async def cate(_, message):
      api = requests.get("https://api.thecatapi.com/v1/images/search").json()
      url = api[0]["url"]
      if url.endswith(".gif"): await message.reply_animation(url)
      else: await message.reply_photo(url)

@Nandha.on_message(filters.regex("baka"))
async def baka(_, message):
       reply = message.reply_to_message
       api = requests.get("https://nekos.best/api/v2/baka").json()
       url = api["results"][0]['url']
       anime = api["results"][0]["anime_name"]     
       if reply:
            name = reply.from_user.first_name
            await reply.reply_animation(url,caption="**• {}**\n**Baka! {}**".format(anime, name))
       else:
           name = message.from_user.first_name
           await message.reply_animation(url,caption="**• {}**\n**Baka! {}**".format(anime, name))

@Nandha.on_message(filters.regex("hug"))
async def hug(_, message):
       reply = message.reply_to_message
       api = requests.get("https://nekos.best/api/v2/hug").json()
       url = api["results"][0]['url']
       anime = api["results"][0]["anime_name"]     
       if reply:
            name = reply.from_user.first_name
            await reply.reply_animation(url,caption="**• {}**\n**Hugs! {}**".format(anime, name))
       else:
           name = message.from_user.first_name
           await message.reply_animation(url,caption="**• {}**\n**Hugs! {}**".format(anime, name))

@Nandha.on_message(filters.command("insult",config.CMDS))
async def insult(_, message):
      reply = message.reply_to_message
      try:
          insult = requests.get("https://insult.mattbas.org/api/insult").text
          if reply:
               string = insult.replace("You are",reply.from_user.first_name)
               await message.reply(string)
          else:
              string = insult.replace("You are",message.from_user.first_name)
              await message.reply(string)
      except Exception as e:
          await message.reply(e)

@Nandha.on_message(filters.command("riddle",config.CMDS))
async def riddle(_, message):
     riddle = requests.get("https://riddles-api.vercel.app/random").json()
     question = riddle["riddle"]
     answer = riddle["answer"]
     msg = await message.reply(f"**• Riddle**:\n[ `{question}` ]\n\n[ `The Answer will show automaticly 20seconds after tell me your guess's!` ]")
     await asyncio.sleep(20)
     await msg.edit(f"**• Riddle**:\n[ `{question}` ]\n\n• **Answer**: [ `{answer}` ]")
     

@Nandha.on_message(filters.command("quote",config.CMDS))
async def quote(_, m):
    api = random.choice(requests.get("https://type.fit/api/quotes").json())
    string = api["text"]
    author = api["author"]
    await m.reply(
        f"**Quotes**:\n`{string}`\n\n"
        f"   ~ **{author}**")
        

__MODULE__ = "Fun"

__HELP__ = """
- `/quote`: get random quotes.
- `/riddle`: get random riddle question.
- `/insult`: reply to user or self for insult.
- `/cat`: cute cat random images 
- `/dog`: dog random funny video and images .

**Regex**:
baka - hug
reply to or it slef.
"""
