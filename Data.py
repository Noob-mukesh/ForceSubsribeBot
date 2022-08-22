from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜᴇʏ {}

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}

ɪ ᴄᴀɴ ғᴏʀᴄᴇ  ʏᴏᴜʀ ɢʀᴏᴜᴘs ᴜsᴇʀ ᴛᴏ ᴊᴏɪɴ  ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ.
 ᴛʜᴇ ᴄʜᴀᴛ ᴄᴀɴ ʙᴇ ᴀ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ ɪᴛ ᴄᴀɴ ᴘʀɪᴠᴀᴛᴇ ᴏʀ ᴘᴜʙʟɪᴄ.
 ᴜsᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ʙᴀʙʏ !

By @mr_sukkun
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ ʙᴏᴛ sᴛᴀᴛᴜs ᴀɴᴅ ᴍᴏʀᴇ✨", url="https://t.me/mukeshbotzone/24")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ?", callback_data="help"),
            InlineKeyboardButton("🎪 ᴀʙᴏᴜᴛ 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ᴀʙᴏᴜᴛ ᴍᴇ♥", url="https://t.me/mr_sukkun")],
        [InlineKeyboardButton("🎨sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 🎨", url="https://t.me/the_support_chat")],
    ]

    # Help Message
    HELP = """
1) Add me as **Admin** to a group.

2) Add me to the particular chat as **Admin** where you want to force your users to join. It can be any group or channel, public or private.

3) Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub -10000000000` or `/forcesubscribe -1000000000`

4) [Optional] Use /settings to change settings!

5) You are good to go. Leave the rest to me.

✨ **ᴀᴠᴀɪʟᴀʙᴇ ᴄᴍᴅs ʙᴀʙʏ ** ✨

/fsub - See current force subscribe chat
/fsub chat_id/username - Force users to join the particular chat
/settings - Change Group Settings
/id - Get the chat id of any group or channel
/about - About The Bot
/help - This Message
/start - Start the Bot

**Note** - You can also use `/forcesubscribe` instead of `/fsub`
    """

    # About Message
    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ** 

ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ  ғᴏʀᴄᴇ sᴜʙ 


ғʀᴀᴍᴇᴡᴏʀᴋ : [Pyrogram](docs.pyrogram.org)

ʟᴀɴɢᴜᴀɢᴇ : [Python](www.python.org)

ᴅᴇᴠᴇʟᴏᴘᴇʀ :  @itz_mst_boi
    """
