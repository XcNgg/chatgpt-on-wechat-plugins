from datetime import datetime
import requests
from pprint import pprint
# https://api.aa1.cn/doc/perpetual-calendar.html
"""
dataSource	    是	string	LOCAL_PERPETUAL_CALENDAR
calendarType	是	string	(默认)日历类型:值必须为gregorian(阳历)或lunar(阴历)
data	        是	string	日期格式:yyyy-MM-dd
"""
url = "https://api.songzixian.com/api/perpetual-calendar"
day = datetime.now().strftime("%Y-%m-%d")
params = {
    "dataSource":"LOCAL_PERPETUAL_CALENDAR",
    "calendarType":"lunar",
    "data":day
}
print(day)
response = requests.get(url=url,params=params)
print(response.url)
pprint(response.json())
"""
{'code': 200,
 'data': {'gregorianInfo': {'date': '2023-11-18', 'dayOfWeek': '星期六'},
          'lunarInfo': {'chineseDate': '二〇二三年十月初六',
                        'chineseZodiac': '兔',
                        'day': 6,
                        'leapMonth': False,
                        'month': 10,
                        'year': 2023},
          'traditionalChineseInfo': {'currentJieQi': '',
                                     'dayStemBranch': '庚辰日',
                                     'monthStemBranch': '癸亥月',
                                     'nextJieQiName': '小雪',
                                     'nextJieQiTime': '2023-11-22 22:02:29',
                                     'yearStemBranch': '癸卯年'}},
 'message': '正常响应',
 'requestId': '1725722671976681472'}
"""