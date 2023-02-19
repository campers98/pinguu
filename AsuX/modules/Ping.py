"""
ɢɪᴛʜᴜʙ -Abishnoi69
ᴛᴇʟᴇɢʀᴀᴍ @Abishnoi1M / @Abishnoi_bots 

"""
import time

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import CommandHandler, ContextTypes

from AsuX import StartTime, rani

from . import get_readable_time


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message

    start_time = time.time()
    message = await msg.reply_text("💤")
    end_time = time.time()
    telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
    uptime = get_readable_time((time.time() - StartTime))

    await message.edit_text(
        "𝗣𝗢𝗡𝗚!! 🥀\n"
        "<b>ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:</b> <code>{}</code>\n"
        "<b>sᴇʀᴠɪᴄᴇ ᴜᴘᴛɪᴍᴇ:</b> <code>{}</code>".format(telegram_ping, uptime),
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="sᴏᴜʀᴄᴇ",
                        url=f"https://github.com/Abishnoi69/AsuX",
                    )
                ]
            ]
        ),
    )


PING_HANDLER = CommandHandler("ping", ping, block=False)
rani.add_handler(PING_HANDLER)
