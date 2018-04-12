#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_99_python异步io模块asyncio
# @time: 2018/4/6 11:04
# 引入异步IO模块
import asyncio


@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(5)  # 当前协程被挂起，会继续执行线程的下一个协程
    print("Hello again!")


@asyncio.coroutine
def ru():
    print("stat run")
    # yield from asyncio.sleep(3)
    print("stop run")


@asyncio.coroutine
def go():
    print("go,  go,go")
    yield from asyncio.sleep(6)


@asyncio.coroutine
def catch():
    print("I catch you")
    yield from asyncio.sleep(1)
    print("catched")


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(asyncio.wait([hello(), ru(), go(), catch()]))
loop.close()
# 以上代码实现了并发或者异步的功能，并发：一个程序挂起了，另外一个程序继续秩序。
# asyncio.wait()中的所有协程都在一个线程中，协程就是一个单线程。
# 实现了将函数hello,run,go,catch串在了同一个线程中，每个函数被标记成了协程，所以每个协程被挂起时，后面的，
# 协程会继续执行

