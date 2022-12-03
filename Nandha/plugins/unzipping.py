
import config
import os
import asyncio
from Nandha import Nandha
from pyrogram import filters
from zipfile import ZipFile


@Nandha.on_message(filters.command("unzip",config.CMDS))
async def unzipping (_ , message):
       unzip_path = "zipfiles/{}".format(message.from_user.id)
       reply = message.reply_to_message
       if reply and reply.document and reply.document.file_name.endswith(".zip"):
            x = await message.reply_text("Zip file downloading...")
            path = await message.reply_to_message.download()
            with ZipFile(path, "r") as zip:
                   zip.extractall(unzip_path)
            await x.edit("Successfully Unzipped Your Zip File (:")
            await x.edit("Uploading...")
            fail = 0
            for file in os.listdir(f"{unzip_path}"):
                try:
                   await message.reply_document(f"{unzip_path}/{file}")
                except: fail += 1            
            await x.delete()
            if fail == 0: await message.reply_text(f"**Successfully Unzipped!** join @NandhaBots")
            else: await message.reply_text(f"Sorry I couldn't upload {fail} fails! But I have upload some files Enjoy and Join @NandhaBots")
            return os.system(f"rm -rf {unzip_path}")           
       return await message.reply_text("Only Extract Zip Files!")


## made by @NandhaxD
