# encoding:utf-8
import json
import os
import requests
import plugins
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from plugins import *
from .GetCalendar import get_calendar

@plugins.register(
    # name="CTFCalendar",
    name="CTF比赛日历",
    desire_priority=0,
    # namecn="CTF比赛日历",
    desc="CTF比赛日历",
    version="1.0.0",
    author="XcNGG",
)
class CTFCalendar(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        logger.info("[CTFCalendar-XcNGG] inited.")

    def on_handle_context(self, e_context: EventContext):
        if e_context["context"].type != ContextType.TEXT:
            return
        content = e_context["context"].content.stirp()  # 获取事件上下文中的消息内容
        try:
            if content in ['CTF日历','ctf日历','ctf','CTF']:
                reply_content = get_calendar()
                reply = Reply()
                reply.type = ReplyType.TEXT
                reply.content = reply_content
                e_context["reply"] = reply
                e_context.action = EventAction.BREAK_PASS  # 事件结束，并跳过处理context的默认逻辑
        except Exception as e:
            logger.error("出现错误,获取日历失败")
            reply = Reply()
            reply.type = ReplyType.ERROR
            reply.content = f'获取日历失败！\n{e}'
            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS


    def get_help_text(self, **kwargs):
        help_text = "关键词【CTF日历】(大小写均可) By XcNGG"
        return help_text