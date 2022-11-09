import config
from fpdf import FPDF
from Nandha import Nandha
from pyrogram import filters


@Nandha.on_message(filters.command("ttp",config.CMDS))
async def text_to_pdf(_, message):
  reply = message.reply_to_message
  if not reply.text or not len(message.text.split()) == 1: return await message.reply("Give Text Or Reply to Text!")
  text = reply.text or message.text.split(None,1)[1]
  name = "ttp.pdf"
  pdf = FPDF()
  pdf.add_page()
  pdf.set_font("Arial", size = 15)
  pdf.cell(200, 10, txt = text, 
  pdf.output(name)
  await message.reply_document(name)
  os.remove(name)
