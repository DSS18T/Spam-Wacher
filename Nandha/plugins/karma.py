import config

from Nandha import Nandha
from pyrogram import filters
from pyrogram import enums
from Nandha.help.karmadb import *

KARMA = "thx|thank|pro|xd|sigma|wah|good|cool"

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


KARMA = "noob|bot|fuck|bish|wtf|kid|bad|sad"

@Nandha.on_message(filters.regex(KARMA))
async def unkarma(_, message):
     reply = message.reply_to_message
     if not reply:
        return
     user_id = reply.from_user.id
     if message.from_user.id == user_id:
           return 
     else: remove_karma(user_id)
     karma = get_karma(user_id)
     await reply.reply(
        f"**Karma for {reply.from_user.first_name}**:\n\n"
        f"**Karma Decreased**: `{karma}`")

@Nandha.on_message(filters.command("karma",config.CMDS))
async def karma(_, message):
      reply = message.reply_to_message
      if reply:
           user_id = reply.from_user.id
           mention = reply.from_user.mention
      else: user_id = message.from_user.id
      mention = message.from_user.mention
      karma = get_karma(user_id)
      await message.reply("**{}'s Karma**: `{}`".format(mention, karma))

