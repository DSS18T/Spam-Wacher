
from Nandha import Nandha

async def is_admin(chat_id: int, user_id: int):
     admin = await Nandha.get_chat_member(chat_id, user_id)
     if admin.privileges:
         return True
     return False
