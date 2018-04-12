#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_98_生成器代码测试
# @time: 2018/4/5 16:10
# 定义一个生成器函数，调用生成器函数返回的是一个生成器对象
import os

'''di = []


def generate():
    r = ''
    # 生成器
    while True:
        n = yield r  # yield 放在这里是为了控制循环
        if not n:
            return
        di.append(n)
        print(di)
        r = "ok"


def produce(g):
    g.send(None)
    n = 0
    while n < 5:
        n += 1
        r = g.send(n)
        print(n)
    g.close()


g = generate()  # 获得生成器对象
produce(g)'''


def p():
    r = ''
    n = 0
    print("zero")
    while n < 5:
        print("start")
        yield r

        n += 1
        print("go")


p = p()  # 获得生成器实例
p.send(None)  # 必须先启动生成器,启动生成器则意味着生成器程序被执行
# 但是程序会停留在yield那一步，直到下一次send值给yield，生成器程序继续执行
p.send(3)  # 给生成器yield传值
p.send(4)


print("==============================")


def hi():
    r = ''
    yield r
    print("hello")


h = hi()
h.send(None)  # 启动程序，
h.send(3)  # 生成器程序已经执行完毕，所以后续无法send
h.send(4)


