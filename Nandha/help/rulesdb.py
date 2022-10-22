from Nandha import mongodb

rulesdb = mongodb.RULES 



def addrules(chat_id: int, text: str):
    RULES = {"_id": chat_id, "rules": text}
    return rulesdb.insert_one(RULES)
