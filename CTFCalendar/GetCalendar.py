import requests
import icalendar
from datetime import datetime, timedelta
from my_fake_useragent import UserAgent

def get_calendar():
    url = "https://api.ctfhub.com/User_API/Event/getAllICS"
    # 获取今天和最近7天的日期范围
    today = datetime.now().date()
    set_start_date = today - timedelta(days=3)
    set_end_date = today + timedelta(days=4)
    # 计数
    count = 0
    # 标题
    content = f"【CTF比赛日历】(仅近7日未结束或未开始的线上竞赛)\n"
    content += "-------------\n"
    response = requests.get(url=url,headers={'user-agent':UserAgent().random()})
    # 解析日历
    calendar = icalendar.Calendar.from_ical(response.text)
    # 遍历日历事件
    for event in calendar.walk('VEVENT'):
        start_date = event.get('dtstart').dt.date()
        end_date = event.get('DTEND').dt.date()
        summary = event.get('summary')
        # print(summary)
        # 检查事件是否在日期范围内
        if (start_date >= set_start_date and end_date <= set_end_date) and (end_date >= today):
            description = event.get('description')
            # 筛选线上的比赛
            if description.startswith('线上 '):
                url = event.get('url')
                # 在这里可以根据需要处理符合条件的日历事件
                # print('Summary:', summary)
                content += f"竞赛名称:《{summary}》\n"
                content += f"比赛描述: {description}\n"
                content += f"开始时间: {start_date}\n"
                content += f"结束时间: {end_date}\n"
                content += f"比赛链接: {url}\n"
                content += "-------------\n"
                count += 1
                # print(count)

    if count >0:
        content += f"近期共【{count}】场比赛,请及时关注！\n"
        content += "👍👍🏻👍🏼全部写出来奖励你大拇哥👍🏽👍🏾👍🏿"
    else:
        content += "当前数据源显示近期无比赛"

    print(content)
    return content


# 解析iCalendar文件
# calendar = icalendar.Calendar.from_ical(data)
#
# 遍历日历事件
# for event in calendar.walk('VEVENT'):
#     summary = event.get('summary')
#     start = event.get('dtstart').dt
#     end = event.get('dtend').dt
#     description = event.get('description')
#     url = event.get('url')
#
#     # 在这里可以根据需要处理日历事件的各个属性
#
#     print('Summary:', summary)
#     print('Start:', start)
#     print('End:', end)
#     print('Description:', description)
#     print('URL:', url)
#     print()

if __name__ == '__main__':
    get_calendar()