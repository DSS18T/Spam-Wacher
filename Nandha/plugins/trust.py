
from Nandha import Nandha
from pyrogram import filters
from pyrogram import enums
from Nandha.help.trustdb import *


@Nandha.on_message(filters.regex("+|trust|thanks|pro"))
async def trust(_, message):
     reply = message.reply_to_message
     if not reply:
        return
     user_id = reply.from_user.id
     if message.from_user.id == user_id:
          return 
     else: add_trust(user_id)
     trust = get_trust(user_id)
     await message.reply(
        "**TRUST**:\n"
        f"**increased**: `{trust}`")
