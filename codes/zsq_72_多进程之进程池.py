#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_72_多进程之进程池
# @time: 2018/3/25 11:02
import os, time, random
from multiprocessing import Pool


def many_process(name):
    print("now, the child process is %s(%s)" % (name, os.getpid()))
    start = time.time()
    hung = time.sleep(random.random()*3)
    end = time.time()
    print("process %s(%s) runs %s seconds" % (name, os.getpid(), start-end))


if __name__ == "__main__":
    print("Parent process is %s" % os.getpid())
    p = Pool(3)
    for i in range(6):
        p.apply_async(many_process, args=(i,))
        # apply和apply_async的区别就是apply是一个进程执行完了才能执行后面的进程
        # 而apply_async是可以同时让cpu执行3个子进程
    p.close()
    p.join()  # 等待子进程结束之后继续执行下面的程序