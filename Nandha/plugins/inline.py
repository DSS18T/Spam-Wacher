from pyrogram import filters
from pyrogram.types import *
from Nandha import Nandha


Nandha_INFO = """
Nandha is my owner
Nandha birth is 2006
Nandha is playboy
Nandha don't have any ambition for his life!
"""

@Nandha.on_inline_query(filters.regex("Nandha"))
async def Nandha(_, query):
     await Nandha.answer_inline_query(
         query.id,
         results = [
           InlineQueryResultArticle(
               "Nandha",
            InputTextMessageContent(Nandha_INFO))])
