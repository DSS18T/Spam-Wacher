import config

from Nandha import mongodb, Nandha
from pyrogram import filters
from pyrogram.types import *
from pyrogram import enums
from Nandha.help.admin import *

db = mongodb["NOTES"]

@Nandha.on_message(filters.command("notes",config.CMDS))
async def notes(_, message):
     chat_id = message.chat.id
     notes = ""
     for note in db.find({"chat_id": chat_id}):
         if bool(note):
               num = note+1
               notes += "**{num}.** `{name}`\n".format(num, name=note["note_name"])
         else: return await message.reply("No Notes Saved Here!")
     return await message.reply_text(notes)

@Nandha.on_message(filters.command("clear",config.CMDS))
async def clear(_, message):
      chat_id = message.chat.id
      try: note_name = message.text.split(None,1)[1]
      except: return await message.reply_text("what I want do clear? tell me note name!")
      x = db.find_one({"chat_id": chat_id, "note_name": note_name})
      if bool(x):
          db.delete_one(x)
          return await message.reply_text(f"Deleted! > `{note_name}` <")
      return await message.reply_text("No Notes In This > `{note_name}` <")

@Nandha.on_message(filters.command("save",config.CMDS))
async def save(_, message):
     reply = message.reply_to_message
     chat_id = message.chat.id
     user_id = message.from_user.id
     if message.chat.type == enums.ChatType.PRIVATE: return await message.reply_text("Commands Work Only On Groups!")
     elif await is_admin(chat_id, user_id) == False: return await message.reply_text("Admins Only Can Save Notes!")
     try: note_name = message.text.split(None,1)[1].lower()
     except: return await message.reply_text("Give Note Name To Save!")
     if reply and reply.text:
          db.insert_one({"chat_id": chat_id, "note_name": note_name, "text": reply.text, "type": "text"})
     elif reply and reply.video:
          if reply.caption:
               caption = reply.caption
          else: caption = ""
          db.insert_one({"chat_id": chat_id, "note_name": note_name, "video": reply.video.file_id, "caption": caption, "type": "video"})
     elif reply and reply.document:
          if reply.caption:
               caption = reply.caption
          else: caption = ""
          db.insert_one({"chat_id": chat_id, "note_name": note_name, "document": reply.document.file_id, "caption": caption, "type": "document"})
     elif reply and reply.animation:
          if reply.caption:
               caption = reply.caption
          else: caption = ""
          db.insert_one({"chat_id": chat_id, "note_name": note_name, "animation": reply.animation.file_id, "caption": caption, "type": "animation"})
     elif reply and reply.photo:
          if reply.caption:
               caption = reply.caption
          else: caption = ""
          db.insert_one({"chat_id": chat_id, "note_name": note_name, "photo": reply.photo.file_id, "caption": caption, "type": "photo"})
     return await message.reply_text("Added! `#{}`".format(note_name))

@Nandha.on_message(filters.regex("^#"))
async def get_notes(_, message):
     chat_id = message.chat.id
     if message.chat.type == enums.ChatType.PRIVATE: return await message.reply_text("Commands Work Only On Groups!")
     try: note_name = message.text.split("#")[1].strip()
     except: return await message.reply_text("example: `#test`")
     x = db.find_one({"chat_id": chat_id, "note_name": note_name})
     if bool(x):
          if "video" == x["type"]:
                video = x["video"]
                caption = x["caption"]
                return await message.reply_video(video=video, caption=caption)
          elif "animation" == x["type"]:
                animation = x["animation"]
                caption = x["caption"]
                return await message.reply_animation(animation=animation, caption=caption)
          elif "photo" == x["type"]:
                photo = x["photo"]
                caption = x["caption"]
                return await message.reply_photo(photo=photo, caption=caption)
          elif "document" == x["type"]:
                document = x["document"]
                caption = x["caption"]
                return await message.reply_document(document=document, caption=caption)
          elif "text" == x["type"]:
                text = x["text"]              
                return await message.reply_text(text=text)
          else: return await message.reply_text("can't send this note in >`{}`<".format(note_name))
     else: return await message.reply_text("No notes saved in >`{}`<".format(note_name))


