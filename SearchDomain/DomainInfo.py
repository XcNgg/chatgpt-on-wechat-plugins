"""
基本功能 查看域名信息
"""
import requests
from my_fake_useragent import UserAgent
from common.log import logger

def domain_info(domain):
    content = ""
    try:
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
            "user-agent": UserAgent().random()
        }
        url = "https://api.uutool.cn/beian/icp/"
        data = {
            "domain": domain
        }
        response_data = requests.post(url, headers=headers, data=data).json()
        status = response_data.get('status',0)
        if status:
            # {'status': 1,
            #   'data':
            #       {'domain': 'baidu.com',
            #       'is_icp': 1,
            #       'icp_org': '北京百度网讯科技有限公司',
            #       'icp_no': '京ICP证030173号-1'
            #       },
            #   'req_id': 'e29115d357a76b547871'}
            content += f"【是否备案】{response_data.get('data', '未知').get('is_icp', '未知')}\n"
            content += f"【所属机构/个人】{response_data.get('data', '未知').get('icp_org', '未知')}\n"
            content += f"【备案号】{response_data.get('data', '未知').get('icp_no', '未知')}\n"
        else:
            content += f"【备案信息】获取失败\n"
            logger.info(content)
    except Exception as e:
        content += f"【备案信息】发送错误:{e}\n"
        logger.error(content)

    return content



if __name__ == '__main__':
    domain = 'baidu.com'
    print(domain_info(domain))
