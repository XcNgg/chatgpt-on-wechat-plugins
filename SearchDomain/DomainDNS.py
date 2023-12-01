"""
    查看域名DNS记录
"""
import requests
from my_fake_useragent import UserAgent
from common.log import logger


# 公用免费DNS
public_dns_server ={
    "114.114.114.114": "电信联通移动全国通用DNS",
    "114.114.115.115": "电信联通移动全国通用DNS",
    "114.114.114.119": "电信联通移动全国通用DNS",
    "114.114.115.119": "电信联通移动全国通用DNS",
    "114.114.114.110": "电信联通移动全国通用DNS",
    "114.114.115.110": "电信联通移动全国通用DNS",
    "223.5.5.5": "阿里DNS",
    "223.6.6.6": "阿里DNS",
    "180.76.76.76": "百度DNS",
    "8.8.8.8": "谷歌DNS",
    "8.8.4.4": "谷歌DNS",
    "119.29.29.29":"腾讯DNS",
    "182.254.116.116": "腾讯备用DNS",
    "180.184.1.1": "字节跳动DNS",
    "180.184.2.2": "字节跳动DNS",
    "101.226.4.6": "360安全DNS(电信/铁通/移动)",
    "218.30.118.6": "360安全DNS(联通)",
    "1.2.4.8":"CNNIC中国互联网信息中心DNS"
}


def domain_dns(domain,dns_server="1.2.4.8"):
    """
        查看域名DNS记录
        {
          "dns": "114.114.114.114",
          "type": "A",
          "domain": "www.baidu.com",
          "state": true,
          "record": [
            {
              "ip": "180.101.50.188",
              "ttl": 125
            },
            {
              "ip": "180.101.50.242",
              "ttl": 125
            }
          ]
        }
    """
    content = ""
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://www.ip33.com",
        "Pragma": "no-cache",
        "Referer": "http://www.ip33.com/",
        "User-Agent": UserAgent().random()
    }
    url = "http://api.ip33.com/dns/resolver"
    data = {
        "domain": domain,
        "dns": dns_server,
        "type": "A",
    }
    try:
        response_data = requests.post(url=url, headers=headers, data=data, verify=False).json()
        if isinstance(response_data, str):
            content += f"【DNS信息】:获取错误：{response_data}\n"
            logger.info(content)
        else:
            content += f"【DNS信息】:\n"
            content += f"  -DNS服务器:{public_dns_server.get(response_data.get('dns',dns_server))}:{response_data.get('dns',dns_server)}\n"
            records = response_data.get('record')
            if len(records) > 0:
                for record in records:
                    content += f"  -A记录:[ip:{record.get('ip')} | ttl:{record.get('ttl')}]\n"
    except Exception as e:
        content += f'【DNS信息】:发生错误:{e}\n'
        logger.error(content)

    return content


if __name__ == '__main__':
    domain = 'baidu.com'
    content = ''
    dns_info = domain_dns(domain)
    content += dns_info
    print(content)


