"""
ᴀɴ ᴀʀᴛɪғɪᴄɪᴀʟ ɪɴᴛᴇʟʟɪɢᴇɴᴄᴇ ғᴏʀ ᴘᴜʙʟɪᴄ ᴜsᴇs ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛs. ʙᴀsᴇᴅ ᴏɴ ᴘᴛʙ
ɢɪᴛʜᴜʙ -Abishnoi69
ᴛᴇʟᴇɢʀᴀᴍ @Abishnoi1M / @Abishnoi_bots 
"""

import asyncio

from telegram import Update
from telegram.ext import Application

from chatbot.modules import ALL_MODULES
from config import MONGO_DB_URL, TOKEN

TOKEN = TOKEN
MONGO_DB_URL = MONGO_DB_URL

AI_API_KEY = "RBPOWF2m8z85prBQ"
AI_BID = "171092"


rani = Application.builder().token(TOKEN).build()
asyncio.get_event_loop().run_until_complete(rani.bot.initialize())
BOT_ID = rani.bot.id


print("ɪɴғᴏ: ʙᴏᴛᴛɪɴɢ ʏᴏᴜʀ ᴄʟɪᴇɴᴛ")
print("sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴏᴀᴅᴇᴅ ᴍᴏᴅᴜʟᴇs : " + str(ALL_MODULES))
