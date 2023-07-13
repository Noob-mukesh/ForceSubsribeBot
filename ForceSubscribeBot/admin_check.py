
from pyrogram import types

async def admin_check(client, message, user_id=None, callback_query=None):
    if not user_id:
        user_id = message.from_user.id
    bot_id = (await client.get_me()).id
    if message.chat.type not in [types.ChatType.SUPERGROUP, types.ChatType.GROUP]:
        await message.reply_text("This command can only be used in groups.", quote=True)
        return False
    chat_member = await client.get_chat_member(message.chat.id, user_id)
    bot_chat_member = await client.get_chat_member(message.chat.id, bot_id)
    if bot_chat_member.status != types.ChatMemberStatus.ADMINISTRATOR:
        text = "Please make me an admin with ban power and try again!"
        if callback_query:
            await callback_query.answer(text, show_alert=True)
        else:
            await message.reply_text(text)
        return False
    if chat_member.status not in (types.ChatMemberStatus.CREATOR, types.ChatMemberStatus.ADMINISTRATOR):
        text = "This command is only for admins!"
        if callback_query:
            await callback_query.answer(text, show_alert=True)
        else:
            await message.reply_text(text)
        return False
    return True
