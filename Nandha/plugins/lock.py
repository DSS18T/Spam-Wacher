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
                elif locktypes in "invite":
                     await Nandha.set_chat_permissions(chat_id,ChatPermissions(
                     can_send_messages=True,
                     can_send_media_messages=True,
                     can_send_other_messages=True,
                     can_add_web_page_previews=True,
                     can_invite_users=False,
                     can_send_polls=True ))
                     await message.reply("`locked invite!`")
                elif locktypes in "media":
                     await Nandha.set_chat_permissions(chat_id,ChatPermissions(
                     can_send_messages=True,
                     can_send_media_messages=False,
                     can_send_other_messages=False,
                     can_add_web_page_previews=True,
                     can_invite_users=True,
                     can_send_polls=True))
                     await message.reply("`locked medias!`")
                elif locktypes in "poll":
                     await Nandha.set_chat_permissions(chat_id,ChatPermissions(
                     can_send_messages=True,
                     can_send_media_messages=True,
                     can_send_other_messages=True,
                     can_add_web_page_previews=True,
                     can_invite_users=True,
                     can_send_polls=False))
                     await message.reply("`locked polls!`")         
      except Exception as e:         
          await message.reply(e)



LOCKTYPES = """
`you can lock this list of chat permissions!`

• `all`: for lock (chat all permissions)
• `media`: for lock chat (medias and other kid of msgs)
• `poll`: for lock chat (sending polls)
• `invite`: for lock (inviting users)
"""

@Nandha.on_message(filters.command("locktypes"))
async def locktypes(_, message):
     if (await is_admin(message.chat.id, message.from_user.id)) == True:
          await message.reply_text(LOCKTYPES)
     else:
        await message.reply_text("`Admins Only!`")


