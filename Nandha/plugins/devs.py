import config
import io
import sys
import traceback

from contextlib import redirect_stdout
from subprocess import getoutput as run
from pyrogram import filters
from Nandha import Nandha



@Nandha.on_message(filters.command("sh",config.CMDS))
async def sh(_, message):
    if not message.from_user.id == config.OWNER_ID:
          return await message.reply_text("`You Don't Have Rights To Run This!`")
    elif len(message.command) <2:
         await message.reply_text("`No Input Found!`")
    else:
          code = message.text.replace(message.text.split(" ")[0], "")
          x = run(code)
          string = f"**📎 Input**: `{code}`\n\n**📒 Output **:\n`{x}`"
          if len(code) >4000:
              with io.BytesIO(str.encode(string)) as out_file:
                 out_file.name = "shell.text"
                 await message.reply_document(document=out_file, caption="`LONG TEXT MESSAGE CANNOT SHOW SO WE SEND FILE TYPE.`")
          else:
             await message.reply_text(string) 
               

@Nandha.on_message(filters.command("eval",config.CMDS))
async def eval(client, message):
    if not message.from_user.id == config.OWNER_ID:
         return await message.reply_text("`You Don't Have Enough Rights To Run This!`")
    status_message = await message.reply_text("Processing ...")
    cmd = message.text.split(" ", maxsplit=1)[1]

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
