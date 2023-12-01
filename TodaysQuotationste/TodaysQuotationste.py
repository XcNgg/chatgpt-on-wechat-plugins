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
    # name="TodaysQuotationste",
    desire_priority=0,
    name="每日语录",
    desc="关键词'每日语录'-By XcNGG",
    version="1.1",
    author="XcNGG",
)
class TodaysQuotationste(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        logger.info("[TodaysQuotationste-XcNGG] inited.")

    def on_handle_context(self, e_context: EventContext):
        content = e_context["context"].content  # 获取事件上下文中的消息内容
        try:
            if content == "每日语录":
                headers = {
                    "authority": "api.vvhan.com",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "cache-control": "no-cache",
                    "pragma": "no-cache",
                    "sec-ch-ua": "^\\^Google",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "^\\^Windows^^",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "none",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
                }

                url = f"https://api.vvhan.com/api/en"
                response = requests.get(url, headers=headers).json()
                status = response.get('success',False)
                if status:
                    logger.info(f"查询[每日语录]成功")
                    reply = Reply()
                    reply.type = ReplyType.TEXT
                    month = response.get("data").get("month")
                    day = response.get("data").get("day")
                    zh = response.get("data").get("zh")
                    en = response.get("data").get("en")
                    reply.content =  f"💬【{month}-{day}】\n【CN】{zh} \n【En】{en}"
                    """
                    {
                        "success": true,
                        "data": {
                        "month": "Nov",
                        "day": "17",
                        "zh": "优质的表现始于积极的态度。",
                        "en": "Quality performance starts with a positive attitude. ",
                        "pic": "https://staticedu-wps.cache.iciba.com/image/1695961f05f79cb6bf630ce9747a189d.jpg"
                        }
                    }
                    """
                    e_context["reply"] = reply
                    e_context.action = EventAction.BREAK_PASS  # 事件结束，并跳过处理context的默认逻辑
                else:
                    logger.info(f"获取[每日语录]成功")
                    reply = Reply()
                    reply.type = ReplyType.TEXT
                    reply.content = f"获取[每日语录]失败"

                    e_context["reply"] = reply
                    e_context.action = EventAction.BREAK_PASS  # 事件结束，并跳过处理context的默认逻辑

        except Exception as e:
            logger.error("出现错误,获取[每日语录]失败")
            reply = Reply()
            reply.type = ReplyType.TEXT
            reply.content = f'[ERROR]\n获取[每日语录]失败！\n{e}'
            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS

    def get_help_text(self, **kwargs):
        help_text = "关键词【每日语录】By XcNGG"
        return help_text