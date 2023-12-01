import requests
from my_fake_useragent import UserAgent
from common.log import logger

def ip_info(ip):
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
        url = f"https://api.uutool.cn/ip/cz/{ip}"
        response = requests.get(url, headers=headers).json()
        status = response.get('status', 0)
        if status:
            content += f"【所属地区】{response.get('data', '未知地区').get('area', '未知地区')}\n"
            content += f"【更多信息】{response.get('data', '未知').get('extra', '未知')}\n"
        else:
            content += f"【请求状态】请求失败\n"
            content += f"【所属地区】未知地区\n"
            content += f"【更多信息】未知信息\n"
            logger.info(content)
    except Exception as e:
        content += f"【请求错误】发生错误{e}\n"
        logger.error(content)
    return content



if __name__ == '__main__':
    ip = "123.23.2.3"
    content = f"【🔎 {ip}】\n"
    content += ip_info(ip)
    print(content)