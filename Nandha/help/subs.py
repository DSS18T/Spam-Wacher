import config

from Nandha import Nandha
from Nandha.help.usersdb import get_users
from pyrogram.types import (
InlineKeyboardButton, InlineKeyboardMarkup)


text = "Oh man Please Dm Me And Start I don't know How are You?"

keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Pm to Access", user_id=config.BOT_ID)]])

async def check_sub(message, user_id: int):
      if not user_id in get_users():
           await message.reply_text(text,reply_markup=keyboard)
           return
     
