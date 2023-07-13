from Data import Data
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
from pyrogram.errors.exceptions import UserNotParticipant
from ForceSubscribeBot.database.chats_sql import (
    get_action,
    change_action,
    get_force_chat,
    get_ignore_service,
    toggle_ignore_service,
    get_only_owner,
    toggle_only_owner
)
from ForceSubscribeBot.admin_check import admin_check
from ForceSubscribeBot.settings import action_markup


# Callbacks

@Client.on_callback_query()
async def _callbacks(bot, callback_query):
    user = await bot.get_me()
    user_id = callback_query.from_user.id
    mention = user.mention
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == 'home':
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.message_id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.START.format(callback_query.from_user.mention, mention),
                reply_markup=InlineKeyboardMarkup(Data.buttons)
            )
    elif query == "about":
        chat_id = callback_query.message.chat.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons)
        )

    elif query == "help":
        chat_id = callback_query.message.chat.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="**ʜᴇʀᴇ's ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ? **\n" + Data.HELP,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )
    elif query.startswith("action"):
        success = await admin_check(bot, callback_query.message, user_id, callback_query)
        if not success:
            return
        main = query.split("+")[1].lower()
        chat_id = int(query.split("+")[2])
        only_owner = await get_only_owner(chat_id)
        creator = True if (await bot.get_chat_member(chat_id, callback_query.from_user.id)).status == "creator" else False
        if only_owner and not creator:
            await callback_query.answer("ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴄʜᴀɴɢᴇ ᴄʜᴀᴛ sᴇᴛᴛɪɴɢs ɪɴ ᴛʜɪs ᴄʜᴀᴛ ғ**.", show_alert=True)
            return
        if main in ["on", "off"]:
            current_bool = await get_ignore_service(chat_id)
            if main == "on":
                damn = True
            else:
                damn = False
            if current_bool == damn:
                if current_bool:
                    await toggle_ignore_service(chat_id, False)
                    await callback_query.answer("ɴᴏᴡ ᴛʜᴇ sᴇʀᴠɪᴄᴇ  ᴍᴇssᴀɢᴇs ᴡɪʟʟ ʙᴇ ᴄʜᴇᴀᴋᴇᴅ ᴛᴏᴏ!", show_alert=True)
                else:
                    await toggle_ignore_service(chat_id, True)
                    await callback_query.answer(" ɴᴏᴡ  ᴛʜᴇ sᴇʀᴠɪᴄᴇ ᴍᴇssᴀɢᴇ ᴡɪʟʟ ɴᴏᴛ ʙᴇ ᴄʜᴇᴀᴋᴇᴅ▼", show_alert=True)
            # else:
            #     pass
        elif main in ["true", "false"]:
            creator = True if (await bot.get_chat_member(chat_id, callback_query.from_user.id)).status == "creator" else False
            if not creator:
                await callback_query.answer("ᴛʜɪs ɪs ᴀ sᴘᴇᴄɪᴀʟ sᴇᴛᴛɪɴɢs ᴀɴᴅ ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴄʜᴀɴɢᴇ ɪᴛ ʙᴀʙʏ.", show_alert=True)
                return
            current_bool = await get_only_owner(chat_id)
            if main == "true":
                damn = True
            else:
                damn = False
            if current_bool == damn:
                if current_bool:
                    await toggle_only_owner(chat_id, False)
                    await callback_query.answer("ɴᴏᴡ ᴀᴅᴍɪɴs ᴄᴀɴ  ᴄʜᴀɴɢᴇ ғsᴜʙ ᴄʜᴀᴛ ᴀɴᴅ sᴇᴛᴛɪɴɢs ᴛᴏᴏ¡", show_alert=True)
                else:
                    await toggle_only_owner(chat_id, True)
                    await callback_query.answer("ɴᴏᴡ ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ  ᴄʜᴀɴɢᴇ ғsᴜʙ ᴄʜᴀᴛ ᴀɴᴅ sᴇᴛᴛɪɴɢs!", show_alert=True)
        else:
            current_action = await get_action(chat_id)
            if main == current_action:
                await callback_query.answer(f"{main.capitalize()} ɪs ᴀʟʀᴇᴀᴅʏ ᴛʜᴇ ᴀᴄᴛɪᴏɴ ᴛʏᴘᴇ.", show_alert=True)
                return
            else:
                await change_action(chat_id, main)
        buttons = await action_markup(chat_id)
        await callback_query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    elif query.startswith("joined"):
        try:
            muted_user_id = int(query.split('+')[1])
        except IndexError:
            # Temporarily catch
            return
        chat_id = callback_query.message.chat.id
        bot_id = (await bot.get_me()).id
        force_chat = await get_force_chat(chat_id)
        bot_chat_member = await bot.get_chat_member(chat_id, bot_id)
        bot_chat_member2 = await bot.get_chat_member(force_chat, bot_id)
        chat = await bot.get_chat(force_chat)
        mention = '@'+chat.username if chat.username else 'the chat'
        if bot_chat_member.status != "administrator":
            await callback_query.answer(" ɪ 'ᴠᴇ ʙᴇᴇɴ ᴅᴇᴍᴏᴛᴇᴅ ғʀᴏᴍ  ᴛʜɪs ᴄʜᴀᴛ. I ᴄᴀɴ'ᴛ ᴜɴᴍᴜᴛᴇ ʏᴏᴜ ɴᴏᴡ. Sᴏʀʀʏ ʙᴀʙʏ ʟᴇᴀᴠɪɴɢ ᴄʜᴀᴛ", show_alert=True)
            await bot.send_message(chat_id, "I've been demoted here. Of no use then!")
            return
        if bot_chat_member2.status != "administrator":
            await callback_query.answer(" ɪ'ᴠᴇ ʙᴇᴇɴ ᴅᴇᴍᴏᴛᴇᴅ ғʀᴏᴍ ғᴏʀᴄᴇ sᴜʙsʀɪʙᴇ ᴄʜᴀᴛ.", show_alert=True)
            await bot.send_message(chat_id, "ɪ'ᴠᴇ ʙᴇᴇɴ ᴅᴇᴍᴏᴛᴇᴅ ғʀᴏᴍ ᴛʜᴇ sᴜʙsʀɪʙᴇ ᴄʜᴀᴛ. Oғ ɴᴏ ᴜsᴇ ᴄʜᴀᴛ. F** ʟᴇᴀᴠɪɴɢ ᴄʜᴀᴛ!")
            return
        not_joined = f"Join {mention} first then try!"
        try:
            if user_id == muted_user_id:
                await bot.get_chat_member(force_chat, user_id)
                await bot.unban_chat_member(chat_id, user_id)
                await callback_query.answer("ɢᴏᴏᴅ ʙᴀʙʏ . Nᴏᴡ ʏᴏᴜ ᴄᴀɴ sᴛᴀʀᴛ ᴄʜᴀᴛᴛɪɴɢ ᴘʀᴏᴘᴇʀʟʏ ɪɴ ɢʀᴏᴜᴘ ɴᴏᴡ. Tʜɴᴋs ғᴏʀ ᴊᴏɪɴɪɴɢ.", show_alert=True)
                await callback_query.message.delete()
            else:
                await callback_query.answer('This is not for u', show_alert=True)
        except UserNotParticipant:
            await callback_query.answer(not_joined, show_alert=True)
