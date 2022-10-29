from Nandha import mongodb

db = mongodb.TRUST





def get_trust_users():
    TRUST_USERS = []
    for x in db.find():
       TRUST_USERS.append(x["_id"])
       return TRUST_USERS
    return TRUST_USERS
     

def get_trust(user_id: int):
    if user_id in get_trust_users():
        x = db.find_one({"_id": user_id})
        trust = x["trust"]
        return trust
    else: return 0


def add_trust(user_id: int):
     if user_id in get_trust_users():
          x = db.find_one({"_id": user_id})
          trust = int(x["trust"])+1
          db.update_one({"_id": user_id},{"$set":{"trust":trust}})
     else:  
        x = {"_id":user_id, "user_id":user_id, "trust":1}
        db.insert_one(x)
       
