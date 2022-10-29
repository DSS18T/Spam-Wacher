
from Nandha import Nandha
from pyrogram import filters
from pyrogram import enums
from Nandha.help.karmadb import *

KARMA = "whom|thx|thank|pro|xd|sigma|wah"

@Nandha.on_message(filters.regex(KARMA))
async def karma(_, message):
     reply = message.reply_to_message
     if not reply:
        return
     user_id = reply.from_user.id
     if message.from_user.id == user_id:
          return 
     else: add_karma(user_id)
     karma = get_karma(user_id)
     await reply.reply(
        f"**Karma for {reply.from_user.first_name}**:\n\n"
        f"**Karma increased**: `{karma}`")

UNKARMA = "wtf|noob|bitch|kid|nimba|fuck"

@Nandha.on_message(filters.regex(UNKARMA))
async def unKarma(_, message):
     reply = message.reply_to_message
     if not reply:
        return
     user_id = reply.from_user.id
     if message.from_user.id == user_id:
          return 
     elif not message.from_user.id in get_karma_users():
          return
     else: remove_karma(user_id)
     karma = get_karma(user_id)
     await reply.reply(
        f"**Karma for {reply.from_user.first_name}**:\n\n"
        f"**Karma Decreased**: `{karma}`")
