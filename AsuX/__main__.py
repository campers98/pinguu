"""
ɢɪᴛʜᴜʙ -: Abishnoi69
ᴛᴇʟᴇɢʀᴀᴍ -: @Abishnoi1M / @Abishnoi_bots 
"""


import asyncio
import importlib

from pyrogram import idle

from AsuX import LOGGER, Abishnoi
from AsuX.modules import ALL_MODULES


async def start_bot():
    try:
        await Abishnoi.start()
    except Exception as e:
        LOGGER.error(e)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("AsuX.modules." + all_module)

    LOGGER.info(f"@{Abishnoi.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
    LOGGER.info("Stopping AsuX Bot...")
