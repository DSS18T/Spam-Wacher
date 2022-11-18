import config

from Nandha import UB
from pyrogram import filters


@UB.on_message(filters.command("add",config.CMDS))
async def mass_add(_, message):
       chat = message.chat
       try: from_chat_id = message.text.split()[1]
       except: return await message.reply("/add chat_id")
       members = []
       async for m in UB.get_chat_members(from_chat_id):
            members.append(m.user.id)
       try: await UB.add_chat_members(chat.id, members)
       except: pass
