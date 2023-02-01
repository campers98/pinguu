"""
ᴀɴ ᴀʀᴛɪғɪᴄɪᴀʟ ɪɴᴛᴇʟʟɪɢᴇɴᴄᴇ ғᴏʀ ᴘᴜʙʟɪᴄ ᴜsᴇs ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛs. ʙᴀsᴇᴅ ᴏɴ ᴘᴛʙ
ɢɪᴛʜᴜʙ -Abishnoi69
ᴛᴇʟᴇɢʀᴀᴍ @Abishnoi1M / @Abishnoi_bots 
"""
import asyncio
from telegram.ext import ContextTypes, CommandHandler
from telegram import Update, InlineKeyboardButton
from config import MONGO_DB_URL, TOKEN
TOKEN = TOKEN
MONGO_DB_URL = MONGO_DB_URL

AI_API_KEY = "RBPOWF2m8z85prBQ"
AI_BID = "171092"
USERS_GROUP = 11

rani = Application.builder().token(TOKEN).build()
asyncio.get_event_loop().run_until_complete(rani.bot.initialize())
BOT_ID = rani.bot.id

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    msg = update.effective_message
    keyb = []
    keyb.append([InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"http://t.me/{context.bot.username}?startgroup=true")])
    await msg.reply_text(f"ʜᴇʏᴀ\nɪ'ᴍ {context.bot.first_name}\nɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴀᴄᴛɪᴠᴇ ʏᴏᴜʀ ᴄʜᴀᴛ", reply_markup=InlineKeyboardMarkup(keyb))



START = CommandHandler(["chatbot", "ping", "start"], start, block=False)
rani.add_handler(START)

print("ɪɴғᴏ: ʙᴏᴛᴛɪɴɢ ʏᴏᴜʀ ᴄʟɪᴇɴᴛ")

application.run_polling()
