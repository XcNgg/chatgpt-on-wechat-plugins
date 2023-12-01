"""
查看域名是否注册
"""
from my_fake_useragent import UserAgent
import requests
from common.log import logger


def can_register(domain):
    content = ""
    try:
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
        "user-agent": UserAgent().random()
        }

        url = "https://api.vvhan.com/api/dm"
        params = {
            "url": domain
        }
        response_data = requests.get(url=url, headers=headers,params=params).json()
        # print(response_data)
        if response_data.get('success',False):
            content += f"【注册信息】:{response_data['message']}\n"
        else:
            content +=f"【注册信息】:获取失败\n"
            logger.info(content)
    except Exception as e:
        content += f"【注册信息】:发生错误:{e}\n"
        logger.error(content)

    return content

if __name__ == '__main__':
    content = ''
    domain = '8.8.8.8'
    "{'success': True, 'domain': 'google', 'message': '不可注册'}"
    content += can_register(domain=domain)
    print(content)