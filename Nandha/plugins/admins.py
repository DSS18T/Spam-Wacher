import config

from Nandha import Nandha
from Nandha.help.admin import *
from pyrogram import filters
from pyrogram.types import *

@Nandha.on_message(filters.command(["fpromote","promote"],config.CMDS))
async def promoting(_, message):
       reply = message.reply_to_message
       chat_id = message.chat.id
       user_id = message.from_user.id
       if (await is_admin(chat_id,user_id)) == False:
            return await message.reply("`Admins Only!`")
       eilf (await can_promote_members(chat_id,user_id)) == False:
            return await message.reply("`You Don't Have Enough Rights!`")
       else:
                bot = await Nandha.get_chat_member(chat_id,config.BOT_ID)
                if reply and len(message.text.split()) >1:
                     user_id = reply.from_user.id
                     admin_title = message.text.split(None,1)[1]
                elif reply and len(message.text.split()) <2:
                      user_id = reply.from_user.id
                      admin_title = "Admin"
                elif not reply and len(message.text.split()) >1:
                      user_id = message.text.split()[1]
                      admin_title = message.text.split(None,2)[2]
                elif not reply and len(message.text.split()) <3:
                     user_id = message.text.split()[1]
                     admin_title = "Admin"                
                if (await is_admin(chat_id,config.BOT_ID)) == False:
                      await message.reply("`Make you sure I'm Admin!`")
                elif (await can_promote_members(chat_id,config.BOT_ID)) == False:
                      await message.reply("`I don't have enough rights to promote!`")
                elif (await is_admin(chat_id,user_id)) == True:
                      await message.reply("`User Already A Admin!`")
                else:
                     await message.chat.promote_member(user_id=user_id,privileges=bot.privileges)
                     await Nandha.set_administrator_title(chat_id, user_id, title=admin_title)
                     await message.reply(f"**Successfully Promoted**!\n**Following Admin Tile**:\n`{admin_title}`") 
       
