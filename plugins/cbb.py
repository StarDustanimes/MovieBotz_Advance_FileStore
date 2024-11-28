#(©) WeekendsBotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b><blockquote>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>𐌵ⁿܔSŏ𐌵l࿐</a>\n○ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Anime_Stardust'>ᴀɴɪᴍᴇ sᴛᴀʀᴅᴜsᴛ</a>\n○ ᴍᴀɴɢᴀ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Manga_Stardust'>ᴍᴀɴɢᴀ sᴛᴀʀᴅᴜsᴛ</a>\n○ ᴀɴɪᴍᴇ ɴᴇᴡs : <a href='https://t.me/News_Stardust'>ɴᴇᴡs sᴛᴀʀᴅᴜsᴛ</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ : <a href='https://t.me/chathub_stardust'>ᴄʜᴀᴛʜᴜʙ sᴛᴀʀᴅᴜsᴛ</a></blockquote></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡ Cℓσѕє", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
