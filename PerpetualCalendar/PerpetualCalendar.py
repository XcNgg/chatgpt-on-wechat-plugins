import requests  # 导入用于发送 HTTP 请求的库
import json  # 导入用于处理 JSON 数据的库
import re  # 导入用于正则表达式匹配的库
import plugins  # 导入自定义的插件模块
from bridge.reply import Reply, ReplyType  # 导入用于构建回复消息的类
from plugins import *  # 导入其他自定义插件
from config import conf  # 导入配置文件
from datetime import datetime


@plugins.register(
    name="万年历",  # 插件的名称
    desire_priority=1,  # 插件的优先级
    hidden=False,  # 插件是否隐藏
    desc="万年历",  # 插件的描述
    version="1.0",  # 插件的版本号
    author="XcNGG",  # 插件的作者
)
class PerpetualCalendar(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        logger.info("[Almanac-XcNGG] inited")  # 初始化插件时打印一条消息

    def on_handle_context(self, e_context: EventContext):
        content = e_context["context"].content  # 获取事件上下文中的消息内容
        url = "https://api.songzixian.com/api/perpetual-calendar"
        day = datetime.now().strftime("%Y-%m-%d")
        """
        dataSource	    是	string	LOCAL_PERPETUAL_CALENDAR
        calendarType	是	string	(默认)日历类型:值必须为gregorian(阳历)或lunar(阴历)
        data	        是	string	日期格式:yyyy-MM-dd
        """
        params = {
            "dataSource": "LOCAL_PERPETUAL_CALENDAR",
            "calendarType": "gregorian",
            "data": day
        }
        if content == "阳历":  # 如果消息内容为 "阳历"
            response = requests.get(url=url, params=params).json()
            if response.get('code',500) == 200:
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
                data = response.get('data')
                gregorianInfo = data.get('gregorianInfo')
                date = gregorianInfo.get('date')
                dayOfWeek = gregorianInfo.get('dayOfWeek')
                lunarInfo = data.get('lunarInfo')
                chineseDate = lunarInfo.get('chineseDate')
                chineseZodiac = lunarInfo.get('chineseZodiac')
                traditionalChineseInfo = data.get('traditionalChineseInfo')
                currentJieQi = traditionalChineseInfo.get('currentJieQi')
                yearStemBranch = traditionalChineseInfo.get('yearStemBranch')
                monthStemBranch = traditionalChineseInfo.get('monthStemBranch')
                dayStemBranch = traditionalChineseInfo.get('dayStemBranch')
                nextJieQiName = traditionalChineseInfo.get('nextJieQiName')
                nextJieQiTime = traditionalChineseInfo.get('nextJieQiTime')

                result = f"""📅阳历【{date}】
- {chineseDate} | {dayOfWeek} | {chineseZodiac}年
- {yearStemBranch} · {monthStemBranch} · {dayStemBranch}
- 今日节气:【{currentJieQi}】
- 下个节气:【{nextJieQiTime}】-【{nextJieQiName}】
"""
                reply = Reply()
                reply.type = ReplyType.TEXT
                reply.content = result
                e_context["reply"] = reply
                e_context.action = EventAction.BREAK_PASS


#             elif content == "阳历":  # 如果消息内容为 "阳历"
#                 response = requests.get(url=url, params=params).json()
#                 if response.get('code', 500) == 200:
#                     """
#                     {'code': 200,
#                      'data': {'gregorianInfo': {'date': '2023-12-30', 'dayOfWeek': '星期六'},
#                               'lunarInfo': {'chineseDate': '二〇二三年冬月十八',
#                                             'chineseZodiac': '兔',
#                                             'day': 18,
#                                             'leapMonth': False,
#                                             'month': 11,
#                                             'year': 2023},
#                               'traditionalChineseInfo': {'currentJieQi': '',
#                                                          'dayStemBranch': '壬戌日',
#                                                          'monthStemBranch': '甲子月',
#                                                          'nextJieQiName': '小寒',
#                                                          'nextJieQiTime': '2024-01-06 04:49:09',
#                                                          'yearStemBranch': '癸卯年'}},
#                      'message': '正常响应',
#                      'requestId': '1725725750474182656'}
#                     """
#                     data = response.get('data')
#                     gregorianInfo = data.get('gregorianInfo')
#                     date = gregorianInfo.get('date')
#                     dayOfWeek = gregorianInfo.get('dayOfWeek')
#                     lunarInfo = data.get('lunarInfo')
#                     chineseDate = lunarInfo.get('chineseDate')
#                     chineseZodiac = lunarInfo.get('chineseZodiac')
#                     traditionalChineseInfo = data.get('traditionalChineseInfo')
#                     currentJieQi = traditionalChineseInfo.get('currentJieQi')
#                     yearStemBranch = traditionalChineseInfo.get('yearStemBranch')
#                     monthStemBranch = traditionalChineseInfo.get('monthStemBranch')
#                     dayStemBranch = traditionalChineseInfo.get('dayStemBranch')
#                     nextJieQiName = traditionalChineseInfo.get('nextJieQiName')
#                     nextJieQiTime = traditionalChineseInfo.get('nextJieQiTime')
#
#                     result = f"""📅阳历【{date}】
# -{chineseDate}|{dayOfWeek}|{chineseZodiac}年
# - {yearStemBranch} · {monthStemBranch} · {dayStemBranch}
# - 今日节气:{currentJieQi}
# - 下个节气:{nextJieQiName}({nextJieQiTime})
#                     """
#                     reply = Reply()
#                     reply.type = ReplyType.TEXT
#                     reply.content = result
#                     e_context["reply"] = reply
#                     e_context.action = EventAction.BREAK_PASS




    def get_help_text(self, **kwargs):
        help_text = "关键词【阳历】By XcNgg"
        return help_text
