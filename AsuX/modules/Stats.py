""" 
ɢɪᴛʜᴜʙ -Abishnoi69
ᴛᴇʟᴇɢʀᴀᴍ @Abishnoi1M / @Abishnoi_bots 
"""

import datetime
import platform
from platform import python_version

from psutil import boot_time, cpu_percent, disk_usage, virtual_memory
from telegram import __version__
from telegram.constants import ParseMode
from telegram.ext import CommandHandler

from AsuX import rani


async def system_status(update, context):
    uptime = datetime.datetime.fromtimestamp(boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    status = "<b>======[ SYSTEM INFO ]======</b>\n\n"
    status += "<b>sʏsᴛᴇᴍ ᴜᴘᴛɪᴍᴇ:</b> <code>" + str(uptime) + "</code>\n"

    uname = platform.uname()
    status += "<b>sʏsᴛᴇᴍ:</b> <code>" + str(uname.system) + "</code>\n"
    status += "<b>ɴᴏᴅᴇ ɴᴀᴍᴇ:</b> <code>" + str(uname.node) + "</code>\n"
    status += "<b>ʀᴇʟᴇᴀsᴇ:</b> <code>" + str(uname.release) + "</code>\n"
    status += "<b>ᴠᴇʀsɪᴏɴ:</b> <code>" + str(uname.version) + "</code>\n"
    status += "<b>ᴍᴀᴄʜɪɴᴇ:</b> <code>" + str(uname.machine) + "</code>\n"
    status += "<b>ᴘʀᴏᴄᴇssᴏʀ:</b> <code>" + str(uname.processor) + "</code>\n\n"
    mem = virtual_memory()
    cpu = cpu_percent()
    disk = disk_usage("/")
    status += "<b>ᴄᴘᴜ ᴜsᴀɢᴇ:</b> <code>" + str(cpu) + " %</code>\n"
    status += "<b>ʀᴀᴍ ᴜsᴀɢᴇ:</b> <code>" + str(mem[2]) + " %</code>\n"
    status += "<b>sᴛᴏʀᴀɢᴇ ᴜsᴇᴅ:</b> <code>" + str(disk[3]) + " %</code>\n\n"
    status += "<b>ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ:</b> <code>" + python_version() + "</code>\n"
    status += "<b>ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ:</b> <code>" + str(__version__) + "</code>\n"
    await context.bot.sendMessage(
        update.effective_chat.id, status, parse_mode=ParseMode.HTML
    )


SYS_STATUS_HANDLER = CommandHandler(["stats", "sysinfo"], system_status, block=False)
rani.add_handler(SYS_STATUS_HANDLER)
