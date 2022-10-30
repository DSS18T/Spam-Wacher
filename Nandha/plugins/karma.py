import config

from Nandha import Nandha
from pyrogram import filters
from pyrogram import enums
from Nandha.help.karmadb import *
from Nandha.help.admin import *

KARMA = "👍|\+|thx|thank|pro|xd|sigma|wah|good|cool"

@Nandha.on_message(filters.command("karmas",config.CMDS))
async def karma_chat(_, message):
      chat_id = message.chat.id
      user_id = message.from_user.id
      if (await is_admin(chat_id,user_id)) == True:
          if len(message.text.split()) == 2:
                  x = message.text.split()[1].lower()
                  if x == "on":
                     on_karma(chat_id)
                     await message.reply("`Karma Successfully Enabled!`")
                  elif x == "off":
                     if is_karma_chat(chat_id) == None:
                         await message.reply("`Karma Not Enabled Here!`")
                     elif is_karma_chat(chat_id) == True:
                           off_karma(chat_id)
                           await message.reply("`Karma Successfully Disabled!`")
          else: return await message.reply("`Wrong Method!`")
                      
      else: return await message.reply("`Admins Only!`")

@Nandha.on_message(filters.regex(KARMA))
async def karma(_, message):
     reply = message.reply_to_message
     if is_karma_chat(message.chat.id) == True:
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


KARMA = "👎|\-|noob|bot|fuck|bish|wtf|kid|bad|Sad"

@Nandha.on_message(filters.regex(KARMA))
async def unkarma(_, message):
     if is_karma_chat(message.chat.id) == True:
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
      if not reply:
           user_id = message.from_user.id
           mention = message.from_user.mention
      else: 
           user_id = reply.from_user.id
           mention = reply.from_user.mention
      karma = get_karma(user_id)
      await message.reply("**{}'s Karma**: `[``{}``]`".format(mention, karma))

__MODULE__ = "Karma"

__HELP__ = """
**Upvote** - Use upvote keywords like "+", "cool", "thanks", etc. to upvote a message.
**Downvote** - Use downvote keywords like "-", "Sad", etc. to downvote a message.
**Commands**
➛ /karma**:** reply to a user to check that user's karma points.
"""
