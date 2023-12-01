# import requests
#
# # http://dict.youdao.com/dictvoice?type=音频类型&audio=单词
# # 请求方法：get
# # type=0 : 美音
# # type=1 : 英音
# # audio : 单词
#
# def get_voice(word):
#     url = "http://dict.youdao.com/dictvoice?type=1&audio=" + word
#     response = requests.get(url)
#     path = r"./voice/"
#     with open(path+word + '.mp3', 'wb') as mp3:
#         mp3.write(response.content)
#


import json
import os

# 创建一个空字典来存储所有的单词数据
all_words = []


for i in range(ord('A'), ord('Z')+1):
# 读取A到Z的json文件并合并到all_words中
    with open(f'src/JSON/{chr(i)}.json','r',encoding='utf-8') as file:
        data = json.load(file)
        all_words += data

print(all_words)
# 保存为total.json
with open('src/total.json', 'w') as file:
    json.dump(all_words, file, ensure_ascii=False, indent=4)



# 打印合并后的单词总数
print(f"Total words: {len(all_words)}")
