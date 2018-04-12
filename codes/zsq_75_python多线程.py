#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_75_python多线程
# @time: 2018/3/26 2:24
import time, threading
"""
python中封装了线程的功能和属性的是_thread模块和threading模块
后者是高级模块对前者进行了封装，一般我们只需要引入threading模块
启动一个线程就是创建一个threading的实例，并将线程函数传参进去，然后
调用threading的start方法即可开始执行线程代码
进程我们说进程id
线程我们说线程名字

"""
# 定义线程要执行的代码块

'''
def loop():  # 这是子线程
    print("thread %s is running" % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print("thread %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s ended." % threading.current_thread().name)


print("thread %s is running..." % threading.current_thread().name)
t = threading.Thread(target=loop, name="LoopThread")
t.start()
t.join()
print("thread %s has ended." % threading.current_thread().name)  # 这是主线程
'''


def hit():
    print("helloworld")
    print("子线程%s结束了" % threading.current_thread().name)


t = threading.Thread(target=hit, name="new")
t.start()
t.join()
print("主线程是%s" % threading.current_thread().name)


