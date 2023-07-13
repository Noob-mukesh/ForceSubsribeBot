from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from Config import MUST_JOIN


@Client.on_message( filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.delete()
                await msg.reply(
                    f"Hey @{msg.from_user.username} ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴ  [ᴛʜɪs ᴄʜᴀɴɴᴇʟ]({link}) ᴛᴏ ᴜsᴇ ᴍᴇ. Aғᴛᴇʀ ᴊᴏɪɴɢ ᴛʀʏ ᴀɢᴀɪɴ /start or /help!",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("✨ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ✨", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"ɪ'ᴍ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ MUST_JOIN ᴄʜᴀᴛ : {MUST_JOIN} !")
