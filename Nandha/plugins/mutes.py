import config

from Nandha import Nandha
from Nandha.help.admin import *
from pyrogram.types import *
from pyrogram import filters

@Nandha.on_message(filters.command("mute",config.CMDS))
async def muted(_, message):
      user_id = int(message.from_user.id)
      chat_id = int(message.chat.id)
      reply = message.reply_to_message
      try:
          if (await can_ban_members(chat_id,user_id)) == True:   
                if not reply and len(message.command) >2:
                    mute_id = int(message.text.split(" ")[1])
                    reason = message.text.split(None, 2)[2]
                elif not reply and len(message.command) == 2:
                    mute_id = int(message.text.split(" ")[1])
                    reason = None
                elif reply and len(message.command) >1:
                    mute_id = reply.from_user.id
                    reason = message.text.split(None, 1)[1]        
                elif reply and len(message.command) <2:
                     mute_id = reply.from_user.id
                     reason = None
                if (await is_admin(chat_id, config.BOT_ID)) == False:
                      return await message.reply_text("`Make you sure I'm Admin!`")
                elif mute_id == config.BOT_ID:
                      return await message.reply_text("`I can't ban myself!`")
                elif (await is_admin(chat_id, mute_id)) == True:
                       return await message.reply_text("`The User Is Admin! I can't ban!`")
                else:
                     await message.reply_sticker(random.choice(config.FUNNY_STICKER))
                     await Nandha.restrict_chat_member(chat_id, mute_id, ChatPermissions(can_send_messages=False))
                     await message.reply_text(f"The Bitch Muted!\n • `{ban_id}`\n\nFollowing Reason:\n`{reason}`",
                     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Unmute", callback_data=f"unmute_btn:{mute_id}")]]))
      except Exception as e:
         await message.reply_text(e)
                     


@Nandha.on_callback_query(filters.regex("unmute_btn"))
async def unmute_btn(_, query):
      chat_id = query.message.chat.id
      user_id = query.from_user.id
      mute_id = query.data.split(":")[1]
      try:
          if (await is_admin(chat_id, user_id)) == False:
                return await query.answer("Admins Only!")
          else:
             await Nandha.restrict_chat_member(chat_id, mute_id, ChatPermissions(can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True))
             await query.message.edit(f"`Semms mute done mistakely admins restored a mute!`\nID: `{ban_id}`")
      except Exception as e:
            await query.message.reply_text(e)
