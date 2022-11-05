import config
import asyncio
from Nandha import Nandha
from pyrogram import filters

@Nandha.on_message(filters.command("pfp",config.CMDS))
async def user_profiles(_, message):
       user_id = message.from_user.id
       reply = message.reply_to_message
       try:
          if reply: uid = reply.from_user.id
          elif not reply: uid = user_id
          msg = await message.reply_text("`Check My Private I'm Sending Photos You Requested!`")
          x = 0
          async for photo in Nandha.get_chat_photos(uid):
               x += +1
               msg = await Nandha.send_photo(user_id, photo.file_id)
               await asyncio.sleep(3)
          await Nandha.send_message(user_id, f"**total profiles I have sent**: `{x}`",reply_to_message_id=msg.id)
       except Exception as e:
             return await message.reply(e)
