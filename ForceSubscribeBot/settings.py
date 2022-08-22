from pyrogram import Client, filters
from ForceSubscribeBot.admin_check import admin_check
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ForceSubscribeBot.database.chats_sql import get_action, get_ignore_service, get_only_owner, chat_exists


@Client.on_message(filters.text & filters.incoming & filters.command("settings"))
async def settings(bot: Client, msg):
    success = await admin_check(bot, msg)
    if not success:
        return
    chat_id = msg.chat.id
    if not await chat_exists(msg.chat.id):
        await msg.reply("ᴘʟᴇᴀsᴇ ᴀᴅᴅ ᴀ ғᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ ᴄʜᴀᴛ  ᴜsɪɴɢ /fsub  ᴛᴏ ᴜsᴇ ᴍᴇ.")
        return
    only_owner = await get_only_owner(chat_id)
    creator =ᴛʀᴜᴇ ɪғ (await bot.get_chat_member(chat_id, msg.from_user.id)).status == "creator" else False
    if only_owner and not creator:
        await msg.reply("ᴏɴʟʏ  ᴏᴡɴᴇʀ ᴄᴀɴ  ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs ɪɴ ᴛʜɪs ᴄʜᴀᴛ")
        return
    buttons = await action_markup(chat_id)
    await msg.reply(
        "**sᴇᴛᴛɪɴɢs** \n\n"
        "1) ᴄʜᴏᴏsᴇ ᴀᴄᴛɪᴏɴ ᴛʏᴘᴇ ғᴏʀ ᴛʜᴏsᴇ  ᴡʜᴏ ʜᴀᴠᴇɴᴛ ᴊᴏɪɴᴇᴅ ғᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ ᴄʜᴀᴛ. Dᴇғᴀᴜʟᴛs ᴛᴏ ᴍᴜᴛᴇ .\n"
        "2) ᴄʜᴏᴏsᴇ  ᴛᴏ ɪɢɴᴏʀᴇ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀғᴇs ᴏʀ ɴᴏᴛ. Iғ ʏᴏᴜ ᴅᴏɴᴛ ᴡᴀɴᴛ  ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴛᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏɴ ᴜsᴇʀs ᴊᴜsᴛ ᴡʜᴇɴ ᴛʜᴇ ᴄʜᴀᴛ (didn't chat) ᴄʜᴏᴏsᴇ ᴏɴ ᴇʟsᴇ  , ᴏғғ ᴀɴᴛɪsᴘᴀᴍ ʏ, \n"
        "3)  ᴄʜᴏᴏsᴇ ᴛᴏ ᴀʟʟᴏᴡ ᴀᴅᴍɪɴs ᴛᴏ ᴄʜᴀɴɢᴇ ғsᴜʙ ᴀɴᴅ sᴇᴛᴛɪɴɢs ᴏʀ ɴᴏᴛ.ᴅᴇғᴀᴜʟᴛ ᴛᴏ 'ᴀʟʟᴏᴡ ᴏɴʟʏ'.",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


async def action_markup(chat_id):
    action = await get_action(chat_id)
    warn = "Warn"
    mute = "Mute"
    kick = "Kick"
    ban = "Ban"
    if action == "warn":
        warn += " ✅"
    elif action == "mute":
        mute += " ✅"
    elif action == "kick":
        kick += " ✅"
    else:
        ban += " ✅"
    ignore_service = await get_ignore_service(chat_id)
    ignore_service_text = "Ignore Welcome Message : "
    if ignore_service:
        ignore_service_text += "On"
        data = "on"
    else:
        ignore_service_text += "Off"
        data = "off"
    only_owner = await get_only_owner(chat_id)
    if only_owner:
        only_owner = "Allow Only Owner"
        data2 = "True"
    else:
        only_owner = "Allow Admins Too"
        data2 = "False"
    buttons = [
        [
            InlineKeyboardButton(warn, callback_data=f"action+warn+{chat_id}"),
            InlineKeyboardButton(mute, callback_data=f"action+mute+{chat_id}"),
            InlineKeyboardButton(kick, callback_data=f"action+kick+{chat_id}"),
            InlineKeyboardButton(ban, callback_data=f"action+ban+{chat_id}")
        ],
        [
            InlineKeyboardButton(ignore_service_text, callback_data=f"action+{data}+{chat_id}")
        ],
        [
            InlineKeyboardButton(only_owner, callback_data=f"action+{data2}+{chat_id}")
        ]
    ]
    return buttons
