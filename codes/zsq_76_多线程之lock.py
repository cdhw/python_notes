#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_76_多线程之lock
# @time: 2018/3/26 2:49
import time, threading
"""
多进程和多线程最大的区别就是变量的差异上
对于多进程，不同的进程拥有相对独立的变量
对于多线程，不同的线程共享同一变量
"""
# 假设这是你的银行存款
balance = 0


def change_it(n):
    # 先存后取， 结果应该为0
    global balance
    # print("线程%s在存钱了" % threading.current_thread().name)
    balance = balance + n
    # print("线程%s在取钱了" % threading.current_thread().name)
    balance = balance - n


def run_thread(n):
    for i in range(1000000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,), name="t1")
t2 = threading.Thread(target=run_thread, args=(8,), name="t2")
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)