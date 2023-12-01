# encoding:utf-8
import json
import os
import requests
import plugins
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from common.log import logger
from plugins import *


@plugins.register(
    name="摸鱼日历",
    desire_priority=0,
    # namecn="摸鱼日历",
    desc="输入关键词'摸鱼日历'即可获取今日摸鱼日历哦-By XcNGG",
    version="1.0",
    author="XcNGG",
)
class FishCalendar(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        logger.info("[FishCalendar-XcNGG] inited.")

    def on_handle_context(self, e_context: EventContext):

        content = e_context["context"].content  # 获取事件上下文中的消息内容
        if content == "摸鱼日历":  # 如果消息内容为 "摸鱼日历"
            url = "https://api.vvhan.com/api/moyu?type=json"
            response = requests.get(url).json()
            status = response.get('success', False)
            if status:
                img_url = response.get('url', 'https://api.vvhan.com/api/moyu')
                logger.info(f"获取日历状态成功，今日日历：{img_url}")
                reply = Reply()
                reply.type = ReplyType.IMAGE_URL
                reply.content = img_url
                e_context["reply"] = reply
                e_context.action = EventAction.BREAK_PASS  # 事件结束，并跳过处理context的默认逻辑
            else:
                logger.log("获取日历状态失败")


    def get_help_text(self, **kwargs):
        help_text = "关键词【摸鱼日历】By XcNGG"
        return help_text