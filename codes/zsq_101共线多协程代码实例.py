#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_100共线多协程代码实例
# @time: 2018/4/7 9:02
import asyncio, threading

'''
@asyncio.coroutine
def a():
    print("进入a程序")
    print("a")
    print("离开a程序")



def b():
    print("进入b程序")
    time.sleep(10)
    x = None
    yield x
    print("离开b程序")


@asyncio.coroutine
def c():
    print("进入c程序")
    r = ''
    yield from asyncio.sleep(10)
    print("离开c程序")


asy = asyncio.get_event_loop()  # 返回_WindowsSelectorEventLoop类，提供事件循环功能
# print(type(asy))
# print(asy.__bases__)
c()  # 直接调用生成器函数，程序不会运行。
asy.run_until_complete(asyncio.wait([c(), a()]))  # 把生成器放入事件循环程序中，生成器程序会执行完毕'''
# c协程在执行到asyncio.sleep时因为需要等待，所以线程继续执行下一个协程a()

'''
@asyncio.coroutine
def hello():
    print("hello world, 我是线程 %s" % threading.current_thread())
    yield from asyncio.sleep(5)
    print("hello again, 我是线程 %s" % threading.current_thread())


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(asyncio.wait([hello(), hello()]))
'''


# @asyncio.coroutine
# def wget(site):
#     # print("visit %s" % site)
#     n = yield from site
#     print(n)
#
#
# w = wget([1, 2, 3])
# w.send(None)
# w.send(4)


'''@asyncio.coroutine
def get():
    o = None
    yield o
    print("hello")


loop = asyncio.get_event_loop()
loop.run_until_complete(get())'''
# 在协程中不管你是否是生成器（是否有yield）生成器的程序都会执行完毕，而不会在yield处暂停


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)  # <generator object open_connection at 0x0000000002F284C0>
    # print(connect)
    reader, writer = yield from connect
    # print("--------------------------")
    print(type(reader))  # <StreamReader t=<_SelectorSocketTransport fd=648 read=polling write=<idle, bufsize=0>>>
    # print(writer)  # <StreamWriter>>>
    # print("-------------------------")
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    print("=======================")
    yield from writer.drain()  # <generator object StreamWriter.drain at 0x0000000002F38518> 生成器实例
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


def hello():
    pass


# print(hello)  # <function hello at 0x0000000000A3BAE8>




