from pyrogram import Client, filters


@Client.on_message(filters.text &  filters.command("id"))
async def id(_, msg):
    await msg.reply(f"ᴄʜᴀᴛ ɪᴅ ɪs : `{msg.chat.id}`", quote=True)
