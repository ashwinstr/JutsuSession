
import asyncio

from typing import Union
from telegraph import Telegraph

tele_ = Telegraph()


async def conv(bot, chat_id: Union[int, str], msg_id: int, user_id: int):
    resp = None
    num = 1
    for one in range(20):
        await asyncio.sleep(0.5)
        msg_ = msg_id + one
        try:
            resp = await bot.get_messages(chat_id, msg_)
        except BaseException:
            num += 1
        if resp:
            break
    return resp


""" async def conv(bot, chat_id, msg_id, user_id):
    try:
        response = await asyncio.wait_for(converse(bot, chat_id, msg_id, user_id), timeout=15)
        return response
    except asyncio.TimeoutError:
        return "Timeout" """


def telegrapher(a_title: str, content: str) -> str:
    auth_name = tele_.create_account(short_name="Kakashi")
    resp = tele_.create_page(
        title=a_title,
        author_name=auth_name,
        author_url="https://t.me/xplugin",
        html_content=content,
    )
    link_ = resp["url"]
    return link_


def int_list(list_):
    intlist = []
    for one in list_:
        if one.isdigit():
            one = int(one)
        intlist.append(one)
    return intlist

async def username_list(list_):
    u_list = []
    for one in list_:
        u_list.append((await bot.get_users(one)).username)
    return u_list

