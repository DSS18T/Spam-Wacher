from Nandha import mongodb

rulesdb = mongodb.RULES 



def addrules(chat_id: int, text: str):
    if chat_id in get_chat():
      return
    RULES = {"_id": chat_id, "rules": text}
    return rulesdb.insert_one(RULES)
