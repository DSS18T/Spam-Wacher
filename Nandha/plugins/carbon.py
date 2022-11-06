import os
import cv2
import config
from Nandha import (
Nandha, session )
from io import BytesIO
from pyrogram import filters 


async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with session.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image



@Nandha.on_message(filters.command(["cb","carbon"],config.CMDS))
async def make_carbon_image(_, message):
      reply = message.reply_to_message
      if reply and reply.text or reply and reply.caption:
           text = reply.text or reply.caption
      elif not reply and len(message.text.split()) >1:
           text = message.text.split(None,1)[1]
      else: return await message.reply("`Reply to text or give a text to make carbon!`")
      msg = await message.reply("`Please Wait!`")
      carbon = await make_carbon(text)
      await message.reply_photo(carbon)
      await msg.delete()

@Nandha.on_message(filters.command("bw",config.CMDS))
async def black_white(client: Nandha, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "black_white.jpg"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                "Downloading image", quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit("Processing Image...")
            image_file = cv2.imread(a)
            grayImage = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(edit_img_loc, grayImage)
            await message.reply_chat_action("upload_photo")
            await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
            await msg.delete()
        else:
            await message.reply_text("Why did you delete that??")
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("black_white-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    "Something went wrong!", quote=True
                )
            except Exception:
                return

