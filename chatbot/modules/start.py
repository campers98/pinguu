
from chatbot import rani
from telegram.ext import ContextTypes, CommandHandler

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    msg = update.effective_message
    keyb = []
    keyb.append([InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"http://t.me/{context.bot.username}?startgroup=true")])
    await msg.reply_text(f"ʜᴇʏᴀ\nɪ'ᴍ {context.bot.first_name}\nɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴀᴄᴛɪᴠᴇ ʏᴏᴜʀ ᴄʜᴀᴛ", reply_markup=InlineKeyboardMarkup(keyb))

START = CommandHandler(["chatbot", "ping", " start"], start, block=False)
rani.add_handler(START)
    
