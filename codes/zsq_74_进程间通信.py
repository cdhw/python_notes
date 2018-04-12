#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_74_进程间通信
# @time: 2018/3/26 1:30
from multiprocessing import Process, Queue
import os, time, random
"""
Process进程之间是必须要通信的，操作系统提供了很多机制来实现进程间的通信，Python的multiprocessing模块封装了这些机制的底层
代码，提供了Queue(队列）、Pipes（管道）等多种方式来交换数据


"""
"""
下面我将从父进程中创建两个子进程，一个子进程往Queue里写数据，一个子进程从Queue里取数据
"""


# def write(q):  # 定义往Queue里写入数据的进程
#     print("Process to write:%s" % os.getpid())
#     for value in ["A", "B", "C"]:
#         print("Put %s to queue..." % value)
#         q.put(value)
#         time.sleep(random.random())
#
#
# def read(q):  # 定义从Queue里读取数据的进程
#     print("Process to read: %s" % os.getpid())
#     while True:
#         value = q.get(True)
#         print("Get %s from queue." % value)
#
#
# if __name__ == "__main__":  # 判断如果执行的是当前模块程序
#     q = Queue()  # 实例化队列类
#     pw = Process(target=write, args=(q,))  # 创建写入进程，参数是队列实例
#     pr = Process(target=read, args=(q,))  # 创建读取进程，参数是队列实例
#     pw.start()  # 开始运行写入进程
#     pr.start()  # 开始运行读取进程
#     pw.join()  # 写入进程执行完成之后，继续执行后面的程序
#     pr.terminate()  # 读取进程执行完毕之后，终止读取进程
def write(p):
    print("the Process %s which will write to Queue" % os.getpid())
    for value in ["A", "B", "C"]:
        print("the Process %s has wrote %s to Queue" % (os.getpid(), value))
        p.put(value)
        time.sleep(random.random())


def read(p):
    print("the Process %s which will read from Queue" % os.getpid())
    while True:
        pt = p.get(True)
        print("the Process %s has read %s from Queue" % (os.getpid(), pt))


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
#  pw pr 两个进程是同时进行的，通过打印的输出就可以看出

