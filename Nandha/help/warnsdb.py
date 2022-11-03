from Nandha import mongodb


db = mongodb.WARNNING

def warn_users():
    warn_users = []
    for x in db.find():
       warn_users.append(x["user_id"])
    return warn_users

def add_warn(user_id: int, reason):
    if not user_id in warn_users():
        db.insert_one({"user_id":user_id, "warn":1, "reason 1": reason})
    x = db.find_one({"user_id":user_id})
    warns = int(x["warn"])+1
    db.update_one({"user_id":user_id},{"$set":{"warn":warns,f"reason {warns}":reason}})
    
def remove_warn(user_id: int):
      x = db.find_one({"user_id":user_id})
      db.delete_one(x)

def is_warns(user_id: int):
     if not user_id in warn_users():
         return 0
     x = db.find_one({"user_id":user_id})
     return x["warn"]
