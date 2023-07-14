from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from Config import BOT_USERNAME,START_IMG


@Client.on_message(filters.command(["about",f"@{BOT_USERNAME}about"]))
async def about(bot, msg):
    await msg.reply_photo(START_IMG,
        Data.ABOUT,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )
