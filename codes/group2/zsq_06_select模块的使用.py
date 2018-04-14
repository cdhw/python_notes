#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_06_select模块的使用
# @time: 2018/4/14 16:35
"""select模块的select方法有什么用？"""
import select, socket
st = socket.socket()
host = socket.gethostname()
port = 88
st_list = []
st.bind((host, port))
st.listen(200)
st_list.append(st)

while True:  # select监听客户端请求、客户端消息
    readlist, writelist, errlist = select.select(st_list, [], [])  # select方法直接调用系统的IO接口,接收、监控3个通信列表
# 10秒是超时设置时间，10秒后readllist中的监控对象被移除
# 若不设置超时的话，select程序会一直运行，当前线程的后面被select方法所阻塞，直到st这个socket接收到连接请求后
# select监控到socket的这个变化于是给，当前线程就会解除阻塞往后执行，我在这里创建一个请求的客户端select06request.py
#     print(readlist)  # readlist存放的是发生了变化的socket，服务器端socket是有连接请求，已连接socket，是有消息到来
    for r in readlist:
        if r is st:
            conn, address = st.accept()  # 响应连接请求 st.recv()接收建立连接后的信息
            conn.send('hello'.encode("utf-8"))
            st_list.append(conn)
        else:
            data = r.recv(4096).decode("utf-8")
            print(data)

    # print(conn)
    # print(st)
    # print(address)  # 客户端的地址和端口
# print(readlist)
#     print("hello")
# 同一个端口只能创建一个socket，不能在同一个端口重复创建socket
# 当前线程如果结束了，则监听端口的socket也被释放了,所以要想server端的socket一直处于监听状态必须得循环select
# 方法一直监控socket的状态，保证整个线程不提前结束,每循环一次处理一个连接请求
