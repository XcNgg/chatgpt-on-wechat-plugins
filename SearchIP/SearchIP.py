# encoding:utf-8
import json
import os
import requests
import plugins
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from common.log import logger
from plugins import *
from .IPInfo import ip_info
from .IPHistory import ip_history

@plugins.register(
    # name="SearchIP",
    name="IP查询",
    desire_priority=0,
    # namecn="IP归属",
    desc="输入关键词(注意小写)'ip xx.xx.xx.xx'即可查询IP归属地哦-By XcNGG",
    version="1.2.1",
    author="XcNGG",
)
class SearchIp(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        logger.info("[SearchIP-XcNGG] inited.")

    def on_handle_context(self, e_context: EventContext):
        content = e_context["context"].content  # 获取事件上下文中的消息内容
        try:
            if content.startswith("ip "):
                ip = content.split(' ')[-1]
                reply = Reply()
                reply.type = ReplyType.TEXT
                reply.content = f"【🔎 {ip}】\n"
                # IP基本信息
                reply.content += ip_info(ip)
                # 历史IP DNS 解析记录
                max_data = 15 # 最大展示条数
                reply.content += ip_history(ip,max_data=max_data)
                e_context["reply"] = reply
                e_context.action = EventAction.BREAK_PASS  # 事件结束，并跳过处理context的默认逻辑

        except Exception as e:
            logger.error("出现错误,查询IP失败！")
            reply = Reply()
            reply.type = ReplyType.TEXT
            reply.content = f'[ERROR]\nIP查询失败！\n{e}'
            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS


    def get_help_text(self, **kwargs):
        help_text = "关键词【ip 8.8.8.8】(注意小写)By XcNGG"
        return help_text