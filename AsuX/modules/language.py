from asyncio import sleep

from Abg.inline import InlineKeyboard
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, Message
from strings import get_string, languages_present

from AsuX import Abishnoi
from AsuX.db.lang_db import Langs
from AsuX.modules.utils.langs import lang


def lanuages_keyboard(_):
    keyboard = InlineKeyboard(row_width=3)
    keyboard.add(
        *[
            (
                InlineKeyboardButton(
                    text=languages_present[i],
                    callback_data=f"languages:{i}",
                )
            )
            for i in languages_present
        ]
    )
    keyboard.row(
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"start_back",
        ),
        InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close_"),
    )
    return keyboard


@Abishnoi.on_cmd("lang")
@lang
async def langs_command(client, message: Message, _):
    keyboard = lanuages_keyboard(_)
    await message.reply_text(
        _["setting_1"].format(message.chat.title, message.chat.id),
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )


@Abishnoi.on_cb("LG")
@lang
async def lanuagecb(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)


@Abishnoi.on_callback_query(filters.regex(r"languages:(.*?)"))
@lang
async def language_markup(client, CallbackQuery, _):
    langauge = (CallbackQuery.data).split(":")[1]
    old = Langs(CallbackQuery.message.chat.id).get_lang()
    if str(old) == str(langauge):
        return await CallbackQuery.answer(
            "You're already on same language", show_alert=True
        )
    try:
        _ = get_string(langauge)
        await CallbackQuery.answer(
            "Successfully changed your language.", show_alert=True
        )
    except:
        return await CallbackQuery.answer(
            "Failed to change language or Language under update.",
            show_alert=True,
        )
    Langs(CallbackQuery.message.chat.id).set_lang(langauge)
    await sleep(0.1)
    keyboard = lanuages_keyboard(_)

    return await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)
