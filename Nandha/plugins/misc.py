
import config

from Nandha import Nandha
from pyrogram import filters
from datetime import datetime as time

@Nandha.on_message(filters.command("ping"))
async def ping(_, message):
      start = time.now()
      end = time.now()
      ping = (end - start) / 1000
      await message.reply("**PING**: {ping}")
