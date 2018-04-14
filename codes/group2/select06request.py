#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: select06request.py
# @time: 2018/4/14 17:22
import socket, select
so = socket.socket()
host = socket.gethostname()
port = 88
so.connect((host, port))  # 连接所用的客户端口是自动产生的，本地同一ip地址可以产生多个连接请求，占用多个客户端口
while True:
    readlist, writelist, errlist = select.select([so], [], [])  # 监听服务器端消息
    data = so.recv(4096).decode("utf-8")
    print(data)
    so.send("hello, again".encode("utf-8"))