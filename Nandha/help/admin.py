
from Nandha import Nandha

async def is_admin(chat_id: int, user_id: int):
     admin = await Nandha.get_chat_member(chat_id, user_id)
     if admin.privileges:
         return True
     return False

async def can_ban_members(chat_id: int, user_id: int):
     admin = await Nandha.get_chat_member(chat_id, user_id)
     if admin.privileges.can_restrict_members:
         return True
     return False

async def can_promote_members(chat_id: int, user_id: int):
     admin = await Nandha.get_chat_member(chat_id, user_id)
     if admin.privileges.can_promote_members:
         return True
     return False

async def can_promote_members(chat_id: int, user_id: int):
     admin = await Nandha.get_chat_member(chat_id, user_id)
     if admin.privileges.can_promote_members:
         return True
     return False

async def can_change_info(chat_id: int, user_id: int):
     admin = await Nandha.get_chat_member(chat_id, user_id)
     if admin.privileges.can_change_info:
         return True
     return False



