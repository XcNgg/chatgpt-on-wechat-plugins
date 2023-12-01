import requests

url = "https://v.api.aa1.cn/api/60s-v3/?cc=%E5%9B%BD%E5%86%85%E8%A6%81%E9%97%BB?type=CurrentAffairs.jpg"
response = requests.get(url)


with open('1.jpg','wb') as file:
    file.write(response.content)

