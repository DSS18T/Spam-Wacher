import config

from Nandha import Nandha
from pyrogram import enums
from Nandha.help.admin import *
from pyrogram import filters
from pyrogram.types import *
from pyrogram.errors import AdminRankInvalid
from datetime import datetime as time


@Nandha.on_message(filters.command("settitle",config.CMDS))
async def set_admin_title(_, message):
     chat_id = message.chat.id
     user_id = message.from_user.id
     reply = message.reply_to_message
     if (await is_admin(chat_id,user_id)) == False:
        return await message.reply("`Admins Only`")
     elif (await is_admin(chat_id,config.BOT_ID)) == False:
        return await message.reply("`I Don't Have Rights!`")
     else:
        try:
           if len(message.text.split()) <2:
               return await message.reply("`Input New Admin Title!`")
           elif reply:
                  user_id = reply.from_user.id
                  title = message.text.split(None,1)[1]
           elif not reply:
                  user_id = int(message.text.split()[1])
                  title = message.text.split(None,2)[2]
           await Nandha.set_administrator_title(chat_id, user_id, title=title)
        except Exception as e: return await message.reply(e)


@Nandha.on_message(filters.command(["glink","grouplink"],config.CMDS))
async def group_link(_, message):
     chat_id = message.chat.id
     user_id = message.from_user.id
     if (await is_admin(chat_id,user_id)) == False:
         return await message.reply("`Admins Only`")
     elif (await is_admin(chat_id,config.BOT_ID)) == False:
         return await message.reply("`I Don't Have Rights!`")
     else:
         try:
            link = (await Nandha.get_chat(chat_id)).invite_link
            await message.reply(link)
         except Exception as e: return await message.reply(e)


@Nandha.on_message(filters.command(["setgdes","setgdesc"],config.CMDS))
async def chat_description(_, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    reply = message.reply_to_message
    if message.chat.type == enums.ChatType.PRIVATE:
          return await message.reply("`This Command work Only In Groups!`")
    elif (await is_admin(chat_id,user_id)) == False or user_id not in config.DEVS:
         return await message.reply_text("`Only Admins!`")
    elif (await can_change_info(chat_id,user_id)) == False or user_id not in config.DEVS:
         return await message.reply_text("`You Don't have Enough Rights to Do This!`")
    else:
         if not reply or reply and not reply.text:
               return await message.reply("reply to message text to set chat description!")
         desc = reply.text
         if len(desc) >250:
               return await message.reply("description is to much text please remove some wards and try again!")
         else:
             try:
                await Nandha.set_chat_description(chat_id, description=desc)
                await message.reply("Successfully Description Added!")
             except Exception as e:
                await message.reply(e)

@Nandha.on_message(filters.command("del",config.CMDS))
async def delete(_, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    reply = message.reply_to_message
    if message.chat.type == enums.ChatType.PRIVATE:
          if not reply:
              return await message.reply("`reply to message to delete!`", quote=True)
          await reply.delete()
          await message.delete()
    else:
        if (await is_admin(chat_id,user_id)) == False or user_id not in config.DEVS:
             return await message.reply("`Admins Only!`")
        elif (await can_delete_messages(chat_id,user_id)) == False or user_id not in config.DEVS:
             return await message.reply("`you don't have enough rights to do this!`")
        else:
            if (await is_admin(chat_id,config.BOT_ID)) == False:
                 return await message.reply("`Im not Admin!`")
            elif (await can_delete_messages(chat_id,config.BOT_ID)) == False:
               return await message.reply("`I don't have enough rights to do this!`")
            else:
               if not reply:
                     return await message.reply("`reply to message to delete!`")
               await reply.delete()
               await message.delete()
    

@Nandha.on_message(filters.command("purge",config.CMDS))
async def purge(_, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    reply = message.reply_to_message
    if message.chat.type == enums.ChatType.PRIVATE:
           start = time.now()
           for ids in range(reply.id, message.id +0):
              await Nandha.delete_messages(chat_id, ids, revoke=True)
           end = time.now()
           delete_time = (end - start).seconds / 10000
           return await message.reply(f"**Success Purged {delete_time}s!**")
    if (await is_admin(chat_id,user_id)) == False or user_id not in config.DEVS:
            return await message.reply("`Admins Only!`")
    elif (await can_delete_messages(chat_id,user_id)) == False or user_id not in config.DEVS:
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
                    await Nandha.delete_messages(chat_id, ids, revoke=True)
                end = time.now()
                y = (end - start).seconds / 10000
                await message.reply(f"**Success Purged {y}s!**")


@Nandha.on_message(filters.command(["admins","adminlist"],config.CMDS))
async def admins(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if message.chat.type == enums.ChatType.PRIVATE:
         return await message.reply("`This Command work Only In Groups!`")
    admin = "**Admins in this Group**!\n\n"
    async for admins in Nandha.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
           admin += f"• **{admins.user.first_name}** - (`{admins.user.id}`)\n"
    await message.reply(text=(admin))
              


@Nandha.on_message(filters.command("setgphoto",config.CMDS))
async def setchatphoto(_, message):
     chat_id = message.chat.id
     user_id = message.from_user.id
     reply = message.reply_to_message
     if message.chat.type == enums.ChatType.PRIVATE:
         return await message.reply("`This Command work Only In Groups!`")
     elif (await is_admin(chat_id,user_id)) == False or user_id not in config.DEVS:
            return await message.reply_text("`Only Admins!`")
     elif (await can_change_info(chat_id,user_id)) == False or user_id not in config.DEVS:
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



@Nandha.on_message(filters.command("setgtitle",config.CMDS))
async def setchattitle(_, message):
     chat_id = message.chat.id
     user_id = message.from_user.id
     reply = message.reply_to_message
     if message.chat.type == enums.ChatType.PRIVATE:
         return await message.reply("`This Command work Only In Groups!`")
     elif (await is_admin(chat_id,user_id)) == False or user_id not in config.DEVS:
         return await message.reply_text("`Only Admins!`")
     elif (await can_change_info(chat_id,user_id)) == False or user_id not in config.DEVS:
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
             




@Nandha.on_message(filters.command(["promote","fpromote","mpromote"],config.CMDS))
async def promoting(_, message):
       reply = message.reply_to_message
       chat_id = message.chat.id
       user_id = message.from_user.id
       if message.chat.type == enums.ChatType.PRIVATE:
         return await message.reply("`This Command work Only In Groups!`")
       elif (await is_admin(chat_id,user_id)) == False or user_id not in config.DEVS:
            return await message.reply("`Admins Only!`")
       elif (await can_promote_members(chat_id,user_id)) == False or user_id not in config.DEVS:
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
                       if message.text[1] == "f":
                           await message.chat.promote_member(user_id=user_id,privileges=bot.privileges)
                           await Nandha.set_administrator_title(chat_id, user_id, title=admin_title)
                           await message.reply(f"**Successfully Full Promoted**!\n**Following Admin Title**:\n`{admin_title}`")
                       elif message.text[1] == "m":
                           await message.chat.promote_member(user_id=user_id,privileges=ChatPrivileges(
               can_invite_users=True,
               can_pin_messages=True,
               can_manage_video_chats=True))
                           await Nandha.set_administrator_title(chat_id, user_id, title=admin_title)
                           await message.reply(f"**Successfully Medium Promoted**!\n**Following Admin Title**:\n`{admin_title}`")
                       else:  
                           await message.chat.promote_member(user_id=user_id,privileges=ChatPrivileges(
               can_invite_users=True,
               can_delete_messages=True,
               can_restrict_members=True,
               can_pin_messages=True,
               can_manage_video_chats=True))
                           await Nandha.set_administrator_title(chat_id, user_id, title=admin_title)
                           await message.reply(f"**Successfully Full Promoted**!\n**Following Admin Title**:\n`{admin_title}`")
                   except AdminRankInvalid:
                      return await message.reply("`Input maximum 8 characters!`")



@Nandha.on_message(filters.command("demote",config.CMDS))
async def demoting(_, message):
       reply = message.reply_to_message
       chat_id = message.chat.id
       user_id = message.from_user.id
       if message.chat.type == enums.ChatType.PRIVATE:
         return await message.reply("`This Command work Only In Groups!`")
       elif (await is_admin(chat_id,user_id)) == False or user_id not in config.DEVS:
            return await message.reply("`Admins Only!`")
       elif (await can_promote_members(chat_id,user_id)) == False or user_id not in config.DEVS:
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


__MODULE__ = "Admin"

__HELP__ = """
**admins only**:

- `/admins`: to know group admins.
- `/purge`: reply to message and bot delete your msg to reply message and also instead all msgs. 
- `/del`: delete a message.
- `/promote`: promote a member to admin.
- `/mpromote`: medium promote a member to admin.
- `/fpromote`: full promote a member to admin.
- `/demote`: demote a admin to member.
- `/setgpic`: set group profile photo.
- `/setgtitle`: set group title.
- `/setgdesc`: set group description.
"""
