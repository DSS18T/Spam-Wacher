from Nandha import mongodb

chatbotdb = mongodb.CHATBOT 

def addchat(chat_id: int):
    chatbotdb.insert_one({"chat_id": chat_id})

def removechat(chat_id: int):
    x = chatbotdb.find_one({"chat_id": chat_id})  
    chatbotdb.delete_one(x)

def is_chat(chat_id: int):
     x = chatbotdb.find_one({"chat_id": chat_id}) 
     if x:
        return True
     return False 

def get_chat():
     chats = []
     for chats in chatbotdb.find():
          chats.append(chats["chat_id"])
     return chats
