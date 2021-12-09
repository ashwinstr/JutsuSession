
import asyncio

from typing import Union


async def converse(bot, chat_id: Union[int, str], msg_id: int, user_id: int):
    resp = None
    while resp is None:
        await asyncio.sleep(0.5)
        try:
            resp = await bot.get_messages(chat_id, int(msg_id + 1))
        except:
            resp = None
    return resp


async def conv(bot, chat_id, msg_id, user_id):
    try:
        response = await asyncio.wait_for(converse(bot, chat_id, msg_id, user_id), timeout=15)
        return response
    except asyncio.TimeoutError:
        return "Timeout"
