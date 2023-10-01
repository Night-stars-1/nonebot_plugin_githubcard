'''
Author: Night-stars-1 nujj1042633805@gmail.com
Date: 2023-10-01 21:25:18
LastEditors: Night-stars-1 nujj1042633805@gmail.com
LastEditTime: 2023-10-01 21:33:54
Description: 

Copyright (c) 2023 by Night-stars-1, All Rights Reserved. 
'''
from nonebot.rule import T_State
from nonebot import get_driver
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment
from nonebot.adapters.console import MessageEvent
from .config import Config
from .data_source import get_github_reposity_information
from nonebot.plugin import on_regex

import re
from typing import Union

global_config = get_driver().config
config = Config(**global_config.dict())
github = on_regex(r"https?://github\.com/([^/]+/[^/]+)", priority=10, block=False)

def match_link_parts(link):
    pattern = r'https?://github\.com/([^/]+/[^/]+)'
    match = re.search(pattern, link)
    if match:
        return match.group(0)
    else:
        return None
    
@github.handle()
async def github_handle(event: Union[GroupMessageEvent, MessageEvent], state: T_State):
    url = match_link_parts(event.get_plaintext())
    imageUrl = await get_github_reposity_information(url)
    assert(imageUrl != "获取信息失败")
    await github.send(MessageSegment.image(imageUrl))
    
