from Nandha import mongodb

coupledb = mongodb.COUPLEDB


def get_chats():
    chats = []
    for chat in coupledb.find():
        chats.append(chat["_id"])
        return chats
    return chats
   

def get_couple(chat_id: int):
    couples = coupledb.find_one({"_id": chat_id})
    if couples:
         return couples["couple"] 
    return {}

def save_couple(chat_id: int, date, couples):
      COUPLES = {"_id":chat_id, "date":date, "couple": couples}
      coupledb.insert_one(COUPLES)



def check_couple(chat_id: int, date, couple):
     couples = coupledb.find_one({"_id": chat_id})
     if couples["date"] == date:
         return get_couple(chat_id)
     else:
         coupledb.update_one({"_id": chat_id},{"$set":{"date": date, "couple":couple}})
         return get_couple(chat_id)
             
