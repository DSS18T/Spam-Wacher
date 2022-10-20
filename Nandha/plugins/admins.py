import config

from Nandha import Nandha
from pyrogram import enums
from Nandha.help.admin import *
from pyrogram import filters
from pyrogram.types import *
from pyrogram.errors import AdminRankInvalid
from datetime import datetime as time


@Nandha.on_message(filters.command("purge",config.CMDS))
async def purge(_, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    reply = message.reply_to_message
    if message.chat.type == enums.ChatType.PRIVATE:
           for ids in range(reply.id, message.id +0):
             await Nandha.delete_messages(chat_id, ids)
    await message.reply(f"**Success Purged {(len({ids})} messages!**")
    else:
       if (await is_admin(chat_id,user_id)) == False:
            return await message.reply("`Admins Only!`")
       elif (await can_delete_messages(chat_id,user_id)) == False:
            return await message.reply("`You Don't have Enough Rights to Do This!`")
       else:
          if (await is_admin(chat_id,config.BOT_ID)) == False:
               return await message.reply("`Make you Sure I'm Admin!`")
          elif (await can_delete_messages(chat_id,user_id)) == False:
               return await message.reply("`I Don't have Enough Rights to Do This!`")
          else:
                if reply:
                     message_reply_id = reply.id
                     message_id = message.id
                elif not reply:
                      return await message.reply("`Reply to Message for purge!`")
                start = time.now()
                for ids in range(message_reply_id, message_id +0):
                    await Nandha.delete_messages(chat_id, ids)
                end = time.now()
                y = (end - start).microseconds / 10000
                await message.reply(f"`Purged!` {y} ms!")


@Nandha.on_message(filters.command("admins",config.CMDS))
async def admins(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    admin = "**Admins in this Group**!\n\n"
    async for admins in Nandha.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
           admin += f"• `{admins.user.first_name}`\n"
    await message.reply(text=(admin))
              


@Nandha.on_message(filters.command("setphoto",config.CMDS))
async def setchatphoto(_, message):
     chat_id = message.chat.id
     user_id = message.from_user.id
     reply = message.reply_to_message
     if (await is_admin(chat_id,user_id)) == False:
            return await message.reply_text("`Only Admins!`")
     elif (await can_change_info(chat_id,user_id)) == False:
            return await message.reply_text("`You Don't have Enough Rights to Do This!`")
     else:
         if reply and not reply.media:
               return await message.reply("`please reply to a photo or document file to insert photo!`")   

         elif reply and reply.media:
              photo = await reply.download() 
         elif not reply and len(message.text.split()) >1:
                  photo = await Nandha.download_media(message.text.split(None, 1)[1])
         elif not reply and len(message.text.split()) <2:
              return await message.reply("`give me a photo id or reply to photo!`")
         if (await is_admin(chat_id,config.BOT_ID)) == False:
                     return await message.reply("`Make you sure I'm Admin!`")
         else:
             await Nandha.set_chat_photo(chat_id=chat_id,photo=photo)
             await message.reply("**Successfully New Photo Insert!**")



@Nandha.on_message(filters.command("settitle",config.CMDS))
async def setchattitle(_, message):
     chat_id = message.chat.id
     user_id = message.from_user.id
     reply = message.reply_to_message
     if (await is_admin(chat_id,user_id)) == False:
         return await message.reply_text("`Only Admins!`")
     elif (await can_change_info(chat_id,user_id)) == False:
         return await message.reply_text("`You Don't have Enough Rights to Do This!`")
     else:
         if reply:
             title = reply.text         
         elif not reply and len(message.text.split()) <2:
                return await message.reply("`give a title or reply to a message to set title!`")
         elif not reply and len(message.text.split()) >1:  
                title = message.text.split(None,1)[1]
         if (await is_admin(chat_id,config.BOT_ID)) == False:
                return await message.reply("`Make you sure I'm Admin!`")
         else:
             await Nandha.set_chat_title(chat_id, title=title)
             await message.reply("`Successfully New title Inputed!`")
             




@Nandha.on_message(filters.command("promote",config.CMDS))
async def promoting(_, message):
       reply = message.reply_to_message
       chat_id = message.chat.id
       user_id = message.from_user.id
       if (await is_admin(chat_id,user_id)) == False:
            return await message.reply("`Admins Only!`")
       elif (await can_promote_members(chat_id,user_id)) == False:
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
                   try:
                       await message.chat.promote_member(user_id=user_id,privileges=bot.privileges)
                       await Nandha.set_administrator_title(chat_id, user_id, title=admin_title)
                       await message.reply(f"**Successfully Promoted**!\n**Following Admin Title**:\n`{admin_title}`") 
                   except AdminRankInvalid:
                      return await message.reply("`Input maximum 8 characters!`")



@Nandha.on_message(filters.command("demote",config.CMDS))
async def demoting(_, message):
       reply = message.reply_to_message
       chat_id = message.chat.id
       user_id = message.from_user.id
       if (await is_admin(chat_id,user_id)) == False:
            return await message.reply("`Admins Only!`")
       elif (await can_promote_members(chat_id,user_id)) == False:
            return await message.reply("`You Don't Have Enough Rights!`")
       else:
                bot = await Nandha.get_chat_member(chat_id,config.BOT_ID)
                if reply:
                     user_id = reply.from_user.id
                elif not reply and len(message.text.split()) <3:
                      user_id = message.text.split()[1]
                else:
                    return await message.reply("`reply to admin or give a userid to demote!`")
                              
                if (await is_admin(chat_id,config.BOT_ID)) == False:
                      await message.reply("`Make you sure I'm Admin!`")
                elif (await can_promote_members(chat_id,config.BOT_ID)) == False:
                      await message.reply("`I don't have enough rights to demote!`")
                else:
                   try:
                       await message.chat.promote_member(user_id=user_id,
                       privileges=ChatPrivileges(
               can_change_info=False,
               can_invite_users=False,
               can_delete_messages=False,
               can_restrict_members=False,
               can_pin_messages=False,
               can_promote_members=False,
               can_manage_chat=False,
               can_manage_video_chats=False))
                       await message.reply(f"**Successfully Demoted!**!") 
                   except Exception as e:
                      return await message.reply(e)
