from Nandha import mongodb

coupledb = mongodb.COUPLEDB


def get_couple(chat_id: int):
    couples = coupledb.find_one({"_id": chat_id})
    if couples:
         return couples["couple"] 
    return {}

def save_couple(chat_id: int, date, couples):
      COUPLES = {"_id":chat_id, "date":date, "couple": couples}
      coupledb.insert_one(COUPLES)
      
