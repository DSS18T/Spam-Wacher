from pyrogram.types import InputMediaPhoto, InputMediaVideo
from Nandha import Nandha
from pyrogram import filters



URL = (
"https://telegra.ph/file/24ed9f2ebe33bb03a8a5b.mp4",
"https://telegra.ph/file/1b9ec1c2e0ee9b5e1d8a9.mp4",
"https://telegra.ph/file/4e7422366b53f659d8c0d.mp4",
"https://telegra.ph/file/a46ae89eda709764f1530.jpg",
)

@Nandha.on_message(filters.command("test"))
async def tests(_, m):
   for link in URL:
      await Nandha.send_media_group(m.chat.id,
    [
        InputMediaPhoto(link),
        InputMediaPhoto(link, caption="test 1"),
    ]
)
