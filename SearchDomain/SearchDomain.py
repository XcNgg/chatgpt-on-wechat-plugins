# encoding:utf-8
import json
import os
import requests
import plugins
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from common.log import logger
from plugins import *

from .DomainInfo import domain_info
from .IsExtranet import is_extranet
from .DomainDNS import domain_dns
from .CanRegister import can_register


@plugins.register(
    # name="SearchDomain",
    name="域名查询",
    desire_priority=0,
    # namecn="备案查询",
    desc="输入关键词(注意小写)'domain baidu.com'即可查询域名信息哦-By XcNGG",
    version="1.4",
    author="XcNGG",
)
class SearchDomain(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        logger.info("[SearchDomain-XcNGG] inited.")

    def on_handle_context(self, e_context: EventContext):
        content = e_context["context"].content
        reply = Reply()
        reply.type = ReplyType.TEXT
        # 获取事件上下文中的消息内容
        try:
            if content.startswith("domain "):
                domain = content.split(' ')[-1]
                reply.content = f"【🔎域名: {domain}】\n"
                reply.content += domain_info(domain)
                reply.content += can_register(domain)
                reply.content += is_extranet(domain)
                reply.content += domain_dns(domain)

                e_context["reply"] = reply
                e_context.action = EventAction.BREAK_PASS  # 事件结束，并跳过处理context的默认逻辑
        except Exception as e:
            reply.content = f"【查询域名】:发送错误:{e}\n"

    def get_help_text(self, **kwargs):
        help_text = "关键词【domain baidu.com】(注意小写)By XcNGG"
        return help_text