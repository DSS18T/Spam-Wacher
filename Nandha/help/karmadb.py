from Nandha import mongodb

db = mongodb.KARMA

def get_chat():
    chat = []
    for x in db.find():
       chat.append(x["chat_id"])
    return chat

def is_karma_chat(chat_id: int):
     if chat_id in get_chat():
        x = db.find_one({"chat_id": chat_id})
        y = x["karma"]
        if y == "on":
          return "on"
        elif y == "off":
           return "off"
     else: return False

def on_karma(chat_id: int):
       if not chat_id in get_chat():
          x = {"chat_id": chat_id,"karma": "on"}
          db.insert_one(x)
       else:
          db.update_one({"chat_id": chat_id},{"$set":{"karma": "on"}})

def off_karma(chat_id: int):
       if not chat_id in get_chat():
          x = {"chat_id": chat_id,"karma": "off"}
          db.insert_one(x)
       else:
          db.update_one({"chat_id": chat_id},{"$set":{"karma": "off"}})

def get_karma_users():
    KARMA_USERS = []
    for x in db.find():
       KARMA_USERS.append(x["_id"])
    return KARMA_USERS
     

def get_karma(user_id: int):
    if user_id in get_karma_users():
        x = db.find_one({"_id": user_id})
        karma = x["karma"]
        return karma
    return "No Karma"

def remove_karma(user_id: int):
     if not user_id in get_karma_users():
          return
     x = db.find_one({"_id": user_id})
     karma = int(x["karma"])-1
     db.update_one({"_id": user_id},{"$set":{"karma":karma}})

def add_karma(user_id: int):
     if not user_id in get_karma_users():
          x = {"_id":user_id,"karma":1}
          db.insert_one(x)
     else:
        x = db.find_one({"_id": user_id})
        karma = int(x["karma"])+1
        db.update_one({"_id": user_id},{"$set":{"karma":karma}})
     
       
