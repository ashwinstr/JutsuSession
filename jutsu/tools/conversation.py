import time
import asyncio

from typing import Union

from pyrogram import filters, CLient
from pyrogram.filters import FIlter

async def conv(bot: Client, chat_id: Union[int, str], msg_id: int, mark_read: bool=True, filters: user_id):
    while True:
        await asyncio.sleep(0.1)
        try:
            resp = await bot.get_messages(chat_id, (msg_id + 1))
            await bot.send_read_acknowledge()
        except:
            pass
        if resp:
            if resp.from_user.id == user_id:
                break
    return resp
