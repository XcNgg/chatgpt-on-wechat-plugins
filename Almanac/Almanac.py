import plugins  # 导入自定义的插件模块
from plugins import *  # 导入其他自定义插件
from config import conf  # 导入配置文件
from datetime import datetime
from .get_data import get_almanac
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from common.log import logger


@plugins.register(
    name="黄历",  # 插件的名称
    desire_priority=1,  # 插件的优先级
    hidden=False,  # 插件是否隐藏
    desc="黄历",  # 插件的描述
    version="1.0",  # 插件的版本号
    author="XcNGG",  # 插件的作者
)
class Almanac(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        logger.info("[Almanac-XcNGG] inited")  # 初始化插件时打印一条消息

    def on_handle_context(self, e_context: EventContext):
        if e_context["context"].type != ContextType.TEXT:
            return
        content = e_context["context"].content.strip()
        if content == "黄历":
            almanac_key = conf().get("almanac_key")
            date = datetime.now().strftime("%Y-%m-%d")
            reply_content = get_almanac(key=almanac_key,date=date)
            reply = Reply()
            reply.type = ReplyType.TEXT
            reply.content = reply_content
            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS


    def get_help_text(self, **kwargs):
        help_text = "关键词【黄历】By XcNgg"
        return help_text
