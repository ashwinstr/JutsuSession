import traceback
import asyncio

from pyrogram import Client, filters
from jutsu import conv, Config


""" @Client.on_message(
    filters.command(["start"])
    & filters.private
    & filters.user([1013414037])
)
async def session_(bot, message):
    try:
        await bot.send_message(Config.LOG_CHANNEL_ID, f"User {message.from_user.mention} started the bot.")
        user_ = message.from_user.id
        bot_ = await bot.get_me()
        start_id = await bot.send_message(user_, f"Hello {message.from_user.first_name}, let's start with string generation with you replying your APP_ID to this message.")
        num = 1
        while True:
            await asyncio.sleep(0.5)
            try:
                app_id = await bot.get_messages(user_, start_id.message_id + num)
            except:
                pass
            num += 1
            if num > 20:
                break
        app_id = await conv(
            bot,
            chat_id=bot_.username,
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
        await bot.send_message(Config.LOG_CHANNEL_ID, f"#SESSION_BOT\n\n```{tb}```") """


@Client.on_message(
    filters.command(["app_id"])
    & filters.private,
    group=2
)
async def app_id_(bot, message):
    app_id = (message.text).split(" ", 1)[-1]
    user_ = message.from_user.id
    reply_to = message.message_id
    if not app_id.isdigit() or len(app_id) != 7:
        return await bot.send_message(user_, f"The provided input `{app_id}` is not valid.", replt_to_message_id=reply_to)
    app_id = int(app_id)
    Config.APP_ID = app_id
    await bot.send_message(user_, f"The provided input `{app_id}` set as APP_ID.", reply_to_message_id=reply_to)


@Client.on_message(
    filters.command(["api_hash"])
    & filters.private,
    group=1
)
async def api_hash_(bot, message):
    api_hash = (message.text).split(" ", 1)[-1]
    user_ = message.from_user.id
    reply_to = message.message_id
    Config.API_HASH = api_hash
    await bot.send_message(user_, f"The provided input `{api_hash}` set as API_HASH.", reply_to_message_id=reply_to)


@Client.on_message(
    filters.command(["generate"])
    & filters.private,
    group=0
)
async def generate_(bot, message):
    try:
        with Client(":memeory:", api_id=int(Config.APP_ID), api_hash=Config.API_HASH) as app:
            await app.send_message(message.from_user.id, f"#HU_STRING_SESSION generated successfully.\n\n```{await app.export_session_string()}```\n\n#KEEP_IT_SAFE.")
    except:
        await bot.send_message(message.chat.id, "Something went wrong, make sure your inputs are correct. If they are correct, since this bot is in beta phase, please report to @UX_xplugin_support.")
        tb = traceback.format_exc()
        await bot.send_message(Config.LOG_CHANNEL_ID, f"#SESSION_BOT\n\n```{tb}```")
