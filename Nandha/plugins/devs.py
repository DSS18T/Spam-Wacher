import config
import io

from subprocess import getoutput as run
from pyrogram import filters
from Nandha import Nandha



@Nandha.on_message(filters.command("sh",config.CMDS))
async def sh(_, message):
    if not message.from_user.id == config.OWNER_ID:
          return await message.reply_text("`You Don't Have Rights To Run This!`")
    elif len(message.command) <2:
         await message.reply_text("`No Input Found!`")
    else:
          code = message.text.replace(message.text.split(" ")[0], "")
          x = run(code)
          string = f"**📎 Input**: `{code}`\n\n**📒 Output **:\n`{x}`"
          if len(code) >4000:
              with io.BytesIO(str.encode(string)) as out_file:
                 out_file.name = "shell.text"
                 await message.reply_document(document=out_file, caption="`LONG TEXT MESSAGE CANNOT SHOW SO WE SEND FILE TYPE.`")
          else:
             await message.reply_text(string) 
               
