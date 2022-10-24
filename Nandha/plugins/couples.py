import config
import random

from pyrogram import filters
from pyrogram.types import *
from pyrogram import enums
from datetime import datetime

from Nandha import Nandha
from Nandha.help.couplesdb import *


def date():
   now = datetime.now()
   dt = now.strftime("%d/%m/%Y")
   return dt
      

def today():
    return str(date())

def tomorrow():
     today = date()
     day = int(today.split("/")[0]) +1
     month = date().split("/")[1]
     year = date().split("/")[2]
     tomorrow = str(day)+"/"+month+"/"+year
     return tomorrow

@Nandha.on_message(filters.command("couples",config.CMDS))
async def couples(_, message):
     chat_id = message.chat.id
     if message.chat.type == enums.ChatType.PRIVATE:
          return await message.reply("Only Groups!")
     else:
        couples = []
        async for member in Nandha.get_chat_members(chat_id):
               if not member.user.is_bot:
                     couples.append(member.user.id)
        if len(couples) <2:
             return await message.reply("`Not enough Members!`")
        men = random.choice(couples)
        women = random.choice(couples)
        while men == women:
            men = random.choice(couples)
        couple = {"men":men,"women":women}
        if not chat_id in get_chats():
              save_couple(chat_id,today(),couple)
              x = check_couple(chat_id,today(),couple)
              await message.reply(x)
        else:
             x = check_couple(chat_id,today(),couple)
             await message.reply(x)
             
               
