import os
from asyncio import gather

from pyrogram import Client
from pyrogram.types import Message
from pySmartDL import SmartDL

from AsuX import Abishnoi


@Abishnoi.on_cmd("webss")
async def take_ss(self: Client, ctx: Message):
    if len(ctx.command) == 1:
        return await ctx.reply_msg("ɢɪᴠᴇ ᴀ ᴜʀʟ ᴛᴏ ғᴇᴛᴄʜ sᴄʀᴇᴇɴsʜᴏᴛ.", del_in=6)
    url = (
        ctx.command[1]
        if ctx.command[1].startswith("http")
        else f"https://{ctx.command[1]}"
    )
    download_file_path = os.path.join("downloads/", f"webSS_{ctx.from_user.id}.png")
    msg = await ctx.reply_msg("ᴄᴀᴘᴛᴜʀɪɴɢ sᴄʀᴇᴇɴsʜᴏᴛ...")
    try:
        url = f"https://webss.yasirapi.eu.org/api?url={url}&width=1280&height=720"
        downloader = SmartDL(url, download_file_path, progress_bar=False, timeout=10)
        downloader.start(blocking=True)
        await gather(
            *[
                ctx.reply_document(download_file_path),
                ctx.reply_photo(
                    download_file_path, caption="sᴄʀᴇᴇɴsʜᴏᴛ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴜsɪɴɢ ᴘᴜᴘᴘᴇᴛᴇᴇʀ"
                ),
            ]
        )
        await msg.delete_msg()
        os.remove(download_file_path)
    except Exception as e:
        await msg.edit_msg("ғᴀɪʟᴇᴅ ᴛᴏ ᴛᴀᴋᴇ sᴄʀᴇᴇɴsʜᴏᴛ. {err}".format(err=str(e)))
