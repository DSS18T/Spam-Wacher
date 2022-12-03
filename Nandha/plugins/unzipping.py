
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
       if reply.document and reply.document.file_name.endswith(".zip"):
            x = await message.reply_text("Zip file downloading...")
            path = await message.reply_to_message.download()
            filename = reply.document.file_name.split(".zip")[0]
            with ZipFile(path, "r") as zip:
                   zip.extractall(unzip_path)
            await x.edit("Successfully Unzipped Your Zip File (:")
            await x.edit("Uploading...")
            fail = 0
            for file in os.listdir(f"{unzip_path}/{filename}"):
                try:
                   await message.reply_document(f"{unzip_path}/{filename}/{file}")
                except:
                   try:
                      for name in os.listdir(f"{unzip_path}/{filename}/{file}"):
                          await message.reply_document(f"{unzip_path}/{filename}/{file}/{name}") 
                   except: fail += 1            
            await x.edit(f"done! uploading join @NandhaBots - fail {fail}") 
            return os.system(f"rm -rf {unzip_path}")           
       return await message.reply_text("Only Extract Zip Files!")
