import time

from Abg.helpers.human_read import get_readable_time

# from Abg.helpers.ratelimit import ratelimiter
from pyrogram import Client
from pyrogram.types import Message

from AsuX import Abishnoi, StartTime


@Abishnoi.on_cmd(["ping", "pong", "alive"])
# @ratelimiter
async def ping(self: Client, ctx: Message):
    currentTime = get_readable_time(time.time() - StartTime)
    start_t = time.time()
    rm = await ctx.reply_msg("💫 ᴘᴏɴɢ !!...")
    end_t = time.time()
    time_taken_s = round(end_t - start_t, 3)
    await rm.edit_msg(
        f"<b>ᴘɪɴɢ:</b> <code>{time_taken_s}ᴍs</code>\n<b>ᴜᴘᴛɪᴍᴇ:</b> <code>{currentTime}</code>"
    )
