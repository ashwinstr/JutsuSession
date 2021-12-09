from pyrogram import Client, filters


@Client.on_message(
    filters.command(["start"])
    & filters.private
)
async def session_(bot, message):
    start_ = await bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}, let's start with string generation with you replying your APP_ID to this message.")
    
