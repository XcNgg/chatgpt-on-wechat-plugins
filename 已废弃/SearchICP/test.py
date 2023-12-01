"""
基本功能 查看域名信息
"""
import requests
domain = 'baidu.com'
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
print(response)