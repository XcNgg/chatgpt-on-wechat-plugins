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
    # name="SearchICP",
    name="域名查询",
    desire_priority=0,
    # namecn="备案查询",
    desc="输入关键词(注意小写)'icp baidu.com'即可查询ICP哦-By XcNGG",
    version="1.2",
    author="XcNGG",
)
class SearchICP(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        logger.info("[SearchICP-XcNGG] inited.")
        self.headers = {

        }

    def on_handle_context(self, e_context: EventContext):
        content = e_context["context"].content  # 获取事件上下文中的消息内容
        try:
            if content.startswith("icp "):
                domain = content.split(' ')[-1]
                headers = {
                    "authority": "api.uutool.cn",
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "cache-control": "no-cache",
                    "origin": "https://uutool.cn",
                    "pragma": "no-cache",
                    "referer": "https://uutool.cn/",
                    "sec-ch-ua": "^\\^Google",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "^\\^Windows^^",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
                }
                url = "https://api.uutool.cn/beian/icp/"
                data = {
                    "domain": domain
                }

                response = requests.post(url, headers=headers, data=data).json()

                status = response.get('status',0)

                if status == 1:
                    logger.info(f"查询icp {domain} 成功")
                    reply = Reply()
                    reply.type = ReplyType.TEXT
                    reply.content =  f"【🔎域名: {domain}】\n"
                    # {'status': 1,
                    #   'data':
                    #       {'domain': 'baidu.com',
                    #       'is_icp': 1,
                    #       'icp_org': '北京百度网讯科技有限公司',
                    #       'icp_no': '京ICP证030173号-1'
                    #       },
                    #   'req_id': 'e29115d357a76b547871'}
                    reply.content += f"【是否备案】:{response.get('data','未知').get('is_icp','未知')}\n"
                    reply.content += f"【所属机构/个人】:{response.get('data','未知').get('icp_org','未知')}\n"
                    reply.content += f"【备案号】:{response.get('data','未知').get('icp_no','未知')}\n"
                    reply.content += f"【梯子信息】:{self.is_extranet(domain)}\n"
                    reply.content += f"【注册信息】:{self.can_register(domain)}"
                    e_context["reply"] = reply
                    e_context.action = EventAction.BREAK_PASS  # 事件结束，并跳过处理context的默认逻辑
                else:
                    logger.info(f"查询icp {domain} 失败")
                    reply = Reply()
                    reply.type = ReplyType.TEXT
                    reply.content = f"【🔎域名: {domain}】查询失败！"
                    e_context["reply"] = reply
                    e_context.action = EventAction.BREAK_PASS  # 事件结束，并跳过处理context的默认逻辑

        except Exception as e:
            logger.error("出现错误,查询ICP失败！")
            reply = Reply()
            reply.type = ReplyType.TEXT
            reply.content = f'[ERROR]\n查询ICP失败！\n{e}'
            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS


    def is_extranet(self,domain):
        """
            查看域名是否被墙
            {"success":true,"domain":"google.com","msg":"被墙了"}
        """
        url = "https://api.vvhan.com/api/qiang?url=" + domain
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
        try:
            response = requests.get(url=url,headers=headers).json()
            if response.get('success',False):
                return response.get('msg')
            else:
                return '获取失败'
        except Exception as e:
            return f'[ERROR] {e}'

    def can_register(self, domain):
        """
            查看域名是否可以注册
            {"success":true,"domain":"google.com","message":"不可注册"}
        """
        url = "https://api.vvhan.com/api/dm"
        params = {
            "url": domain
        }
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
        try:
            response = requests.get(url=url, headers=headers,params=params).json()
            if response.get('success', False):
                return response.get('message')
            else:
                return '获取失败'
        except Exception as e:
            return f'[ERROR] {e}'




    def get_help_text(self, **kwargs):
        help_text = "关键词【icp baidu.com】(注意小写)By XcNGG"
        return help_text