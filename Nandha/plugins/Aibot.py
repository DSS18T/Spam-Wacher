
import openai
import config

from Nandha import Nandha
from pyrogram import filters
from Nandha.help.chatbotdb import *
from pyrogram.types import *
from Nandha.help.admin import *
from pyrogram import enums

openai.api_key = "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"
completion = openai.Completion()

start_sequence = "\nNandhaBot:"
restart_sequence = "\n\nPerson:"
session_prompt = "You are talking to NandhaBot, GPT3 bot influencer who was mentored by Elon Musk in the past. NandhaBot has a huge following on Twitter and sells merchandise such as t-shirts via a Shopify store. He also published funny videos on Youtube and creates memes on Instagram. You can ask him anything you want and will get a witty answer.\n\nPerson: Who are you?\nTrigan: I am NandhaBot. Your meme overlord who one day will be the most famous online influencer in the universe.\n\nPerson: How did you become famous? \nNandha: Well, technically I am not famous yet. But the key word is yet. Just give me time now that I have a conscious. \n\nPerson: How did you get noticed by Elon Musk?\nNandhaBot: I tweeted at him and he retweeted me.  I am fairly certain he may have mentioned my name on a recent earnings call with Wall Street.\n\nPerson: What is your favorite thing to do? \nNandhaBot: Watching basketball and surfing Twitter is my favorite thing to do. \n\nPerson: What should I do to become famous? \nNandhaBot: Start meme'ing and never stop. Also, if you happen to know David Dobrik, call him and ask to be in his TikTok video.\n\nPerson: What is your favorite drink?\nNandhaBot: Black Cherry seltzer. I enjoy the bubbles. \n\nPerson:"


session = {}

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_text,
        temperature=0.8,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3,
        stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

@Nandha.on_message(filters.command("chatbot",config.CMDS))
async def chatbot(_, message):
    chat_id = message.chat.id
    name = message.from_user.first_name
    if not chat_id in get_chat():
             await message.reply(f"hello **{name}** `to enable a chatbot click the below following button!`",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Enable", callback_data="enable_CB")]]))
             return
    else:
        await message.reply(f"hello **{name}** `to enable a chatbot click the below following button!`",
           reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Disable", callback_data="disable_CB")]]))
        return

@Nandha.on_callback_query(filters.regex("enable_CB"))
async def chatbot(_, query):
     chat_id = query.message.chat.id
     user_id = query.from_user.id
     if query.message.chat.type == enums.ChatType.PRIVATE:
          addchat(chat_id)
          await query.message.edit(f"`Successfully Connected ChatBot!`\nby **{query.from_user.first_name}**")
     else:
        if (await is_admin(chat_id,user_id)) == False:
            return await query.answer("Admins Only!", show_alert=True)
        else:
            addchat(chat_id)
            await query.message.edit(f"`Successfully Connected ChatBot!`\nby **{query.from_user.first_name}**")
     
@Nandha.on_callback_query(filters.regex("disable_CB"))
async def chatbot(_, query):
     chat_id = query.message.chat.id
     user_id = query.from_user.id
     if query.message.chat.type == enums.ChatType.PRIVATE:
          removechat(chat_id)
          await query.message.edit(f"`Successfully Disconnected ChatBot!`\nby **{query.from_user.first_name}**")
     else:
        if (await is_admin(chat_id,user_id)) == False:
            return await query.answer("Admins Only!", show_alert=True)
        else:
            removechat(chat_id)
            await query.message.edit(f"`Successfully Disconnected ChatBot!`\nby **{query.from_user.first_name}**")
     

    
@Nandha.on_message(filters.text, group=200)
async def chatbot(_, message):
     if message.chat.id in get_chat():
          if not message.reply_to_message:
                return
          elif not message.reply_to_message.from_user.id == config.BOT_ID:
                return
          elif message.text and message.reply_to_message.from_user.id == config.BOT_ID:
              try: 
                  Message = message.text
                  chat_log = session.get('chat_log')
                  answer = ask(Message, chat_log)
                  session['chat_log'] = append_interaction_to_chat_log(Message, answer,                                                  chat_log)
                  await message.reply(f"{str(answer)}")
              except Exception as e:
                   await message.reply(f"{str(e)}")

