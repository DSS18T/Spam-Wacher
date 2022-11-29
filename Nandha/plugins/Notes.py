import config

from Nandha import mongodb, Nandha
from pyrogram import filters
from pyrogram.types import *

db = mongodb["NOTES"]

@Nandha.on_message(filters.command("save",config.CMDS))
async def save(_, message):
     reply = message.reply_to_message
     chat_id = message.chat.id
     user_id = message.from_user.id
     if message.chat.type == enums.ChatType.PRIVATE: return await message.reply_text("Commands Work Only On Groups!")
     try: note_name = message.text.split(None,1)[1]
     except: return await message.reply_text("Give Note Name To Save!")
     if reply and reply.text:
          db.insert_one({"chat_id": chat_id, "note_name": note_name, "text": reply.text})
     elif reply and reply.video:
          if reply.caption:
               caption = reply.caption
          else: caption = ""
          db.insert_one({"chat_id": chat_id, "note_name": note_name, "video": reply.video.file_id, "caption": caption})
     elif reply and reply.document:
          if reply.caption:
               caption = reply.caption
          else: caption = ""
          db.insert_one({"chat_id": chat_id, "note_name": note_name, "document": reply.document.file_id, "caption": caption})
     elif reply and reply.animation:
          if reply.caption:
               caption = reply.caption
          else: caption = ""
          db.insert_one({"chat_id": chat_id, "note_name": note_name, "animation": reply.animation.file_id, "caption": caption})
     elif reply and reply.photo:
          if reply.caption:
               caption = reply.caption
          else: caption = ""
          db.insert_one({"chat_id": chat_id, "note_name": note_name, "photo": reply.photo.file_id, "caption": caption})
     return await message.reply_text("Added! `#{}`".format(note_name))

@Nandha.on_message(filters.regex("^#")
async def get_notes(_, message):
     chat_id = message.chat.id
     if message.chat.type == enums.ChatType.PRIVATE: return await message.reply_text("Commands Work Only On Groups!")
     try: note_name = message.text.split("#")[1].strip()
     x = db.find_one({"chat_id": chat_id, "note_name": note_name})
     if bool(x):
          if bool(x["video"]):
                video = x["video"]
                caption = x["caption"]
                await message.reply_video(video=video, caption=caption)



