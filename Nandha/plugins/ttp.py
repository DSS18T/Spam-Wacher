import os
import config
from fpdf import FPDF
from Nandha import Nandha
from pyrogram import filters



@Nandha.on_message(filters.command("ttp",config.CMDS))
async def text_to_pdf(_, message):
  reply = message.reply_to_message
  if reply and not reply.text or not reply: return await message.reply("Give Text Or Reply to Text!")
  name = "ttp.pdf"
  m = await message.reply("Processing....")
  try: 
    pdf = FPDF(); pdf.add_page(); pdf.set_font("Arial", size = 15)
    pdf.cell(200, 10, txt = reply.text,
       ln = 1, align = 'C'); pdf.output(name)
    await m.edit("done now uploading..."); await message.reply_document(name); os.remove(name); await m.delete()
  except Exception as e: await m.delete(); os.remove(name)
