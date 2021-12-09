import traceback

from pyrogram import Client, filters
from jutsu import conv, Config


@Client.on_message(
    filters.command(["start"])
    & filters.private
)
async def session_(bot, message):
    try:
        await bot.send_message(Config.LOG_CHANNEL_ID, f"User {message.from_user.mention} started the bot.")
        user_ = message.from_user.id
        start_id = await bot.send_message(user_, f"Hello {message.from_user.first_name}, let's start with string generation with you replying your APP_ID to this message.")
        app_id = await conv(
            chat_id=user_,
            msg_id=start_id.message_id,
            user_id=user_,
        )
        await bot.send_message(user_, f"{app_id}")
        APP_ID = int(app_id.text)
        if not isinstance(APP_ID, int) or len(APP_ID):
            return await bot.send_message(user_, "The APP_ID must be a 7 digit number. Please try again with /start.")
        start_hash = await bot.send_message(user_, "APP_ID received, now send API_HASH.")
        api_hash = await conv(
            bot,
            chat_id=message.chat.id,
            msg_id=start_hash.message_id,
            user_id=message.from_user.id,
        )
        API_HASH = api_hash.text
        try:
            with Client(":memeory:", api_id=int(APP_ID), api_hash=API_HASH) as app:
                app.send_message("me", f"#HU_STRING_SESSION generated successfully.\n\n```{app.export_session_string()}```\n\n#KEEP_IT_SAFE.")
        except:
            await bot.send_message(message.chat.id, "Something went wrong, make sure your inputs are correct. If they are correct, since this bot is in beta phase, please report to @UX_xplugin_support.")
    except:
        tb = traceback.format_exc()
        await bot.send_message(Config.LOG_CHANNEL_ID, f"#SESSION_BOT\n\n```{tb}```")