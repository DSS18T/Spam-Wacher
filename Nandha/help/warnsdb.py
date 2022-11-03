from Nandha import mongodb


db = mongodb.WARNNING

def warn_users():
    warn_users = []
    for x in db.find():
       append(x["user_id"])
    return warn_users

def add_warn(user_id: int, reason):
    if not user_id in warn_users():
        db.insert_one({"user_id":user_id, "warn":1, "reason": reason})
    x = db.find_one({"user_id":user_id})
    warns = int(x["warn"])+1
    db.update_one({"user_id":user_id},{"$set":{"warn":warns,f"reason {warns}":reason}})
    
