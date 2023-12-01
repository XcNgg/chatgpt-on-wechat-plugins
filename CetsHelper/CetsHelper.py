# encoding:utf-8
import json
import os
import requests
import plugins
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from common.log import logger
from plugins import *
from datetime import datetime
import random

@plugins.register(
    name="CETs助手",
    desire_priority=900,
    hidden=True,
    desc="CETs助手",
    version="0.1",
    author="XcNGG",
)
class CetsHelper(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        logger.info("[CETs助手] inited.")


    def on_handle_context(self, e_context: EventContext):
        if e_context["context"].type != ContextType.TEXT:
            return
        content = e_context["context"].content.strip()

        if content == "今日单词":
            reply = Reply()
            reply.type = ReplyType.TEXT
            reply.content = self.get_words()
            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS  # 事件结束，并跳过
        elif content.startswith("发音 "):
            words = content.split('发音 ')[-1]
            reply = Reply()
            reply.type = ReplyType.FILE
            reply.content = self.get_voice(words=words)

            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS  # 事件结束，并跳过处理context的默认逻辑

    def get_words(self):
        now_path = os.getcwd().replace("\\", "/") + "/"
        print(f"当前路径:{now_path}")
        # "E:\CodeProject\PythonProject\chatgpt-on-wechat\cet-4\"
        # 生成新的json文件名
        date = datetime.now().strftime('%Y-%m-%d')
        new_file_name = now_path + f"plugins/CetsHelper/data/{date}.json"
        print(f"new_file_name:{new_file_name}")

        src_path = now_path + "plugins/CetsHelper/data/total.json"
        print(f"src_path:{src_path}")


        if not os.path.exists(new_file_name):
            # 读取total.json文件
            with open(src_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            if len(data) >= 20:
                random_words = random.sample(data, 20)
            else:
                random_words = random.sample(data, len(data))

            with open(new_file_name, 'w', encoding='utf-8') as f:
                json.dump(random_words, f,indent=4)


            data = [word for word in data if word not in random_words]

            with open(src_path, 'w', encoding='utf-8') as f:
                json.dump(data, f,indent=4)


        with open(new_file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)

        content = f"{date}🕖【今日单词】🔠\n"
        for index, d in enumerate(data, 1):
            content += f"{index}. {d['word']}\n"
            content += f"解释：{d['mean']}|音标：{d['phonetic_symbol']}\n"
        content += "✅今天也是元气满满的一天！✨"
        return content

    def get_voice(self,words):
        url = "http://dict.youdao.com/dictvoice?type=1&audio=" + words
        response = requests.get(url)
        now_path = os.getcwd().replace("\\", "/") + "/"
        path = r"plugins/CetsHelper/voice/"
        mp3_path = now_path+path+words+".mp3"
        with open(mp3_path, 'wb') as mp3:
            mp3.write(response.content)
        return mp3_path



    def get_help_text(self, **kwargs):
        help_text = "关键词【今日单词】获取今日单词清单\n关键词【发音 单词】获取单词发音\nBy XcNGG"
        return help_text
