import config
from pyrogram import filters
from Nandha import Nandha, session



async def get(url: str, *args, **kwargs):
    async with session.get(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data

@Nandha.on_message(filters.command("repo",config.CMDS))
async def repo(_, m):
    users = await get("https://api.github.com/repos/NandhaxD/VegetaRobot/contributors")
    list_of_users = ""
    count = 1
    for user in users:
        list_of_users += (f"**{count}.** [{user['login']}]({user['html_url']})\n")
        count += 1
    text = f"""[Github](https://github.com/NandhaxD/VegetaRobot) | [Group](t.me/VegetaSupport)
```----------------
| Contributors |
----------------```
{list_of_users}"""
    await m.reply(text=text)
