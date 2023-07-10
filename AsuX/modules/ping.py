import time

from Abg.helpers.human_read import get_readable_time
from pyrogram import Client
from pyrogram.types import Message

from AsuX.modules.utils.langs import lang
from AsuX import Abishnoi, StartTime


@Abishnoi.on_cmd(["ping", "pong", "alive"])
@lang
async def ping(self: Client, ctx: Message, _):
    currentTime = get_readable_time(time.time() - StartTime)
    start_t = time.time()
    rm = await ctx.reply_msg("_[ping_1]")
    end_t = time.time()
    time_taken_s = round(end_t - start_t, 3)
    await rm.edit_msg(
        "_[ping_2]".format(time_taken_s, currentTime)
    )
