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



DAY = ["good morning","good afternoon","good night"]


GM_TEXT = """
🤗 **Hi and good morning {}**,
we have nice quote for this morning!

**quote**: {}

**this is {} and date {}
my wish's for you have good day!
"""

@Nandha.on_message(filters.regex(DAY))
async def day(_, message):
    part = await get_part_of_day(datetime.now().hour)
    if part == "morning":
           api = requests.get("https://api.waifu.pics/sfw/smile").json()
           url = api["url"]
           quote = "somthin"
           day = datetime.now()
           dayname = ok.strftime("%A")
           date = f"{day.day}-{day.month}-{day.year}"
           mention = message.from_user.mention
           await message.reply_animation(url,caption=GM_TEXT.format(
            mention,quote,dayname,date))





