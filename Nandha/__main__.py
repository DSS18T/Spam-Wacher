
import config
from Nandha import Nandha
from pyrogram import filters


@Nandha.on_message(filters.command("start",config.CMDS))
async def start(_, message):
     await message.reply("`SpamWatcher System Alive!`")

if __name__ == "__main__":
    Nandha.run()

