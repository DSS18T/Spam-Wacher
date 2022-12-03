
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
            filename = reply.document.file_name.split(".zip")[0]
            with ZipFile(path, "r") as zip:
                   zip.extractall(unzip_path)
            await x.edit("Successfully Unzipped Your Zip File (:")
            await x.edit("Uploading...")
            for file in os.listdir(f"{unzip_path}/{filename}"):
                try:
                   await message.reply_text(f"{unzip_path}/{filename}/{file}")
                   await asyncio.sleep(2)
                except: pass
            await x.edit("done! uploading join @NandhaBots") 
            return os.system(f"rm -rf {unzip_path}")           
       return await message.reply_text("Only Extract Zip Files!")
