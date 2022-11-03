from Nandha import mongodb


db = mongodb.WARNNING

def add_warn(user_id: int, reason):
    if not user_id in warn_users():
        db.insert_one({"user_id":user_id, "warn":1, "reason": reason})
    x = db.find_one({"user_id":user_id})
    warns = int(x["warn"])+1
    x = {"user_id":user_id,{"$set":{"warn":warns,f"reason {warns}":reason}})
    db.update_one(x)
