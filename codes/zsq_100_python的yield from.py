#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_100_python的yield from
# @time: 2018/4/6 11:30
import time


def a():
    r = ''
    print("a")
    yield r
    print("a-end")
    time.sleep(20)


def b():
    print("b")
    yield from a()
    print("b-end")


b1 = b()
b1.send(None)
try:
    b1.send(9)  # 如果生成器的程序结束了就会报StopIteration
except StopIteration:
    print("stop")
# yield 生成器就是靠暂停一个运行中的程序来迭代数据的，迭代出的数据也是供这个运行中的程序所用的
# 如果一个程序已经停止了，那么迭代也会停止
