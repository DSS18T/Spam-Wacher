import config
import random
import re
import requests
import asyncio
from Nandha import Nandha
from Nandha.help.admin import *
from pyrogram.types import *
from pyrogram import filters

@Nandha.on_message(filters.command(["sban","ban"],config.CMDS))
async def bans(_, message):
      user_id = int(message.from_user.id)
      chat_id = int(message.chat.id)
      reply = message.reply_to_message
      api = requests.get("https://api.waifu.pics/sfw/kick").json()
      url = api["url"]
      try:
          if (await can_ban_members(chat_id,user_id)) == True or message.from_user.id in config.DEVS:   
                if not reply and len(message.command) >2:
                    ban_id = int(message.text.split(" ")[1])
                    reason = message.text.split(None, 2)[2]
                elif not reply and len(message.command) == 2:
                    ban_id = int(message.text.split(" ")[1])
                    reason = None
                elif reply and len(message.command) >1:
                    ban_id = reply.from_user.id
                    reason = message.text.split(None, 1)[1]        
                elif reply and len(message.command) <2:
                     ban_id = reply.from_user.id
                     reason = None
                if (await is_admin(chat_id, config.BOT_ID)) == False:
                      return await message.reply_text("`Make you sure I'm Admin!`")
                elif ban_id == config.BOT_ID:
                       return await message.reply_text("`I can't ban myself!`")
                elif ban_id in config.DEVS:
                       return await message.reply_text("`I can't do against my owner!`")
                elif (await is_admin(chat_id, ban_id)) == True:
                       return await message.reply_text("`The User Is Admin! I can't ban!`")
                if re.search("s", message.text.split()[0]):
                      msg = await Nandha.ban_chat_member(chat_id, ban_id)
                      await msg.delete()
                      await message.delete()
                else:
                    await Nandha.ban_chat_member(chat_id, ban_id)
                    await message.reply_animation(url,caption=f"The Bitch As Dust!\n • `{ban_id}`\n\nFollowing Reason:\n`{reason}`",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Unban", callback_data=f"unban_btn:{ban_id}")]]))          
      except Exception as e:
         await message.reply_text(e)
       
@Nandha.on_callback_query(filters.regex("unban_btn"))
async def unban_btn(_, query):
      chat_id = query.message.chat.id
      user_id = query.from_user.id
      ban_id = query.data.split(":")[1]
      api = requests.get("https://api.waifu.pics/sfw/smile").json()
      url = api["url"]
      try:
         if (await is_admin(chat_id, user_id)) == False:
               return await query.answer("Admins Only!", show_alert=True)
         else:
            await Nandha.unban_chat_member(chat_id, ban_id)
            await query.message.edit_media(media=InputMediaAnimation(url,caption=f"`fine they can join again now!`\nID: `{ban_id}`"))
      except Exception as e:
            msg = await query.message.reply_text(e)
            await asyncio.sleep(10)
            await msg.delete()
