import time
from asyncio import sleep

from pyrogram import enums
from pyrogram.types import Message

from AsuX import Abishnoi


@Abishnoi.on_cmd("instatus", group_only=True, self_admin=True)
@Abishnoi.adminsOnly(permissions="can_change_info", is_both=True)
async def instatus(c: Abishnoi, m: Message):
    start_time = time.perf_counter()
    user = await c.get_chat_member(m.chat.id, m.from_user.id)
    count = await c.get_chat_members_count(m.chat.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
        sent_message = await m.reply_text("**ɪs ɢᴀᴛʜᴇʀɪɴɢ ᴜsᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ...**")
        recently = 0
        within_week = 0
        within_month = 0
        long_time_ago = 0
        deleted_acc = 0
        premium_acc = 0
        no_username = 0
        restricted = 0
        banned = 0
        uncached = 0
        bot = 0
        async for ban in c.get_chat_members(
            m.chat.id, filter=enums.ChatMembersFilter.BANNED
        ):
            banned += 1
        async for restr in c.get_chat_members(
            m.chat.id, filter=enums.ChatMembersFilter.RESTRICTED
        ):
            restricted += 1
        async for member in c.get_chat_members(m.chat.id):
            user = member.user
            if user.is_deleted:
                deleted_acc += 1
            elif user.is_bot:
                bot += 1
            elif user.is_premium:
                premium_acc += 1
            elif not user.username:
                no_username += 1
            elif user.status.value == "recently":
                recently += 1
            elif user.status.value == "last_week":
                within_week += 1
            elif user.status.value == "last_month":
                within_month += 1
            elif user.status.value == "long_ago":
                long_time_ago += 1
            else:
                uncached += 1
        end_time = time.perf_counter()
        timelog = "{:.2f}".format(end_time - start_time)
        await sent_message.edit(
            "<b>💠 {}\n👥 {} ᴍᴇᴍʙᴇʀ\n——————\n👁‍🗨ᴍᴇᴍʙᴇʀ sᴛᴀᴛᴜs ɪɴғᴏʀᴍᴀᴛɪᴏɴ \n——————\n</b>🕒 <code>ʀᴇᴄᴇɴᴛʟʏ</code>: {}\n🕒 <code>ʟᴀsᴛ_ᴡᴇᴇᴋ</code>: {}\n🕒 <code>ʟᴀsᴛ_ᴍᴏɴᴛʜ</code>: {}\n🕒 <code>ʟᴏɴɢ_ᴀɢᴏ</code>: {}\n🔎 ɴᴏ ᴜsᴇʀɴᴀᴍᴇ: {}\n🤐 ʀᴇsᴛʀɪᴄᴛᴇᴅ: {}\n🚫 ʙʟᴏᴄᴋᴇᴅ: {}\n👻 ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ (<code>/zombies</code>): {}\n🤖 ʙᴏᴛ: {}\n⭐️ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀ: {}\n👽 ᴜɴᴄᴀᴄʜᴇᴅ: {}\n\n⏱ ᴇxᴇᴄᴜᴛɪᴏɴ ᴛɪᴍᴇ {} sᴇᴄᴏɴᴅ.".format(
                m.chat.title,
                count,
                recently,
                within_week,
                within_month,
                long_time_ago,
                no_username,
                restricted,
                banned,
                deleted_acc,
                bot,
                premium_acc,
                uncached,
                timelog,
            )
        )
    else:
        sent_message = await m.reply_text(
            "❗ **ʏᴏᴜ ᴍᴜsᴛ ʙᴇ ᴀɴ ᴀᴅᴍɪɴ ᴏʀ ɢʀᴏᴜᴘ ᴏᴡɴᴇʀ ᴛᴏ ᴘᴇʀғᴏʀᴍ ᴛʜɪs ᴀᴄᴛɪᴏɴ.**"
        )
        await sleep(5)
        await sent_message.delete()
