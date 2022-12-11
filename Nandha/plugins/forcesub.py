import config
from Nandha import Nandha, mongodb
from pyrogram import filters
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied

db = mongodb.FSUB

@Nandha.on_message(filters.command("fsub"config.CMDS))
async def ForceSubscribe(_, message):
      chat_id = message.chat.id
      bot_id = Nandha.me.id
      if message.text.split()[1] == "on":
           ask = await Nandha.ask(chat_id, 
                  text="okay send me Force Subscribe channel username.", 
                  reply_to_message_id=message.id)
           try:
               Fsub_channel = ask.text
               hmm = await Nandha.get_chat_member(chat_id=Fsub_channel, user_id=bot_id)
           except ChatAdminRequired:
                  return await message.reply_text("I don't have rights to check the user is a member in a channel please make me sure am admin there!")
           except UsernameNotOccupied:
                  return await message.reply_text("Double check channel username the username is invalid!")
           fsub_chat = await Nandha.get_chat(Fsub_channel)
           x = db.find_one({"chat_id": chat_id})
           if x:
              db.update_one({"chat_id": chat_id}, {"$set": {"channel": Fsub_channel}})
           else:
              db.insert_one({"chat_id": chat_id, "fsub": True, "channel": Fsub_channel})          
           return await message.reply_text(f"okay thanks for using and I have now Force Subscribed this group to {fsub_chat.title}")
      elif message.text.split()[1] == "off":
           x = db.find_one({"chat_id": chat_id})
           if x:
               db.delete_one(x)
               return await message.reply_text("okay I have stopped the force subscription!")
           return await message.reply_text("Semms like this chat don't have set any Force subs!")
      else: return await message.reply_text("Format: /fsub on/off")
             
