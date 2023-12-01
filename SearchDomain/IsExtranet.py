"""
    查看域名是否被墙
"""
import requests
from my_fake_useragent import UserAgent
from common.log import logger

def is_extranet(domain):
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

        url = "https://api.vvhan.com/api/qiang"
        params = {
            "url": domain
        }
        response = requests.get(url, headers=headers, params=params)
        response_data = response.json()
        if response_data.get('success',False):
            content += f"【梯子状态】{response_data['msg']}\n"
        else:
            content += f"【梯子状态】获取失败\n"
            logger.info(content)
    except Exception as e:
        content += f"【梯子状态】发生错误-{e}\n"
        logger.error(content)

    return content

if __name__ == '__main__':
    """
    {'success': True, 'domain': 'google.com', 'msg': '被墙了'}
    """
    domain = 'google.com'
    print(is_extranet(domain))

