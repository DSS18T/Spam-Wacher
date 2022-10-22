import config
import requests
from Nandha import Nandha
from pyrogram import filters



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

@Nandha.on_message(filters.command("riddle"))
async def riddle(_, message):
     riddle = requests.get("https://riddles-api.vercel.app/random").json()
     msg = await message.reply((
              "**• riddle**:-\n"
             f"`{riddle["riddle"]}`"))
     await asyncio.sleep(5)
     await msg.edit(f"{msg.text}\n\n• **Answer**: [`{riddle["answer"]}`]")
     


    
