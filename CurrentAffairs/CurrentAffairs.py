# encoding:utf-8
import requests
import plugins
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from common.log import logger
from plugins import *


@plugins.register(
    name="时政要闻",
    desire_priority=0,
    # namecn="时政要闻",
    desc="输入关键词'时政要闻'即可获取今日时政要闻哦-By XcNGG",
    version="1.0",
    author="XcNGG",
)
class CurrentAffairs(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        logger.info("[CurrentAffairs-XcNGG] inited.")

    def on_handle_context(self, e_context: EventContext):
        content = e_context["context"].content  # 获取事件上下文中的消息内容
        if content == "时政要闻":  # 如果消息内容为 "摸鱼日历"
            url = "https://v.api.aa1.cn/api/60s-v3/?cc=%E5%9B%BD%E5%86%85%E8%A6%81%E9%97%BB?type=CurrentAffairs.jpg"
            reply = Reply()
            reply.type = ReplyType.IMAGE_URL
            reply.content = url

            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS  # 事件结束，并跳过处理context的默认逻辑


    def get_help_text(self, **kwargs):
        help_text = "关键词【时政要闻】By XcNGG"
        return help_text