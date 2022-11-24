import strings
import config
from Nandha import Nandha, UB
from pyrogram import filters

import time
import importlib
from Nandha.help.utils.misc import paginate_modules
from Nandha.plugins import ALL_MODULES
from Nandha.help.usersdb import (
add_user, get_users)
from Nandha.help.rulesdb import (
rules_chat, get_rules)
from pyrogram import filters
from pyrogram import enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaVideo
import re




HELPABLE = {}

def get_helps():
    global HELPABLE
    for module in ALL_MODULES:
        imported_module = importlib.import_module("Nandha.plugins." + module)
        if (
            hasattr(imported_module, "__MODULE__")
            and imported_module.__MODULE__
        ):
            imported_module.__MODULE__ = imported_module.__MODULE__
            if (
                hasattr(imported_module, "__HELP__")
                and imported_module.__HELP__
            ):
                HELPABLE[
                    imported_module.__MODULE__.replace(" ", "_").lower()
                ] = imported_module


get_helps()

async def help_parser(name, keyboard=None):
  if not keyboard:
    keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return (strings.HELP_TEXT, keyboard)

Button = InlineKeyboardMarkup([[InlineKeyboardButton("Help",url=f"https://t.me/{config.USERNAME}?start=help")]])

@Nandha.on_message(filters.command("help",config.CMDS))
async def _help(_, message):
       if message.reply_to_message:
          await message.reply_to_message.reply_text("Click The Below Button to Know How to Use Commands!",
           reply_markup=Button)
       else:
          await message.reply_text("Click The Below Button to Know How to Use Commands!",
           reply_markup=Button)

@Nandha.on_callback_query(filters.regex("bot_commands"))
async def commands_callbacc(_, query):
  text, keyboard = await help_parser(query.from_user.first_name)
  await query.message.edit_media(
    media=InputMediaVideo(
      config.profile,
      caption=text
    ),
    reply_markup=keyboard
  )
  return await Nandha.answer_callback_query(query.id)

@Nandha.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(client, query):
  home_match = re.match(r"help_home\((.+?)\)", query.data)
  mod_match = re.match(r"help_module\((.+?)\)", query.data)
  prev_match = re.match(r"help_prev\((.+?)\)", query.data)
  next_match = re.match(r"help_next\((.+?)\)", query.data)
  back_match = re.match(r"help_back", query.data)
  create_match = re.match(r"help_create", query.data)
  top_text = strings.HELP_TEXT
  if mod_match:
    module = (mod_match.group(1)).replace(" ", "_")
    text = (
        "**{}** `{}` **{}**:\n".format(
          "Here Is The Help For The", HELPABLE[module].__MODULE__, "Module"
        )
        + HELPABLE[module].__HELP__
    )

    await query.message.edit_caption(
      caption=text,
      reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("Back 🔄", callback_data="help_back")]]
      )
    )
  elif home_match:
    await query.message.edit_caption(caption=strings.START_TEXT,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Help Commands!",callback_data="help_back"),]])
    )
  elif prev_match:
    curr_page = int(prev_match.group(1))
    await query.message.edit_caption(
      caption=top_text,
      reply_markup=InlineKeyboardMarkup(
        paginate_modules(curr_page - 1, HELPABLE, "help")
      )
    )

  elif next_match:
    next_page = int(next_match.group(1))
    await query.message.edit_caption(
      caption=top_text,
      reply_markup=InlineKeyboardMarkup(
        paginate_modules(next_page + 1, HELPABLE, "help")
      )
    )

  elif back_match:
    await query.message.edit_caption(
      caption=top_text,
      reply_markup=InlineKeyboardMarkup(
        paginate_modules(0, HELPABLE, "help")
      )
    )

  elif create_match:
    text, keyboard = await help_parser(query.from_user.first_name)
    await query.message.edit_caption(
      caption=text,
      reply_markup=keyboard
    )

  return await Nandha.answer_callback_query(query.id)

sub_txt = "`Oh man Please Dm Me And Start I don't know Who are You?`"

sub_keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Pm to Access", user_id=config.BOT_ID)]])



NUT = """
#NEWUSER
NAME: **{}**
UID: `{}`
"""


@UB.on_message(filters.me & filters.commamd("alive",config.CMDS))
async def alive(_, message):
      await message.reply_text("`Alive!`")

@Nandha.on_message(filters.command("start",config.CMDS))
async def start(_, message):
     chat = message.chat
     user = message.from_user
     text, keyboard = await help_parser(user.first_name)
     if len(message.text.split()) >1:
          name = message.text.split(None, 1)[1]
          if name[0:4] == "help":
              return await message.reply_video(config.profile,caption=strings.HELP_TEXT,reply_markup=keyboard)
          elif name[0:5] == "rules":
            chat_id = int(name.split("s")[1])
            if not chat_id in rules_chat():
                 return await message.reply(f"`{chat_id}` don't have rules!")
            else: 
                 x = get_rules(chat_id)
                 return await message.reply_text(x)
     if message.chat.type == enums.ChatType.PRIVATE:
         if not user.id in get_users():
             add_user(user.id)
             await Nandha.send_message(config.LOG_CHANNEL_ID,NUT.format(user.mention,user.id))
             return await message.reply_video(config.profile,caption=strings.START_TEXT,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Help Commands!",callback_data="help_back"),]]))
         else: return await message.reply_video(config.profile,caption=strings.START_TEXT,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Help Commands!",callback_data="help_back"),]]))
     else: return await message.reply_video(config.profile,caption=strings.START_TEXT,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Help Commands!",callback_data="help_back"),]]))


if __name__ == "__main__":
      Nandha.run()
      with Nandha:
          Nandha.send_sticker(config.GROUP_ID, sticker="CAACAgQAAx0CatX7ugAC1Q5je29sMbWkm8pX9KFL-LgW5MScSgACXgEAAiIN2QABm8LQQ_qSuqceBA")
