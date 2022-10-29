from Nandha import mongodb

db = mongodb.TRUST


def is_trust_user(user_id: int):
    if user_id in get_trust_users():
       return True
    return False


def get_trust_users():
    TRUST_USERS = []
    for x in db.find():
       TRUST_USERS.append(x["_id"]["user_id"])
       return TRUST_USERS
    return TRUST_USERS
     

def get_trust(user_id: int):
    if is_trust_user == True:
        x = db.find_one({"_id": user_id})
        trust = int(x["_id"]["trust"])
        return trust
    else: return 0


def add_trust(user_id: int):
     if is_trust_user == True:
          x = db.find_one({"_id": user_id})
          trust = int(x["_id"]["trust"])+1
          db.update_one({"_id": user_id},{"$set":{"trust":trust}})
     else:  db.insert_one({"_id": user_id,"user_id": user_id,"trust": 1})
       
