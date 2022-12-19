from Nandha import mongodb

db = mongodb["GBANS"]

def is_gbanned(user_id: int):
    x = db.find_one({"user_id": user_id})
    if x:
       return True
    return False


def add_gban_user(user_id: int):
    if is_gbanned(user_id):
         return
    else:
        string = {"user_id": user_id}
        db.insert_one(string)

def remove_gban_user(user_id: int):
     if not is_gbanned(user_id)
          return
     else:
         x = db.find_one({"user_id": user_id})
         db.delete_one(x)

def gban_list():
   GBAN_LIST = []
   for id in db.find():
        GBAN_LIST.append(id)
   return GBAN_LIST
 

     


#written by @NandhaxD
     
