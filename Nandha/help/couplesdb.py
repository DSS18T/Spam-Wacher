from Nandha import mongodb
from Nandha import Nandha
coupledb = mongodb.COUPLEDB


def get_chats():
    chats = []
    for chat in coupledb.find():
        chats.append(chat["_id"])
        return chats
    return chats
   

async def get_couple(chat_id: int):
    couples = coupledb.find_one({"_id": chat_id})
    if couples:
         men = (await Nandha.get_users(couples["men"])).mention
         women = (await Nandha.get_users(couples["women"])).mention
         text = f"""
**Couples of the Day!**

**Men**: {men}
**Women**: {women}

**New Couples Change 24 hours!**
"""
         return text

def save_couple(chat_id: int, date, men, women):
      COUPLES = {"_id":chat_id,"date":date,"men":men,"women":women}
      coupledb.insert_one(COUPLES)



async def check_couple(chat_id: int, date, men, women):
     couples = coupledb.find_one({"_id": chat_id})
     if couples["date"] == date:
         return await get_couple(chat_id)
     else:
         coupledb.update_one({"_id":chat_id},{"$set":{"date": date, "men":men, "women":women}})
         return await get_couple(chat_id)
             
