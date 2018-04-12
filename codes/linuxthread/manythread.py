#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: 多进程
# @time: 2018/3/24 20:10
import os
from multiprocessing import Process

# print('Process (%s) start...' % os.getpid())
#
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
# 先定义一段子进程程序


def child_process(name):
    print("Run child process %s(%s)" % (os.getpid(), name))
# 调用multiprocessing看是否能实现上面子进程程序的执行


if __name__ == "__main__":  # 如果执行的是当前模块程序
    print("Parent process is %s" % os.getpid())
    c = Process(target=child_process, args=("child",))
    print("child process start now")
    c.start()
    c.join()  # join功能的作用是等待子进程执行完成后继续执行父进程后面的程序
print("back to parent process")








