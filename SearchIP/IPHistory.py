import requests
import pprint
from my_fake_useragent import UserAgent
from common.log import logger
def ip_history(ip,max_data = 10):
    set_time = 4  # 超时时间
    content = ""
    try:
        headers = {
            "authority": "api.pearktrue.cn",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "origin": "https://api.aa1.cn",
            "pragma": "no-cache",
            "referer": "https://api.aa1.cn/",
            "sec-ch-ua": "^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": UserAgent().random()
        }
        url = "https://api.pearktrue.cn/api/website/sameip/"
        params = {
            "ip": ip
        }

        response_data = requests.get(url, headers=headers, params=params,timeout=set_time).json()
        if response_data['code'] == 200:
            content += f"【历史解析】共{response_data['count']}条"
            if len(response_data['data']) > max_data:
                content += f"(以下仅展示{max_data}条)\n"
            for history in response_data['data'][:max_data]:
                content += f"{history['domain']} | {history['time'].replace('----', '->')}\n"
        else:
            content += f"【历史解析】{response_data['msg']} | Http状态:{response_data['code']}\n"
            logger.info(content)

    except requests.exceptions.ReadTimeout:
        # requests.exceptions.ReadTimeout:HTTPSConnectionPool(host='api.pearktrue.cn', port=443): Read timed out.
        content += f"【历史解析】请求超过({set_time}秒),建议稍后再试\n"
        logger.error(content)

    except Exception as e:
        content += f"【历史解析】发生错误:{e}\n"
        logger.error(content)

    return content
    # pprint.pprint(response.json())
    # return response.json()


if __name__ == '__main__':
    content = ""
    ip = "123.11.15.14"
    content += ip_history(ip,max_data=15)
    print(content)


"""
{'api_source': '官方API网:https://api.pearktrue.cn/',
 'code': 200,
 'count': 100,
 'data': [{'domain': 'baidu.cn', 'time': '20190604----20231119'},
          {'domain': 'www.zz666.com', 'time': '20220722----20231119'},
          {'domain': 'zz666.com', 'time': '20220724----20231119'},
          {'domain': '3365.com', 'time': '20220804----20231119'},
          {'domain': '4233.com', 'time': '20220823----20231119'},
		  .....
 'ip': '39.156.66.10',
 'msg': '查询成功'}
"""

