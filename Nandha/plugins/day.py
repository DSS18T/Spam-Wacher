import requests
import random

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


GM_TEXT = [
"Let your morning be the start of your new life. Do your best and forget about the rest. Good morning!",
"Good morning, wake up. Start fresh and see the beautiful opportunity in each day. Wish you all the very best!",
"Whenever you find yourself in doubt about how far you can go, just remember how far you have come. Stay positive and always have faith in yourself. Good morning!",
"Keep moving on in life. Everything you need will come to you at a perfect time. Just believe in yourself and keep doing hard work. Good morning!",
"Good morning sunshine, waking up with your beautiful smile makes my day extraordinary.",
"Good morning to the beautiful soul, your positive energy makes me enthusiastic, thank you, love!",
"Can't wait for the day when you wake up next to me, good morning sweetheart!",
"Good morning to my world, may you have a positive day and find solutions to all your problems.",
"It's the best morning when you wake up next to me, good morning love!",
"Good morning darling, the warmth of your hugs and love makes me special every day!",
"I don't need an alarm when I have you, you are my snooze-buster. Good morning love!",]

GN_TEXT = [
"I hope God blesses you with many more peaceful nights. Good night, dear.",
"When your day gets tough, remember that tomorrow is a fresh day after your sleep. Good night.",
"Good night, my one and only. I wish I could hold you in my arms right now as I go to sleep.",
"May the stars and moonlight shine brightly on your night. Have a good night.",
"Have a good night, friend. May you have a restful and pleasant night’s sleep tonight.",
"No matter how bad the day was, always try to end it with positive thoughts. Try to focus on the next day and hope for a sweet dream. Good night.",
"You have so many reasons to thank God, but first thank him for such a peaceful night like this. What a blissful night for a good sleep. Good night!",
"I don’t need anything else to warm me up as long as you love me. Because the warmth of your love is all I need. Good night!",
"Do you know when an ordinary dream becomes a sweet dream? When someone as sweet as you is present in it. Good night! Please come and make my dreams sweeter!",
"Good night dear. Tomorrow, you are going to have a great day. Just make sure your body is prepared to take on the challenges of tomorrow. Sleep well!",
"A new morning is waiting for you. Sleep well and sleep tight. Because the new day wants you to be fit and all charged up. Good night!",]


TEXT = """
🤗 **Hi and good {} 
{}**, **we have nice quote for this {}!**

**quote**:
{}

**this is {} and date 
{} my wish's for you have good day today!**
"""

@Nandha.on_message(group=20)
async def day(_, message):
    part = await get_part_of_day(datetime.now().hour)
    if message.text in ("good morning","good night","good afternoon"):
           api = requests.get("https://api.waifu.pics/sfw/smile").json()
           url = api["url"]
           if message.text in "good morning":
                 quote = random.choice(GM_TEXT)
           elif message.text in "good night":
                 quote = random.choice(GN_TEXT)
           elif message.text in "good afternoon":
                 qoute = "good afternoon qoute"
           day = datetime.now()
           dayname = day.strftime("%A")
           date = f"{day.day}-{day.month}-{day.year}"
           mention = message.from_user.mention
           await message.reply_animation(url,caption=TEXT.format(
            part,mention,part,quote,dayname,date))





