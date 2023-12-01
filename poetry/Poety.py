import plugins
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from plugins import *
from bridge import bridge
from common.expired_dict import ExpiredDict
from common import const
import os
from .test import get_data

@plugins.register(
    name="诗词",
    # name="linkai",
    desc="随机诗词",
    version="0.1",
    author="XcNGG",
    desire_priority=0, # 权重值
    # hidden = False, # 插件是否隐藏
)
class LinkAI(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        logger.info(f"[诗词] inited ")

    def on_handle_context(self, e_context: EventContext):
        """
        消息处理逻辑
        :param e_context: 消息上下文
        """
        if e_context["context"].type != ContextType.TEXT:
            return

        content = e_context["context"].content.strip()

        if content == "诗词":
            from_who, hitokoto, _from = get_data()
            response = f"{hitokoto} \n --{from_who} · 《{_from}》"

            reply = Reply()
            reply.type = ReplyType.TEXT
            reply.content = response

            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS  # 事件结束，并跳过处理context的默认逻辑

    def get_help_text(self, verbose=False, **kwargs):
        help_text = "关键词【诗词】"
        return help_text


