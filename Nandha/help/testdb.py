
from Nandha import mongodb

db = mongodb["FUCK"]


def is_db(chat_id: int):
    x = db.find_one({"chat_id": chat_id})
    if x:
       return True
    return False

def ai_on(chat_id: int):
    format = {"chat_id": chat_id, "chatbot": "on"}
    db.insert_one(format)

def ai_off(chat_id: int):
    if is_db:
       db.update_one({"chat_id": chat_id},{"$set":{"chatbot": "off"}})
        
def get_chats(chat_id: int):
    chats = []
    for i in db.find():
       chats.append(i["chat_id"])
    return chats
