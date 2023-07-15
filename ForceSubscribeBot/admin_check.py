import asyncio 

from pyrogram import Client , filters, enums


# Create an instance of the Pyrogram client

# Define the admin_check function
async def admin_check(client, message, user_id=None, callback_query=None):
    if not user_id:
        user_id = message.from_user.id
    bot_id = (await client.get_me()).id
    if message.chat.type not in [enums.ChatType.SUPERGROUP, enums.ChatType.GROUP]:
        await message.reply_text("This command can only be used in groups.", quote=True)
        return False
    chat_member = await client.get_chat_member(message.chat.id, user_id)
    bot_chat_member = await client.get_chat_member(message.chat.id, bot_id)
    if bot_chat_member.status != enums.ChatMemberStatus.ADMINISTRATOR:
        text = "Please make me an admin with ban power and try again!"
        if callback_query:
            await callback_query.answer(text, show_alert=True)
        else:
            await message.reply_text(text)
        return False
    if chat_member.status not in (enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR):
        text = "This command is only for admins!"
        if callback_query:
            await callback_query.answer(text, show_alert=True)
        else:
            await message.reply_text(text)
        return False
    return True

# Define a command handler
@Client.on_message(filters.command("test"))
async def test_command(client, message):
    # Call the admin_check function
    is_admin = await admin_check(client, message)
    if is_admin:
        await message.reply_text("You are an admin!")


