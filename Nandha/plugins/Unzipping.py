
import config
import os
import asyncio
from Nandha import Nandha
from pyrogram import filters
from zipfile import ZipFile


@Nandha.on_message(filters.private & filters.command("unzip",config.CMDS))
async def unzipping (_ , message):
       unzip_path = "zipfiles/{}".format(message.from_user.id)
       reply = message.reply_to_message
       if reply.document and reply.document.file_name.endswith(".zip"):
            x = await message.reply_text("Zip file downloading...")
            path = await message.reply_to_message.download()
            with ZipFile(path, "r") as zip:
                   zip.extractall(unzip_path)
            await x.edit("Successfully Unzipped Your Zip File (:")
            await x.edit("Uploading...")
            for file in os.listdir(unzip_path):
                    await message.reply_documemt(document=unzip_path+"/"+file)
                    asyncio.sleep(2)
            await x.edit("done! thanks for using Me!")            
       return await message.reply_text("Only Extract Zip Files!")
