from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜᴇʏ {}

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {} [🥀](https://te.legra.ph/file/fe924e2746ad34b7dc76d.jpg)

ɪ ᴄᴀɴ ғᴏʀᴄᴇ  ʏᴏᴜʀ ɢʀᴏᴜᴘs ᴜsᴇʀ ᴛᴏ ᴊᴏɪɴ  ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ.
 ᴛʜᴇ ᴄʜᴀᴛ ᴄᴀɴ ʙᴇ ᴀ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ ɪᴛ ᴄᴀɴ ᴘʀɪᴠᴀᴛᴇ ᴏʀ ᴘᴜʙʟɪᴄ.
 ᴜsᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ʙᴀʙʏ !

Bʏ - @mr_sukkun
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ ʙᴏᴛ sᴛᴀᴛᴜs ᴀɴᴅ ᴍᴏʀᴇ✨", url="https://t.me/mukeshbotzone/24")],
        [
            InlineKeyboardButton("⚡ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅ ⚡", callback_data="help"),
            InlineKeyboardButton("🎪 ᴀʙᴏᴜᴛ ᴍᴇ", callback_data="about")
        ],
        [InlineKeyboardButton("➕ᴀᴅᴅ ɢʀᴏᴜᴘ ᴄᴏɴᴛʀᴏʟʟᴇʀ ʙᴏᴛ ➕", url="https://t.me/groupcontrollertgbot?startgroup=true")],
        [InlineKeyboardButton("★ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ★", url="https://t.me/the_support_chat")],
        [InlinekeyboardButton("➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ➕", url="https://t.me/forcesubtgbot?startgroup=true")],
    ]
    # Help Message
    HELP = """
𝟷) ᴀᴅᴅ ᴍᴇ ᴀs ᴀᴅᴍɪɴ ᴛᴏ ᴀ ɢʀᴏᴜᴘ. 
𝟸) ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴀs ᴀᴅᴍɪɴ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ғᴏʀᴄᴇ ʏᴏᴜʀ ᴜsᴇʀs ᴛᴏ ᴊᴏɪɴ. ɪᴛ ᴄᴀɴ ʙᴇ ᴀɴʏ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ, ᴘᴜʙʟɪᴄ ᴏʀ ᴘʀɪᴠᴀᴛᴇ. 
𝟹) ᴜsᴇ /fsub chat_id /username ᴛᴏ ᴍᴀᴋᴇ ᴍᴇ ғᴜɴᴄᴛɪᴏɴᴀʟ. ᴜsᴇ /id ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴄʜᴀᴛ ɪᴅ.
 ᴇxᴀᴍᴘʟᴇ : /fsub -𝟷𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶 ᴏʀ /forcesubsribe -𝟷𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶 
𝟺) [ᴏᴘᴛɪᴏɴᴀʟ] ᴜsᴇ /settings ᴛᴏ ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs! 
𝟻) ʏᴏᴜ ᴀʀᴇ ɢᴏᴏᴅ ᴛᴏ ɢᴏ. ʟᴇᴀᴠᴇ ᴛʜᴇ ʀᴇsᴛ ᴛᴏ ᴍᴇ.

 ✨ ᴀᴠᴀɪʟᴀʙᴇ ᴄᴍᴅs ʙᴀʙʏ  ✨ 
/start -  sᴛᴀʀᴛ ғᴏʀᴄᴇ sᴜʙsʀɪʙᴇ ʙᴏᴛ 
/fsub - sᴇᴇ ᴄᴜʀʀᴇɴᴛ ғᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ ᴄʜᴀᴛ 
/fsub chat_id/username- ғᴏʀᴄᴇ ᴜsᴇʀs ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ
/settings - ᴄʜᴀɴɢᴇ ɢʀᴏᴜᴘ sᴇᴛᴛɪɴɢs 
/id - ɢᴇᴛ ᴛʜᴇ ᴄʜᴀᴛ ɪᴅ ᴏғ ᴀɴʏ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ
/about - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ 
/help - ᴛʜɪs ᴍᴇssᴀɢᴇ 
☞︎︎︎ ɴᴏᴛᴇ - ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ /forcesubsribe ɪɴsᴛᴇᴀᴅ ᴏғ /fsub
"""

    # About Message
    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ** 

ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ  ғᴏʀᴄᴇ sᴜʙ 


ғʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)

ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](www.python.org)

ᴅᴇᴠᴇʟᴏᴘᴇʀ :  @itz_mst_boi

ᴜᴘᴅᴀᴛᴇ   : @mukeshbotzone
    """
