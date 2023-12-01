from .systemfuc import *
import plugins  # 导入自定义的插件模块
from bridge.reply import Reply, ReplyType  # 导入用于构建回复消息的类
from plugins import *  # 导入其他自定义插件

@plugins.register(
    # name="WindowsHostInfo",  # 插件的EN名称
    name="Windows主机巡检",  # 插件的CN名称
    desire_priority=0,  # 插件的优先级
    hidden=True,  # 插件是否隐藏
    desc="Windows主机巡检插件",  # 插件的描述
    version="1.0",  # 插件的版本号
    author="XcNGG",  # 插件的作者
)
class WindowsHostInfo(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        logger.info("[WindowsHostInfo-XcNGG] inited")  # 初始化插件时打印一条消息

    def on_handle_context(self, e_context: EventContext):
        content = e_context["context"].content  # 获取事件上下文中的消息内容
        if content == "主机巡检":  # 如果消息内容为 "主机巡检"
            reply = Reply()  # 创建回复消息对象
            reply.type = ReplyType.TEXT  # 设置回复消息的类型为文本
            system_data = GetFullSystemData()
            result = f"""【主机时间】:{system_data['boot']['datetime']}
【主机系统】:{GetSystemVersion()}
【CPU信息】:{system_data['cpu']['cpu_name']} 
【CPU占用】:{str(system_data['cpu']['used'] * 10) + '%'}  
【内存占用】:{str(round(system_data['mem']['menUsedPercent'], 1)) + '%'}
【持续运行】:{round(system_data['boot']['runtime'] / 3600, 2)} 小时
【磁盘占用】:
"""
            disk_info = system_data['disk']
            for disk in disk_info:
                info = f" [{disk['path']}]占用:{str(round(disk['size']['percent'], 2))}%\n"
                result += info
            logger.info(result)
            reply.content = result  # 设置回复消息的内容

            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS


    def get_help_text(self, **kwargs):
        help_text = "关键词【主机巡检】By XcNgg"
        return help_text
