import strings
import config
from Nandha import Nandha
from pyrogram import filters

import time
import importlib
from Nandha.help.utils.misc import paginate_modules
from Nandha.plugins import ALL_MODULES
from Nandha.help.subs import check_sub
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
    return (strings.HELP_TEXT, keyboard)

@Nandha.on_message(filters.command("help",config.CMDS))
async def _help(_, message):
  text, keyboard = await help_parser(message.from_user.first_name)
  return await message.reply_video(
      config.profile,
      caption=strings.HELP_TEXT,
      reply_markup=keyboard
    )

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

@Nandha.on_message(filters.command("start",config.CMDS))
async def start(_, message):
      user_id = message.from_user.id
      mention = message.from_user.mention
      if message.chat.type == enums.ChatType.PRIVATE:
          if not user_id in (await get_users()):
                await add_user(user_id)
                await Nandha.send_message("Spamwatcher", text=(
                     "**#NEWUSER**:\n"
                     f"**UserID**: {user_id}\n"
                     f"**profile link**: {mention}"))
                return await message.reply_video(config.profile,caption=strings.START_TEXT,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Help Commands!",callback_data="help_back"),]]))
          else: return await message.reply_video(config.profile,caption=strings.START_TEXT,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Help Commands!",callback_data="help_back"),]]))
      else:
         await check_sub(message, user_id)
         return await message.reply_video(config.profile,caption=strings.START_TEXT,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Help Commands!",callback_data="help_back"),]]))


if __name__ == "__main__":
    Nandha.run()

