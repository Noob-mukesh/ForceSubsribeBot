from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from Config import BOT_USERNAME,START_IMG,


@Client.on_message(filters.command(["about",f"@{BOT_USERNAME}about"]))
async def about(bot, msg):
    await msg.reply_phto(START_IMG,
        Data.ABOUT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )
