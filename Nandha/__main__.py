
import config
from Nandha import Nandha
from pyrogram import filters

import time
import importlib
from Nandha.help.utils.misc import paginate_modules
from Nandha.plugins import ALL_MODULES
from pyrogram import filters
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
    return ("**Konnichiwa {},** `I Am Hottie, The Hottest And Coolest Robot Available On Telegram`\n\n• `I Have Lot's Of Hot And Smexy Commands`\n•`To Get Known About These Commands Checkout The Buttons Given Bellow`\n\n**×× Want To Vibe With Me ? Join @CityOfCreations ^_^**".format(name), keyboard)

@Nandha.on_callback_query(filters.regex("help"))
async def _help(_, query):
  text, keyboard = await help_parser(message.from_user.first_name)
  return await query.message.edit(text,
      reply_markup=keyboard
    )

@Nandha.on_callback_query(filters.regex("bot_commands"))
async def commands_callbacc(_, query):
  text, keyboard = await help_parser(query.from_user.first_name)
  await query.message.edit(text,
    reply_markup=keyboard
  )
  return await bot.answer_callback_query(query.id)

@Nandha.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(client, query):
  home_match = re.match(r"help_home\((.+?)\)", query.data)
  mod_match = re.match(r"help_module\((.+?)\)", query.data)
  prev_match = re.match(r"help_prev\((.+?)\)", query.data)
  next_match = re.match(r"help_next\((.+?)\)", query.data)
  back_match = re.match(r"help_back", query.data)
  create_match = re.match(r"help_create", query.data)
  top_text = "**Konnichiwa {},** `I Am Hottie, The Hottest And Coolest Robot Available On Telegram`\n\n• `I Have Lot's Of Hot And Smexy Commands`\n•`To Get Known About These Commands Checkout The Buttons Given Bellow`\n\n**×× Want To Vibe With Me ? Join @CityOfCreations ^_^**".format(query.from_user.first_name)
  if mod_match:
    module = (mod_match.group(1)).replace(" ", "_")
    text = (
        "**{}** `{}` **{}**:\n".format(
          "Here Is The Help For The", HELPABLE[module].__MODULE__, "Module"
        )
        + HELPABLE[module].__HELP__
    )

    await query.message.edit(
      text,
      reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("Back Home", callback_data="help_back")]]
      )
    )
  elif home_match:
    await query.message.edit(text="hi {}".format(query.from_user.mention),
      reply_markup=START_KEYBOARD
    )
  elif prev_match:
    curr_page = int(prev_match.group(1))
    await query.message.edit(
      top_text,
      reply_markup=InlineKeyboardMarkup(
        paginate_modules(curr_page - 1, HELPABLE, "help")
      )
    )

  elif next_match:
    next_page = int(next_match.group(1))
    await query.message.edit(
      top_text,
      reply_markup=InlineKeyboardMarkup(
        paginate_modules(next_page + 1, HELPABLE, "help")
      )
    )

  elif back_match:
    await query.message.edit(
      top_text,
      reply_markup=InlineKeyboardMarkup(
        paginate_modules(0, HELPABLE, "help")
      )
    )

  elif create_match:
    text, keyboard = await help_parser(query.from_user.first_name)
    await query.message.edit(
      text,
      reply_markup=keyboard
    )

  return await Nandha.answer_callback_query(query.id)


@Nandha.on_message(filters.command("start"))
async def start(_, message):
      await message.reply_video(video="https://telegra.ph/file/921195f5e140f8f77392c.mp4", caption="hello!",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Help",callback_data="help"),]]))
if __name__ == "__main__":
    Nandha.run()

