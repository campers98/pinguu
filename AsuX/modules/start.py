import time

from Abg.helpers.human_read import get_readable_time
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)

from AsuX import Abishnoi
from AsuX import StartTime as boot
from AsuX.db.chats_db import add_served_chat
from AsuX.db.users_db import add_served_user

from . import PICS


@Abishnoi.on_cmd("start")
async def start_pm(cli: Abishnoi, message: Message):
    bot_uptime = int(time.time() - boot)
    uptime = get_readable_time(bot_uptime)
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ",
                    url=f"https://t.me/{(await cli.get_me()).username}?startgroup=new",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ",
                    callback_data="help_",
                ),
                InlineKeyboardButton(
                    text="sᴏᴜʀᴄᴇ",
                    callback_data="h_source",
                ),
            ],
        ]
    )
    await message.reply_photo(
        PICS,
        caption=f"""🥀 ʜᴇʏ {message.from_user.mention},

ᴛʜɪs ɪs {(await cli.get_me()).mention},
 ɪ ᴄᴀɴ ꜰᴏʀᴄᴇ ᴜꜱᴇʀ ᴛᴏ ᴊᴏɪɴ ʙᴇꜰᴏʀᴇ ᴠᴏᴛᴇ ᴀɴʏᴏɴᴇ.\nɪғ ᴜsᴇʀ ʟᴇᴀᴠᴇ ᴄʜᴀᴛ ᴠᴏᴛᴇ ᴜɴᴅᴏɴᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄ\nᴀʟɪᴠᴇ sɪɴᴄᴇ {uptime}""",
        reply_markup=upl,
    )


@Abishnoi.on_cb("close")
async def on_close_button(_, CallbackQuery):
    await CallbackQuery.answer()
    await CallbackQuery.message.delete()


@Abishnoi.on_cb("help_")
async def help_(cli: Abishnoi, query: CallbackQuery):
    await query.answer()
    await query.message.edit_text(
        text=f"""
<u><b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ {(await cli.get_me()).mention} :</b></u>

• /enter (/register, /participate): ᴛᴏ ᴘᴀʀᴛɪᴄɪᴘᴀᴛᴇ ɪɴ ɢɪᴠᴇᴀᴡᴀʏ. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴇ ʙᴏᴛ ɪs sᴛᴀʀᴛᴇᴅ ᴛᴏ ɢᴇᴛ ʀᴇɢɪsᴛᴇʀᴇᴅ.

ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:
• /startgiveaway (/startga) : sᴛᴀʀᴛ ᴛʜᴇ ɢɪᴠᴇᴀᴡᴀʏ. ʀᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ ᴛᴏ sᴇɴᴅ ɢɪᴠᴇᴀᴡᴀʏ sᴛᴀʀᴛ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ᴛᴀɢɢᴇᴅ ᴍᴇᴅɪᴀ (ᴡɪʟʟ ᴏɴʟʏ ᴡʀᴏᴋ ɪɴ ʙᴏᴛ ᴘᴍ(ᴅᴍ)).
ᴜsᴇʀ ᴅᴇᴘᴇɴᴅᴇɴᴛ ᴄᴏᴍᴍᴀɴᴅs
• /stopentry <ᴘᴏsᴛ ʟɪɴᴋ>: sᴛᴏᴘ ᴛʜᴇ ғᴜʀᴛʜᴇʀ ᴇɴᴛʀɪᴇs. ᴄʜᴀɴɴᴇʟ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴛᴏᴘ ᴛʜᴇ ᴇɴᴛʀɪᴇs. ᴘᴀss ᴛʜᴇ ᴘᴏsᴛ ʟɪɴᴋ ᴏғ ᴛʜᴇ ᴘᴏsᴛ ʏᴏᴜ ᴡᴀɴᴛ to ᴇᴅɪᴛ ᴛʜᴇ ᴍsɢ ᴀɴᴅ sᴇᴛ ɪᴛ ᴀs ᴄʟᴏsᴇᴅ ᴍᴇssᴀɢᴇ
• /startvote <ᴘᴏsᴛ ʟɪɴᴋ>: sᴛᴀʀᴛ ᴜᴘʟᴏᴀᴅɪɴɢ ᴀʟʟ ᴛʜᴇ ᴜsᴇʀ ɪɴғᴏ ᴀɴᴅ ᴡɪʟʟ sᴛᴀʀᴛ ᴠᴏᴛɪɴɢ. ᴘᴀss ᴛʜᴇ ᴘᴏsᴛ ʟɪɴᴋ ᴏғ ᴛʜᴇ ᴘᴏsᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴇᴅɪᴛ ᴛʜᴇ ᴍsɢ ᴀɴᴅ sᴇᴛ ɪᴛ ᴀs ᴄʟᴏsᴇᴅ ᴍᴇssᴀɢᴇ. ɴᴏᴛ ɴᴇᴄᴇssᴀʀʏ ᴛᴏ ɢɪᴠᴇ ᴘᴏsᴛ ʟɪɴᴋ.
ᴘᴏsᴛ ʟɪɴᴋ (ғᴏʀ ᴄʜᴀɴɴᴇʟs) = ᴍᴇssᴀɢᴇ ʟɪɴᴋ (ғᴏʀ ᴄʜᴀᴛs)
• /stopgiveaway (/stopga) : sᴛᴏᴘ ᴛʜᴇ ɢɪᴠᴇᴀᴡᴀʏ. ᴄʜᴀɴɴᴇʟ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴛᴏᴘ ᴛʜᴇ ɢɪᴠᴇᴀᴡᴀʏ. ᴡɪʟʟ ᴀʟsᴏ ᴄʟᴏsᴇ ᴠᴏᴛɪɴɢ ᴀᴛ sᴀᴍᴇ ᴛɪᴍᴇ.


""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="AsuX_home")]]
        ),
        parse_mode=ParseMode.HTML,
    )


@Abishnoi.on_cb("source_")
async def source_(cli: Abishnoi, query: CallbackQuery):
    await query.answer()
    await query.message.edit_text(
        text=f"""
<u><b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ sᴏᴜʀᴄᴇ ᴏғ {Abishnoi.mention} :</b></u>

• ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ : [ᴘʏʀᴏɢʀᴀᴍ](https://github.com/pyrogram/pyrogram), [ᴀʙɢ](https://github.com/Abishnoi69/Abg) ᴀɴᴅ [ᴍᴏɴɢᴏ](https://cloud.mongodb.com/) ᴀs ᴅᴀᴛᴀʙᴀsᴇ.
• ʜᴇʀᴇ ɪs ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [{Abishnoi.name}](https://github.com/Abishnoi69/AsuX)
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="AsuX_home")]]
        ),
    )


@Abishnoi.on_cb("AsuX_home")
async def AsuX_home(cli: Abishnoi, query: CallbackQuery):
    await query.answer()
    bot_uptime = int(time.time() - boot)
    uptime = get_readable_time(bot_uptime)
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ",
                    url=f"https://t.me/{(await cli.get_me()).username}?startgroup=new",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ",
                    callback_data="help_",
                ),
                InlineKeyboardButton(
                    text="sᴏᴜʀᴄᴇ",
                    callback_data="source_",
                ),
            ],
        ]
    )
    await query.edit_message_media(
        InputMediaPhoto(
            media=PICS,
            caption=f"""🥀 ʜᴇʏ {query.from_user.mention},

ᴛʜɪs ɪs {(await cli.get_me()).mention},
  ɪ ᴄᴀɴ ꜰᴏʀᴄᴇ ᴜꜱᴇʀ ᴛᴏ ᴊᴏɪɴ ʙᴇꜰᴏʀᴇ ᴠᴏᴛᴇ ᴀɴʏᴏɴᴇ.\nɪғ ᴜsᴇʀ ʟᴇᴀᴠᴇ ᴄʜᴀᴛ ᴠᴏᴛᴇ ᴜɴᴅᴏɴᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄ\nᴀʟɪᴠᴇ sɪɴᴄᴇ {uptime}""",
        ),
        reply_markup=upl,
    )
