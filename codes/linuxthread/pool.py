#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: pool
# @time: 2018/3/25 9:47
"""
pool 对象可以实现多个进程，称作进程池
pool对象批量创建进程
"""
import os, time, random
from multiprocessing import Pool


def long_time_task(name):  # name是进程的名字
    print("process %s(%s) is beginning" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*2)  # 程序执行到这里就挂起（暂停）一段时间
    end = time.time()
    print("%s run %s seconds" % (name, end - start))


if __name__ == "__main__":
    print("parent process is %s" % os.getpid())
    p = Pool(2)  # 表示最多同时跑3个进程，默认是电脑的cpu核数，若你没有写限制进程数，那么
    # 你实现的进程数要大于cpu核数，才能看到进程等待状态
    for i in range(4):
        p.apply_async(long_time_task, args=(i,))
    p.close()
    p.join()

