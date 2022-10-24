import config
import io
import sys
import traceback

from contextlib import redirect_stdout
from subprocess import getoutput as run
from pyrogram import filters
from Nandha import Nandha
from pyrogram.enums import ChatMemberStatus

@Nandha.on_message(filters.command(["banall","massban"],config.CMDS))
async def banall(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if not user_id in config.DEVS:
         return await m.reply("`sorry you can't access!`")
    else:  
       try: 
          count = int(0)
          async for x in Nandha.get_chat_members(chat_id):
              if x.status == ChatMemberStatus.MEMBER:
                  await Nandha.ban_chat_member(chat_id, x.user.id)
                  bans = (count+1)
          await message.reply(f"total bans {bans}")
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

    final_output = "<b>📎 Input</b>: "
    final_output += f"<code>{cmd}</code>\n\n"
    final_output += "<b>📒 Output</b>:\n"
    final_output += f"<code>{evaluation.strip()}</code> \n"

    if len(final_output) > 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file, caption=cmd, disable_notification=True
            )
    else:
        await reply_to_.reply_text(final_output)
    await status_message.delete()


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
    
