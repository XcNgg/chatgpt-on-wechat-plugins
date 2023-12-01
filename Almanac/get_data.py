from datetime import datetime
import requests

def get_almanac(key,date):
    url = f"http://v.juhe.cn/laohuangli/d?date={date}&key={key}"
    response =  requests.get(url=url,timeout=3)
    if response.status_code == 200:
        response_data =response.json()
        result = response_data.get('result')
        yangli = result.get('yangli')
        yinli =  result.get('yinli')
        wuxing = result.get('wuxing')
        chongsha = result.get('chongsha')
        baiji = result.get('baiji')
        jishen = result.get('jishen')
        yi = result.get('yi')
        xiongshen = result.get('xiongshen')
        ji = result.get('ji')

        content = f"📅老黄历 [{yangli}]\n"
        content += f"【阴历】\t{yinli}\n"
        content += f"【五行】\t{wuxing}\n"
        content += f"【冲煞】\t{chongsha}\n"
        content += f"【百忌】\t{baiji}\n"
        content += f"【吉神】\t{jishen}\n"
        content += f"【凶神】\t{xiongshen}\n"
        content += f"【宜】\t{yi}\n"
        content += f"【忌】\t{ji}\n"
        return content
    else:
        return f"老黄历获取失败!{response.status_code}"


    # {
    #     "reason": "successed",
    #     "result": {
    #         "id": "4915",
    #         "yangli": "2023-11-27",
    #         "yinli": "癸卯(兔)年十月十五",
    #         "wuxing": "霹雳火 满执位",
    #         "chongsha": "冲羊(癸未)煞东",
    #         "baiji": "己不破券二比并亡 丑不冠带主不还乡",
    #         "jishen": "月德合 守日 天巫 福德 玉宇 玉堂",
    #         "yi": "开光 裁衣 安门 会亲友 安床 结网 理发",
    #         "xiongshen": "月厌 地火 九空 大煞 归忌",
    #         "ji": "嫁娶 冠笄 出行 祈福 安葬 伐木 入宅 移徙 出火 栽种 动土 上梁"
    #     },
    #     "error_code": 0
    # }



if __name__ == '__main__':
    key = "5caa483c89be598ddfa80ac738ce4b82"
    date = datetime.now().strftime("%Y-%m-%d")
    response = get_almanac(key,date)

