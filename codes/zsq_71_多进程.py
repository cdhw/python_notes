#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_71_多进程
# @time: 2018/3/24 11:12

"""
linux/unix操作系统提供了一个fork()系统程序调用，他的作用是将当前进程复制一份，然后在运行的父进程和子进程中分别
返回数据。子进程永远返回0，父进程返回子进程的id
python 的os对象就封装了调用系统fork程序的功能
windows系统没有提供fork程序调用

"""
import os
from multiprocessing import Process
# print("Process %s start ..." % os.getpid())  # os.getpid指获取当前的进程
# print(os.getppid())  # os.getppid获取当前进程的父id


def create_child(name):
    print("child process %s(%s) is beginning" % (name, os.getpid()))


if __name__ == "__main__":
    print("parent process is %s" % (os.getpid(),))
    c = Process(target=create_child, args=("tom",))  # 开启子进程create_child
    c.start()
    c.join()




