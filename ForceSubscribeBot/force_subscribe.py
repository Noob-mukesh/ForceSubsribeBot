from pyrogram import Client, filters
from pyrogram.types import Message
from ForceSubscribeBot.admin_check import admin_check
from pyrogram.errors import UsernameInvalid, PeerIdInvalid, UserNotParticipant
from ForceSubscribeBot.database.chats_sql import get_force_chat, change_force_chat, get_only_owner
from pyrogram.enums import ChatMemberStatus

@Client.on_message(filters.text & filters.command(["fsub", "forcesubscribe"]))
async def fsub(bot, msg: Message):
    chat_id = msg.chat.id
    bot_id = (await bot.get_me()).id
    success = await admin_check(bot, msg)
    if not success:
        return
    if len(msg.command) == 1:
        force_chat = await get_force_chat(chat_id)
        if force_chat:
            chat = await bot.get_chat(force_chat)
            mention = '@' + chat.username if chat.username else f"{chat.title} ({chat.id})"
            await msg.reply(f"**ᴄᴜʀʀᴇɴᴛ ғᴏʀᴄᴇ sᴜʙsʀɪʙᴇ ᴄʜᴀᴛ ** ɪs: {mention} \n\nᴄᴏᴜʟᴅ ʙᴇ ᴄʜᴀɴɢᴇᴅ ᴜsɪɴɢ `/forcesubscribe new_chat_id`")
        else:
            await msg.reply("ɴᴏ ғᴏʀᴄᴇ sᴜʙsʀɪʙᴇ ᴄʜᴀᴛ sᴇᴛ•! \n\nᴄᴏᴜʟᴅ ʙᴇ sᴇᴛ ᴜsɪɴɢ `/forcesubscribe chat_id`")
    else:
        creator = True if (await bot.get_chat_member(chat_id, msg.from_user.id)).status ==ChatMemberStatus.OWNER else False
        only_owner = await get_only_owner(chat_id)
        if only_owner and not creator:
            await msg.reply("ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴄʜᴀɴɢᴇ ғᴏʀᴄᴇ sᴜʙsʀɪʙᴇ ᴄʜᴀᴛ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ ʙᴀʙʏ.")
            return
        to_be_chat = msg.command[1]
        try:
            bot_chat_member = await bot.get_chat_member(to_be_chat, bot_id)
        except (UsernameInvalid, PeerIdInvalid):
            await msg.reply(
                "Uɴsᴜᴄᴄᴇsғᴜʟ:( \n\nᴘᴏssɪʙʟᴇ ʀᴇᴀsᴏɴ ᴄᴏᴜʟᴅ ʙᴇ: \n\n"
                "1) ɪ ʜᴀᴠᴇɴ'ᴛ ʙᴇᴇɴ ᴀᴅᴅᴇᴅ ᴛʜᴇʀᴇ. \n"
                "2) ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ chat_id/username ɪs ɪɴᴠᴀʟɪᴅ. \n"
                "3) ɪ ʜᴀᴠᴇ ʙᴇᴇɴ ᴅᴇᴍᴏᴛᴇᴅ ᴛʜᴇʀᴇ. \n"
                "4) ʏᴏᴜ ʜᴀᴠᴇ ᴘʀᴏᴠɪᴅᴇᴅ ʟɪɴᴋ ɪɴsᴛᴇᴀᴅ ᴏғ ᴜsᴇʀɴᴀᴍᴇ/chat_id. \n\n"
                "Pʟᴇᴀsᴇ ʀᴇ-ᴄʜᴇᴀᴋ ᴀʟʟ ᴛʜɪs 3 ᴛʜɪɴɢs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ʙᴀʙʏ"
                "Iғ sᴛɪʟʟ ʜᴀᴠᴇ ɪssᴜᴇ ᴛʜᴇɴ ᴠɪsɪᴛ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ @the_support_chat."
            )
            return
        except ValueError as e:
            await msg.reply(f"sᴇʀɪᴏᴜsʟʏ \n\n{str(e)}")
            return
        except UserNotParticipant:
            await msg.reply(f"ɪ ʜᴀᴠᴇɴ'ᴛ ʙᴇᴇɴ ᴀᴅᴅᴇᴅ ᴛʜᴇʀᴇ.")
            return
        if bot_chat_member.status ==ChatMemberStatus.ADMINISTRATOR:
            to_be_chat_id = (await bot.get_chat(to_be_chat)).id
            await change_force_chat(chat_id, to_be_chat_id)
            await msg.reply("sᴜᴄᴇssғᴜʟ. Nᴏᴡ ɪ'ʟʟ ᴍᴜᴛᴇ ᴘᴇᴏᴘʟᴇ ᴡʜᴏ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴛʜᴀᴛ ᴄʜᴀᴛ ʙᴀʙʏ . \n\nᴜsᴇ  /settings ᴛᴏ ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs.")
        else:
            await msg.reply("ᴘʟᴇᴀsᴇ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴛʜᴇʀᴇ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ʙᴀʙʏ ᴠɪsɪᴛ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ @the_support_chat !")
