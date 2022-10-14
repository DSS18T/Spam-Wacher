
import config
from Nandha import Nandha
from pyrogram import filters


@Nandha.on_message(filters.command("start",config.CMDS))
async def start(_, message):
     await message.reply("`Group Protection Alive!`")

if __name__ == "__main__":
    Nandha.run()
    with Nandha:
        Nandha.send_message(config.GROUP_ID, "`hello everyone!\nyour group protection system awakened!`")
