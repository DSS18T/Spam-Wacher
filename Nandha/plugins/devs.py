import config

from subprocess import getoutput as run
from pyrogram import filters
from Nandha import Nandha



@Nandha.on_message(filters.command("sh",config.CMDS))
async def sh(_, message):
    if message.from_user.id == config.OWNER_ID:
        code = message.text.replace(message.text.split(" ")[0], "")
        x = run(code)
        await message.reply(
            f"**SHELL**: `{code}`\n\n**OUTPUT**:\n`{x}`")
    else:
        await message.reply("`Only Devs can Access this command!`")
