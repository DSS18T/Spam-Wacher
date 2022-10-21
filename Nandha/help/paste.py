from Nandha.help.aiohttp import post



async def paste(text: str):
     resp = await post(f"https://batbin.me/api/v2/paste", data=text)
     code = resp["message"]
     return f"https://batbin.me/{code}"
