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
        total = count+1
    text = f"""
**Here The [Repository](https://github.com/NandhaxD/VegetaRobot)**
**Here The [SupportGroup](t.me/VegetaSupport)**

```----------------
| Contributors in Vegeta |
----------------```
{list_of_users}

**total Contributors {total}**"""
    await m.reply(text=text, disable_webpage_preview=True)
