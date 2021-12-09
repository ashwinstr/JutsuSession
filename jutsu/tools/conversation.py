import time
import asyncio

from typing import Union

from pyrogram import filters, Client

async def conv(bot, chat_id: Union[int, str], msg_id: int, user_id: int):
    while True:
        await asyncio.sleep(0.1)
        try:
            resp = await bot.get_messages(chat_id, (msg_id + 1))
            await bot.send_read_acknowledge(chat_id, (msg_id + 1))
        except:
            pass
        if resp:
            if resp.from_user.id == user_id:
                break
    return resp
