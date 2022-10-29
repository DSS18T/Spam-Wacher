from Nandha import mongodb

db = mongodb.TRUST


def is_trust_user(user_id: int):
    if user_id in get_trust_users():
       return True
    return False


def get_trust_users():
    TRUST_USERS = []
    for x in db.find():
       TRUST_USERS.append(x["_id"])
       return TRUST_USERS
    return TRUST_USERS
     

def get_trust(user_id: int):
    if is_trust_user == True:
        x = db.find_one({"user_id": user_id})
        trust = int(x["_id"]["trust"])
        return trust
    else: 0


def add_trust(user_id: int):
     if is_trust_user == True:
          x = db.find_one({"user_id": user_id})
          add_one = int(x["_id"]["trust"]) +1
          db.insert_one({"_id": user_id,"user_id": user_id,"turst": add_one})
     else:  db.insert_one({"_id": user_id,"user_id": user_id,"turst": 1})
       
