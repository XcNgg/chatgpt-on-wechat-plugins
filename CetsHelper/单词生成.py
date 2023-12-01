import json
import random
import os
from datetime import datetime



def get_words():
    # 生成新的json文件名
    date = datetime.now().strftime('%Y-%m-%d')
    new_file_name = f"data/{date}.json"
    if not os.path.exists(new_file_name):
        # 读取total.json文件
        with open('data/total.json', 'r',encoding='utf-8') as f:
            data = json.load(f)

        if len(data) >=20:
            # 从data中随机选择20个单词
            random_words = random.sample(data, 20)
        else:
            random_words = random.sample(data, len(data))

        # 将随机选择的单词写入新的json文件
        with open(new_file_name, 'w',encoding='utf-8') as f:
            json.dump(random_words, f)
        # 从total.json中删除随机选择的单词
        data = [word for word in data if word not in random_words]
        # 将更新后的data写入total.json文件
        with open('src.json', 'w',encoding='utf-8') as f:
            json.dump(data, f)

    with open(new_file_name, 'r',encoding='utf-8') as f:
        data = json.load(f)


    content = f"{date}🕖 [今日单词]✅\n"
    for index,d in enumerate(data,1):
        content += f"{index}. 【{d['word']}】\n"
        content += f"mean:{d['mean']} {d['phonetic_symbol']}\n"

    content += "今天也是元气满满的一天！✨"

    print(content)

if __name__ == '__main__':
    get_words()