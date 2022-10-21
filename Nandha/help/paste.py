from Nandha.help.aiohttp import post as bpost

from requests import post as spost

async def batbin(text):
     resp = await bpost(f"https://batbin.me/api/v2/paste", data=text)
     code = resp["message"]
     return f"https://batbin.me/{code}"

async def spacebin(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = spost(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"
