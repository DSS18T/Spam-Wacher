import config
import random

from pyrogram import filters
from pyrogram.types import *
from pyrogram import enums
from datetime import datetime

from Nandha import Nandha


def date():
   now = datetime.now()
   dt = int(now.strftime("%d/%m/%Y"))
   return dt
      

def today():
    return date()

def tomorrow():
     tom = (date() +1)
     return tom

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
        men_m = (await Nandha.get_users(men)).mention
        women_m = (await Nandha.get_users(women)).mention
        await message.reply(f"""**New Couples Arrived!**

**Men**: **{men_m}**
**women**: **{women_m}**

**we all wish you happy marrie life 🤭🤭😂❤️!**
""")
               
