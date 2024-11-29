# Telegram 散小战QQ查绑机器人项目

[![GitHub license](https://img.shields.io/badge/license-MPL%202.0-blue.svg)](https://github.com/yourusername/yourrepository/blob/main/LICENSE)

## 简介

这是一个基于Python的Telegram机器人项目，提供QQ号查询和服务器状态检查等功能。本项目遵循Mozilla公共许可证2.0（MPL 2.0），确保代码的透明度和可扩展性。

## 功能

- **QQ号查询**：用户可以通过命令`/qq`查询指定QQ号的相关信息。
- **服务器状态检查**：通过命令`/status`，用户可以获取服务器的CPU使用率、内存使用情况、磁盘使用情况和网络I/O统计信息。
- **启动问候**：当用户启动机器人时，通过命令`/start`，机器人会回复一条问候信息。

## 环境要求

- Python 3.x
- telebot
- requests
- json
- psutil
- datetime
- distro

## 安装指南

1. **克隆项目**  

   一定要先修改散小战查绑机器人.py里的你的Token改成你自己的
安装所有依赖 pip3 install -r requirements.txt
然后我们启动机器人python3 散小战查绑机器人.py
