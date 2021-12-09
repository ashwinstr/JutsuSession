
import asyncio

from typing import Union


async def conv(bot, chat_id: Union[int, str], msg_id: int, user_id: int):
    resp = None
    while True:
        await asyncio.sleep(0.5)
        try:
            resp = await bot.get_messages(chat_id, int(msg_id + 1))
        except:
            pass
        if resp is not None:
            break
    return resp
