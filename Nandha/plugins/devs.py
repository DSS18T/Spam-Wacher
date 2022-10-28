import config
import io
import sys
import traceback

from contextlib import redirect_stdout
from subprocess import getoutput as run
from pyrogram import filters
from Nandha import Nandha
from Nandha.help.paste import spacebin
from Nandha.help.couplesdb import get_chats as couples_chats
from Nandha.help.rulesdb import rules_chat as rules_chats
from Nandha.help.chatbotdb import get_chat ad chatbot_chats
from datetime import datetime
from pyrogram.enums import (
ChatMemberStatus, ChatMembersFilter)


@Nandha.on_message(filters.command("stats",config.CMDS))
async def stats(_, message):
     user_id = message.from_user.id
     if not user_id in config.DEVS:
         return await message.reply("`You Don't Have Enough Rights to Do This!`")
     else: couples_chats = len(await couples_chats())
     rules_chats = len(rules_chats())
     chatbot_chats = len(chatbot_chats())
     stats = (
         "**Stats Info**\n:
         f"**Rules Chats**: `{rules_chats}`\n"
         f"**Couples chats**: `{couples_chats}`\n"
         f"**Chatbot Chats**: `{chatbot_chats}`\n")
     await message.reply(stats)
     

@Nandha.on_message(filters.command("logs",config.CMDS))
async def logs(_, message):
     if message.from_user.id in config.DEVS:
          try:
            logs = run("tail logs.txt")
            paste = await spacebin(logs)
            msg = await message.reply("uploading...")
            await message.reply_document("logs.txt",caption="**Paste**: {}".format(paste))
            await msg.delete()
          except Exception as e:
              await msg.edit(e)
     else:
        await message.reply("`You Don't have Enough Rights to Run This!`")

@Nandha.on_message(filters.command(["unbanall","massunban"],config.CMDS))
async def unbanall(_, message):
     user_id = message.from_user.id
     chat_id = message.chat.id
     if not user_id in config.DEVS:
          return await message.reply("sorry you can't access!")
     else:
       try:
          users = 0
          async for m in Nandha.get_chat_members(chat_id, filter=ChatMembersFilter.BANNED):
                 await Nandha.unban_chat_member(chat_id,m.user.id)
                 users += 1
          await message.reply(f"**Successfully Unbanned**: `{users}`")
       except Exception as e:
           print(e)
                 

@Nandha.on_message(filters.command(["sbanall","banall","massban"],config.CMDS))
async def banall(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if not user_id in config.DEVS:
         return await message.reply("`sorry you can't access!`")
    else:  
       try: 
          Members = []
          Admins = []
          async for x in Nandha.get_chat_members(chat_id):
              if not x.privileges:
                    Members.append(x.user.id)
              else:
                    Admins.append(x.user.id)
          for user_id in Members:
               if message.text.split()[0].lower().startswith("s"):
                        m = await Nandha.ban_chat_member(chat_id, user_id)
                        await m.delete()
               else:
                   await Nandha.ban_chat_member(chat_id, user_id)
          await message.reply_text("**Successfully Banned**: `{}`\n**Remaining Admins**: `{}`".format(len(Members),len(Admins),))
       except Exception as e:
        print(e)

@Nandha.on_message(filters.command(["skickall","kickall","masskick"],config.CMDS))
async def kickall(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if not user_id in config.DEVS:
         return await message.reply("`sorry you can't access!`")
    else:  
       try: 
          Members = []
          Admins = []
          async for x in Nandha.get_chat_members(chat_id):
              if not x.privileges:
                    Members.append(x.user.id)
              else:
                    Admins.append(x.user.id)
          for user_id in Members:
               if message.text.split()[0].lower().startswith("s"):
                        m = await Nandha.ban_chat_member(chat_id, user_id)
                        await Nandha.unban_chat_member(chat_id, user_id)
                        await m.delete()
               else:
                   await Nandha.ban_chat_member(chat_id, user_id)
                   await Nandha.unban_chat_member(chat_id, user_id)
          await message.reply_text("**Successfully Kicked**: `{}`\n**Remaining Admins**: `{}`".format(len(Members),len(Admins),))
       except Exception as e:
        print(e)

@Nandha.on_message(filters.command("sh",config.CMDS))
async def sh(_, message):
    if not message.from_user.id in config.DEVS:
          return await message.reply_text("`You Don't Have Rights To Run This!`")
    elif len(message.command) <2:
         await message.reply_text("`No Input Found!`")
    else:
          code = message.text.replace(message.text.split(" ")[0], "")
          x = run(code)
          string = f"**📎 Input**: `{code}`\n\n**📒 Output **:\n`{x}`"
          try:
             await message.reply_text(string) 
          except Exception as e:
              with io.BytesIO(str.encode(string)) as out_file:
                 out_file.name = "shell.text"
                 await message.reply_document(document=out_file, caption=e)

async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)

@Nandha.on_message(filters.command(["run","eval"],config.CMDS))
async def eval(client, message):
    if not message.from_user.id in config.DEVS:
         return await message.reply_text("`You Don't Have Enough Rights To Run This!`")
    if len(message.text.split()) <2:
          return await message.reply_text("`Input Not Found!`")
    status_message = await message.reply_text("Processing ...")
    cmd = message.text.split(None, 1)[1]
    start = datetime.now()
    reply_to_ = message
    if message.reply_to_message:
        reply_to_ = message.reply_to_message

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    end = datetime.now()
    ping = (end-start).microseconds / 1000
    final_output = "<b>📎 Input</b>: "
    final_output += f"<code>{cmd}</code>\n\n"
    final_output += "<b>📒 Output</b>:\n"
    final_output += f"<code>{evaluation.strip()}</code> \n\n"
    final_output += f"<b>✨ Taken Time</b>: {ping}<b>ms</b>"
    if len(final_output) > 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file, caption=cmd, disable_notification=True
            )
    else:
        await status_message.edit_text(final_output)


@Nandha.on_message(filters.command("leave",config.CMDS))
async def leave(_, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    reply = message.reply_to_message
    if not user_id in config.DEVS:
        return await message.reply("`You Don't Enough Rights To Do This!`")
    if reply or not reply and len(message.text.split()) <2:
         await message.reply("`I'm leaving here bye buddy's!`")
         await Nandha.leave_chat(chat_id)
    elif reply or not reply and len(message.text.split()) >2:
          return await message.reply("`Give me only chat ID!`")
    elif reply or not reply and len(message.text.split()) == 1:
         await message.reply("`I'm leaving here bye buddy's!`")
         await Nandha.leave_chat(message.text.split()[1])
    

__MODULE__ = "Dev"

__HELP__ = """
developer can access this commnds!
- `/logs`: get bot logs.
- `/leave` or give id : request to leave chat.
- `/run`: run the code.
- `/sh`: shell
- `/unbanall`: unbanall from a group.
- `/massban` or `/sbanall`: ban all user from a group.
- `/kick` or `/skickall`: kick all user from a group.
"""
