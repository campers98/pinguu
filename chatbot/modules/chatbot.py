from pymongo import MongoClient
import requests
import random
import os
import re
from re import IGNORECASE, escape, search
from telegram import Update
from telegram.error import TelegramError
from telegram.error import BadRequest
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, CommandHandler, filters as Filters, MessageHandler, CallbackQueryHandler
import telegram.ext as tg
import re
from telegram.ext import Application
import asyncio
from typing import Union, List, Dict, Callable, Generator, Any
import itertools
from collections.abc import Iterable
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram import Chat, ChatMember, Update, User
from functools import wraps
from chatbot import *
USERS_GROUP = 11

async def log_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
   chat = update.effective_chat
   message = update.effective_message
   try:
       if (
           message.text.startswith("!")
           or message.text.startswith("/")
           or message.text.startswith("?")
           or message.text.startswith("@")
           or message.text.startswith("#")
       ):
           return
   except Exception:
       pass
   chatbotdb = MongoClient(MONGO_DB_URL)
   chatbotai = chatbotdb["Word"]["WordDb"]
   if not message.reply_to_message:
       K = []  
       is_chat = chatbotai.find({"chat":chat.id, "word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       if K:
           hey = random.choice(K)
           is_text = chatbotai.find_one({"chat":chat.id, "text": hey})
           Yo = is_text['check']
       else:
           r = requests.get(f"http://api.brainshop.ai/get?bid={AI_BID}&uid={message.from_user.id}&key={AI_API_KEY}&msg={message.text}")
           hey = r.json()["cnt"]
           Yo = None
       if Yo == "sticker": 
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:                   
       if message.reply_to_message.from_user.id == BOT_ID:                    
           K = []  
           is_chat = chatbotai.find({"chat":chat.id, "word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           if K:
               hey = random.choice(K)
               is_text = chatbotai.find_one({"chat":chat.id, "text": hey})
               Yo = is_text['check']
           else:
               r = requests.get(f"http://api.brainshop.ai/get?bid={AI_BID}&uid={message.from_user.id}&key={AI_API_KEY}&msg={message.text}")
               hey = r.json()["cnt"]
               Yo = None
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == BOT_ID:          
           if message.sticker:
               is_chat = chatbotai.find_one({"chat":chat.id, "word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatbotai.insert_one({"chat":chat.id, "word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatbotai.find_one({"chat":chat.id, "word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatbotai.insert_one({"chat":chat.id, "word": message.reply_to_message.text, "text": message.text, "check": "none"})


USER_HANDLER = MessageHandler(
    Filters.ALL, log_user, block=False
)
rani.add_handler(USER_HANDLER, USERS_GROUP)
