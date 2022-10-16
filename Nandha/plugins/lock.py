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


