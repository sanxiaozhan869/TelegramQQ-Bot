# Copyright (c) 散小战开发
# 版权所有，请勿二改
# 保留所有权利。

import telebot  # 导入telebot库，这是一个Python库，用于创建和控制Telegram机器人。
import os       # 导入os库，这个库提供了许多与操作系统交互的功能。
import requests # 导入requests库，这是一个非常流行的HTTP客户端库，用于发送网络请求。
import json     # 导入json库，用于解析JSON格式的数据。
import psutil   # 导入psutil库，用于获取系统运行时的信息，如CPU和内存使用率。
from datetime import datetime  # 从datetime模块导入datetime类，用于处理日期和时间。
import distro   # 导入distro库，用于获取Linux操作系统的发行版信息。

# Copyright (c) 散小战开发
# 版权所有，请勿二改
# 保留所有权利。

# 定义一个字符串变量TOKEN，存储你的Telegram机器人的API token。
# 这个token是创建机器人后由BotFather提供的，用于验证和授权你的机器人。
TOKEN = "你的Token"
# 使用TOKEN创建一个TeleBot对象，这个对象将用于控制你的机器人。
bot = telebot.TeleBot(TOKEN)

# Copyright (c) 散小战开发
# 版权所有，请勿二改
# 保留所有权利。

# 使用装饰器定义一个消息处理函数，当用户发送/qq命令时触发。
@bot.message_handler(commands=['qq'])
def check_license_plate(message):
    # 使用split方法将消息文本按空格分割成列表，以便提取QQ号。
    parts = message.text.split(' ')
    # 检查分割后的列表长度是否小于2，即用户是否输入了QQ号。
    if len(parts) < 2:
        # 如果没有输入QQ号，回复用户提示输入正确QQ号。
        bot.reply_to(message, "请输入正确QQ号")
        return
    # 提取用户输入的QQ号，它是列表的第二个元素。
    plate = parts[1]
    # 构造一个URL，用于向API发送请求，查询QQ号对应的信息。
    url = f"https://api.xywlapi.cc/qqapi?qq={plate}"
    # 使用requests库发送GET请求到构造的URL。
    response = requests.get(url)
    try:
        # 尝试将API返回的JSON格式的响应文本解析成Python字典。
        data = json.loads(response.text)
        # 从解析后的字典中获取'qq'和'phone'键对应的值。
        qq_value = data.get('qq', '  ')
        phone_value = data.get('phone', '  ')
        # 获取当前时间，并格式化为"年-月-日 时:分:秒"的格式。
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 构造一个包含查询信息和当前时间的回复文本。
        reply_text = f"查询信息:\n当前时间: {current_time}\nQQ号对应的值: {qq_value}\n电话号码对应的值: {phone_value}\n----------------------------------------------\n人工查询\n人工双向 @Xiaozhanzai_Bot\n人工 @Sanxiaozhan886\n----------------------------------------------\n没有显示就是没有查到\n----------------------------------------------\n散小战查绑Bot @SAN869CN"
        # 使用reply_to方法回复用户查询结果。
        bot.reply_to(message, reply_text)
    except json.JSONDecodeError:
        # 如果解析JSON失败，回复用户提示接口返回数据格式有误。
        bot.reply_to(message, "接口返回数据格式有误，无法解析")

# Copyright (c) 散小战开发
# 版权所有，请勿二改
# 保留所有权利。

# 定义一个消息处理函数，当用户发送/start命令时触发。
@bot.message_handler(commands=['start'])
def send_hello(message):
    # 回复用户一条问候信息，并提供客服信息。
    bot.reply_to(message, "你好！这是一条来自散小战制作的查绑机器人。需要同款请找客服散小战 @Xiaozhanzai_Bot 使用教程/qq xxxx")

# Copyright (c) 散小战开发
# 版权所有，请勿二改
# 保留所有权利。

# 定义一个消息处理函数，当用户发送/status命令时触发。
@bot.message_handler(commands=['status'])
def get_server_status(message):
    # 获取当前CPU使用率，interval=1表示计算1秒内的使用率。
    cpu_usage = psutil.cpu_percent(interval=1)
    # 获取当前内存使用情况。
    memory = psutil.virtual_memory()
    # 获取当前磁盘使用情况。
    disk = psutil.disk_usage('/')
    # 获取网络I/O统计信息。
    network_io = psutil.net_io_counters()

    # 根据操作系统类型获取操作系统信息。
    if os.name == 'nt':
        # 如果操作系统是Windows，设置os_info为"Windows"。
        os_info = f"Windows"
    elif os.name == 'posix':
        try:
            # 如果操作系统是Linux，尝试获取Linux发行版信息。
            distro_info = distro.info()
            # 设置os_info为Linux发行版名称和版本号。
            os_info = f"{distro_info['name']} {distro_info['version']}"
        except Exception as e:
            # 如果获取Linux发行版信息失败，设置os_info为"Linux"。
            os_info = "Linux"
    else:
        # 如果操作系统类型既不是Windows也不是Linux，设置os_info为"Unknown OS"。
        os_info = "Unknown OS"

    # 获取当前时间，并格式化为"年-月-日 时:分:秒"的格式。
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 将网络上传和下载的字节数转换为兆比特每秒（Mbps）。
    bytes_sent_mbps = (network_io.bytes_sent / (1024 * 1024)) / 8
    bytes_recv_mbps = (network_io.bytes_recv / (1024 * 1024)) / 8

    # 构造一个包含服务器状态信息的文本。
    status_message = (
        f"操作系统: {os_info}\n"
        f"当前时间: {current_time}\n"
        f"CPU 使用率: {cpu_usage}%\n"
        f"内存使用: {memory.percent}%\n"
        f"磁盘使用: {disk.percent}%\n"
        f"上传流量: {bytes_sent_mbps:.2f} Mbps\n"
        f"下载流量: {bytes_recv_mbps:.2f} Mbps"
    )
    # 使用reply_to方法回复用户服务器状态信息。
    bot.reply_to(message, status_message)

# Copyright (c) 散小战开发
# 版权所有，请勿二改
# 保留所有权利。

# 启动机器人的轮询模式，这样机器人就可以定期检查Telegram服务器是否有新的消息或事件。
bot.polling()
