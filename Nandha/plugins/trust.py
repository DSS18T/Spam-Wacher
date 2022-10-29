
from Nandha import Nandha
from pyrogram import filters
from pyrogram import enums
from Nandha.help.trustdb import *

TRUST = "trust|thank|pro|thx"

@Nandha.on_message(filters.regex(TRUST))
async def trust(_, message):
     reply = message.reply_to_message
     if not reply:
        return
     user_id = reply.from_user.id
     if message.from_user.id == user_id:
          return 
     else: add_trust(user_id)
     trust = get_trust(user_id)
     await reply.reply(
        f"**TRUST for {reply.from_user.first_name}**:\n\n"
        f"**Trust increased**: `{trust}`")
