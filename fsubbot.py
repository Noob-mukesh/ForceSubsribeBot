import Config
import logging
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid


logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


app = Client(
    ":memory:",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="ForceSubscribeBot"),
)


# Run Bot
if __name__ == "__main__":
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("ʏᴏᴜʀ API_ID/API_HASH ɪs ɴᴏᴛ ᴠᴀɪʟᴅ.")
    except AccessTokenInvalid:
        raise Exception("ʏᴏᴜʀ BOT_TOKEN ɪs ɴᴏᴛ ᴠᴀɪʟᴅ.")
    uname = app.get_me().username
    print(f"@{uname} ʙᴏᴛ ᴅᴇᴘʟᴏʏᴇᴅ sᴜᴄᴇssғᴜʟʟʏ ʙᴀʙʏ  ᴊᴏɪɴ  @mukeshbotzone !")
    idle()
    app.stop()
    print("ʙᴏᴛ sᴛᴏᴘᴘᴇᴅ .ʙᴀʙʏ!")
