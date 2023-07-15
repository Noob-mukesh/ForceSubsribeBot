from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from Config import START_IMG

# Start Message
@Client.on_message(filters.private & filters.command("start"))
async def start(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(START_IMG,
		caption=Data.START.format(msg.from_user.mention, mention),
		reply_markup=InlineKeyboardMarkup(Data.buttons)
	)
