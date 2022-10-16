import config

from pyrogram import filters
from pyrogram.types import *
from Nandha import Nandha
from Nandha.help.admin import *
from pyrogram.errors import (
ChatNotModified )


@Nandha.on_message(filters.command("lock",config.CMDS))
async def lock(_, message):
      chat_id = message.chat.id
      user_id = message.from_user.id
      try:
          if (await is_admin(chat_id,user_id)) == True:
                 
                if (await is_admin(chat_id,config.BOT_ID)) == False:
                       return await message.reply("`Make you Sure I'm Admin!`")
                if len(message.text.split()) <2:
                       return await message.reply("`No input found!`")

                lock_type = message.text.split()[1]

                get_perm = message.chat.permissions

                msg = get_perm.can_send_messages
                media = get_perm.can_send_media_messages
                webprev = get_perm.can_add_web_page_previews
                polls = get_perm.can_send_polls
                info = get_perm.can_change_info
                invite = get_perm.can_invite_users
                pin = get_perm.can_pin_messages
                stickers = animations = games = inlinebots = None
                if lock_type in ("msg","all"):
                    msg = False
                    perm = "messages"

                elif lock_type == "media":
                     media = False
                     perm = "audios, documents, photos, videos, video notes, voice notes"

                elif lock_type == "stickers":
                    stickers = False
                    perm = "stickers"

                elif lock_type == "animations":
                     animations = False
                     perm = "animations"

                elif lock_type == "games":
                     games = False
                     perm = "games"

                elif lock_type in ("inlinebots", "inline"):
                     inlinebots = False
                     perm = "inline bots"

                elif lock_type == "webprev":
                     webprev = False
                     perm = "web page previews"

                elif lock_type == "polls":
                      polls = False
                      perm = "polls"

                elif lock_type == "info":
                      info = False
                      perm = "info"

                elif lock_type == "invite":
                      invite = False
                      perm = "invite"

                elif lock_type == "pin":
                     pin = False
                     perm = "pin"
                else:
                     return await message.reply("`Invalid locktype!`")
                await Nandha.set_chat_permissions(
                chat_id,
                ChatPermissions(
                can_send_messages=msg,
                can_send_media_messages=media,
                can_send_other_messages=any([stickers, animations, games, inlinebots]),
                can_add_web_page_previews=webprev,
                can_send_polls=polls,
                can_change_info=info,
                can_invite_users=invite,
                can_pin_messages=pin,),)
                await message.reply_text(f"`locked! {lock_type}`")
                              
          else:
              await message.reply_text("`Admins Only!`")
      except ChatNotModified:         
           await message.reply(f"`already locked! {lock_type}`")


@Nandha.on_message(filters.command("unlock",config.CMDS))
async def unlock(_, message):
        chat_id = message.chat.id
        user_id = message.from_user.id
        try:
            if (await is_admin(chat_id,user_id)) == True:
                  if (await is_admin(chat_id,config.BOT_ID)) == False:
                       return await message.reply("`Make you Sure I'm Admin!`")
                  if len(message.text.split()) <2:
                       return await message.reply("`No input found!`")
                  unlock_type = message.text.split()[1]
                  if unlock_type == "all":
                       await Nandha.set_chat_permissions(
                       chat_id,
                       ChatPermissions(
                       can_send_messages=True,
                       can_send_media_messages=True,
                       can_send_other_messages=True,
                       can_add_web_page_previews=True,
                       can_send_polls=True,
                       can_change_info=False,
                       can_invite_users=True,
                       can_pin_messages=False),)
                       return await message.reply(f"`locked! {unlock_type}`")
                  get_uperm = m.chat.permissions
                  umsg = get_uperm.can_send_messages
                  umedia = get_uperm.can_send_media_messages
                  uwebprev = get_uperm.can_add_web_page_previews
                  upolls = get_uperm.can_send_polls
                  uinfo = get_uperm.can_change_info
                  uinvite = get_uperm.can_invite_users
                  upin = get_uperm.can_pin_messages
                  ustickers = uanimations = ugames = uinlinebots = None
                  if unlock_type == "msg":
                         umsg = True
                         uperm = "messages"

                  elif unlock_type == "media":
                         umedia = True
                         uperm = "audios, documents, photos, videos, video notes, voice notes"

                  elif unlock_type == "stickers":
                        ustickers = True
                        uperm = "stickers"

                  elif unlock_type == "animations":
                        uanimations = True
                        uperm = "animations"

                  elif unlock_type == "games":
                       ugames = True
                       uperm = "games"

                  elif unlock_type in ("inlinebots", "inline"):
                         uinlinebots = True
                         uperm = "inline bots"

                  elif unlock_type == "webprev":
                         uwebprev = True
                         uperm = "web page previews"

                  elif unlock_type == "polls":
                       upolls = True
                       uperm = "polls"

                  elif unlock_type == "info":
                       uinfo = False
                       uperm = "info"

                  elif unlock_type == "invite":
                       uinvite = True
                       uperm = "invite"

                  elif unlock_type == "pin":
                        upin = False
                        uperm = "pin"

                  else:
                      await message.reply("`Invalid locktypes!`")      
                  await Nandha.set_chat_permissions(
                   chat_id,
                   ChatPermissions(
                   can_send_messages=umsg,
                   can_send_media_messages=umedia,
                   can_send_other_messages=any(
                     [ustickers, uanimations, ugames, uinlinebots],),
                   can_add_web_page_previews=uwebprev,
                   can_send_polls=upolls,
                   can_change_info=uinfo,
                   can_invite_users=uinvite,
                   can_pin_messages=upin,))
                  await message.reply(f"`locked! {unlock_type}`")


            else:
                await message.reply("`Admins Only!`")
        except Exception as e:
              await message.reply(e)


LOCKS = """
• `{} 
following permissions:`

**messages**: {}
**media_messages**: {}
**other_messages**: {}
**web_page_previews**: {}
**send_polls**: {}
**change_info**: {}
**invite_users**: {}
**pin_messages**: {}
"""

@Nandha.on_message(filters.command("locks",config.CMDS))
async def locks(_, message):
     chat_id = message.chat.id
     user_id = message.from_user.id
     try:
         if (await is_admin(chat_id,user_id)) == True:

                if (await is_admin(chat_id,config.BOT_ID)) == False:
                       return await message.reply("`Make you Sure I'm Admin!`")

                v_perm = message.chat.permissions   
            
                async def convert_to_emoji(val: bool):
                     return "✅" if val else "❌"

                vmsg = await convert_to_emoji(v_perm.can_send_messages)
                vmedia = await convert_to_emoji(v_perm.can_send_media_messages)
                vother = await convert_to_emoji(v_perm.can_send_other_messages)
                vwebprev = await convert_to_emoji(v_perm.can_add_web_page_previews)
                vpolls = await convert_to_emoji(v_perm.can_send_polls)
                vinfo = await convert_to_emoji(v_perm.can_change_info)
                vinvite = await convert_to_emoji(v_perm.can_invite_users)
                vpin = await convert_to_emoji(v_perm.can_pin_messages)
                if v_perm is not None:
                    await message.reply_text(LOCKS.format(
                        message.chat.title, vmsg, vmedia, vother, vwebprev, vpolls, vinfo, vinvite, vpin))
         else:
            await message.reply("`Admins Only!`")
     except Exception as e:
         await message.reply(e)


@Nandha.on_message(filters.command("locktypes",config.CMDS))
async def locktypes(_, message):
     if (await is_admin(message.chat.id, message.from_user.id)) == True:
          await message.reply_text(
        (
            "**Lock Types:**\n"
            " - `all` = Everything\n"
            " - `msg` = Messages\n"
            " - `media` = Media, such as Photo and Video.\n"
            " - `polls` = Polls\n"
            " - `invite` = Add users to Group\n"
            " - `pin` = Pin Messages\n"
            " - `info` = Change Group Info\n"
            " - `webprev` = Web Page Previews\n"
            " - `inlinebots`, `inline` = Inline bots\n"
            " - `animations` = Animations\n"
            " - `games` = Game Bots\n"
            " - `stickers` = Stickers")
     ,)
     else:
        await message.reply_text("`Admins Only!`")


