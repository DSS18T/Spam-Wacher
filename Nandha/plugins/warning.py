import config
from Nandha.help.warnsdb import *
from Nandha import Nandha
from Nandha.help.admin import *
from pyrogram import filters
from pyrogram.types import *


@Nandha.on_message(filters.command("warn",config.CMDS))
async def warn(_, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    reply = message.reply_to_message
    if await is_admin(chat_id,user_id) == False:
        return await message.reply("`Admins Only!`")
    elif await can_ban_members(chat_id,user_id) == False:
        return await message.reply("`You Need Ban Right!`")
    elif await is_admin(chat_id,config.BOT_ID) == False:
        return await message.reply("`I'm not Admins!`")
    elif await can_ban_members(chat_id,config.BOT_ID) == False:
         return await message.reply("`I Need Ban Right!`")
    else:
        if reply and len(message.text.split()) >1:
             user_id = reply.from_user.id
             reason = message.text.split(None,1)[1]             
        elif not reply:
             user_id = message.text.split()[1]
             reason = message.text.split(None,2)[2]
        else: return await message.reply("Invalid Method!")
        if is_warna(user_id) == 3:
           try:
             await message.chat.ban_member(user_id)
             await message.reply("The User Reached Maximum Warns Now Banned!")
           except Exception as e: return await message.reply(e)
        elif not user_id in warn_users():
              add_warn(user_id,reason)
              return await message.reply("Warn Increased {}".format(is_warn(user_id)))
        else: return await message.reply("Somthing went Wrong!")

        
            
