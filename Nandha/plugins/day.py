import requests

from Nandha import Nandha
from pyrogram import filters

from datetime import datetime

async def get_part_of_day(h):
    return (
        "morning"
        if 5 <= h <= 11
        else "afternoon"
        if 12 <= h <= 17
        else "evening"
        if 18 <= h <= 22
        else "night"
    )



GM_TEXT = """
🤗 **Hi and good {} {}**,
we have nice quote for this {}!

**quote**: {}

**this is {} and date {}
my wish's for you have good day!
"""

@Nandha.on_message(group=20)
async def day(_, message):
    part = await get_part_of_day(datetime.now().hour)
    if message.text in ("good morning","good night","good afternoon"):
           api = requests.get("https://api.waifu.pics/sfw/smile").json()
           url = api["url"]
           if message.text in "good morning":
                 quote = "good morning quote"
           elif message.text in "good night":
                 quote = "good night quote"
           elif message.text in "good afternoon":
                 qoute = "good afternoon qoute"
           day = datetime.now()
           dayname = day.strftime("%A")
           date = f"{day.day}-{day.month}-{day.year}"
           mention = message.from_user.mention
           await message.reply_animation(url,caption=GM_TEXT.format(
            part,mention,part,quote,dayname,date))





