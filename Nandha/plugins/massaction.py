import config

from pyrogram import filters
from pyrogram import enums
from pyrogram.types import *
from Nandha.help.admin import *
from Nandha import Nandha



@Nandha.on_message(filters.command(["unbanall","massunban"],config.CMDS))
async def unbanall(_, message):
     user_id = message.from_user.id
     chat_id = message.chat.id
     if message.chat.type == enums.ChatType.PRIVATE:
          return await message.reply("`This Command Only work in Groups!`")
     else:
       try:
          USERS = []
          async for m in Nandha.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BANNED):
                 USERS.append(m.user.id)
          await message.reply("**Found Banned Members**: `{}`\n**Do you want to Process this Confirm your a Owner**!".format(len(USERS)),
              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Confirm ✅",callback_data=f"unbanall:{USERS}")]]))
       except Exception as e:
           print(e)

@Nandha.on_callback_query(filters.regex("unbanall"))
async def unbanall_btn(_, query):
      user_id = query.from_user.id
      chat_id = query.message.chat.id
      async for m in Nandha.get_chat_members(chat_id):
      try:
         if m.status == enums.ChatMemberStatus.OWNER or user_id in config.DEVS:
             USERS = query.data.split(":")[1]
             msg = await query.message.edit("`processing....`")
             unbanned = 0
             for user_id in USERS:
                  await query.message.chat.unban_member(user_id)
                  s_unban += +1
             await msg.edit("Successfully UNBanned: {}".format(unbanned))
           
         else:  await query.answer("You Can't Access This!", show_alert=True)
                 
      except Exception as e:
         print(e)


@Nandha.on_message(filters.command(["sbanall","banall","massban"],config.CMDS))
async def banall(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if not user_id in config.DEVS:
         return await message.reply("`sorry you can't access!`")
    else:  
       try: 
          Members = []
          Admins = []
          async for x in Nandha.get_chat_members(chat_id):
              if not x.privileges:
                    Members.append(x.user.id)
              else:
                    Admins.append(x.user.id)
          for user_id in Members:
               if message.text.split()[0].lower().startswith("s"):
                        m = await Nandha.ban_chat_member(chat_id, user_id)
                        await m.delete()
               else:
                   await Nandha.ban_chat_member(chat_id, user_id)
          await message.reply_text("**Successfully Banned**: `{}`\n**Remaining Admins**: `{}`".format(len(Members),len(Admins),))
       except Exception as e:
        print(e)

@Nandha.on_message(filters.command(["skickall","kickall","masskick"],config.CMDS))
async def kickall(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if not user_id in config.DEVS:
         return await message.reply("`sorry you can't access!`")
    else:  
       try: 
          Members = []
          Admins = []
          async for x in Nandha.get_chat_members(chat_id):
              if not x.privileges:
                    Members.append(x.user.id)
              else:
                    Admins.append(x.user.id)
          for user_id in Members:
               if message.text.split()[0].lower().startswith("s"):
                        m = await Nandha.ban_chat_member(chat_id, user_id)
                        await Nandha.unban_chat_member(chat_id, user_id)
                        await m.delete()
               else:
                   await Nandha.ban_chat_member(chat_id, user_id)
                   await Nandha.unban_chat_member(chat_id, user_id)
          await message.reply_text("**Successfully Kicked**: `{}`\n**Remaining Admins**: `{}`".format(len(Members),len(Admins),))
       except Exception as e:
        print(e)
