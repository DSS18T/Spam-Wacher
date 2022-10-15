import config

from pyrogram import filters
from pyrogram.types import *
from Nandha import Nandha
from Nandha.help.admin import *

@Nandha.on_message(filters.command("lock",config.CMDS))
async def lock(_, message):
      chat_id = message.chat.id
      user_id = message.from_user.id
      try:
           if (await is_admin(chat_id,user_id)) == True:
                if len(message.text.split()) <2:
                     return await message.reply("`Please input the locktypes.`")
                locktypes = message.text.split()[1]
                if locktypes in "all":
                    await Nandha.set_chat_permissions(chat_id, ChatPermissions())
                    await message.reply("`locked all!`")
                elif locktypes in "msg":
                    await Nandha.set_chat_permissions(chat_id,ChatPermissions(can_send_messages=False))
                    await message.reply("`locked messages!`")
                elif locktypes in "media":
                     await Nandha.set_chat_permissions(chat_id,ChatPermissions(can_send_media_messages=False))
      except Exception as e:         
          await message.reply(e)
