#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_78_线程回顾
# @time: 2018/3/26 15:09
import threading, time, random


'''def submit_name():
    print("线程%s开始了" % threading.current_thread().name)
    for i in range(18):
        print("线程%s走到第%s步了" % (threading.current_thread().name, i))
        time.sleep(2)


def submit_password():

    print("线程%s开始了" % threading.current_thread().name)
    for i in range(18):

        print("线程%s走到第%s步了" % (threading.current_thread().name, i))
        time.sleep(8)


t1 = threading.Thread(target=submit_name,  name="num1")  # 创建线程对对象
t2 = threading.Thread(target=submit_password, name="num2")
t2.start()
t1.start()  # 执行线程
t2.join()  # join方法保证线程对象执行完成再执行下面的线程
t1.join()'''
'''
有一种情况，当多个线程同时作用于同一个变量时，这个变量的值会混乱不堪
'''
num = 0
lock = threading.Lock()


def count(n):
    global num
    # cpu工作到这里时，就会等待前面的线程执行完并解锁之后继续执行
    num += n
    num -= n


def count1(n):

    for i in range(1,99):
        lock.acquire()
        try:
            count(n)  # 对count(n)这段程序上锁，该段程序只能被一本线程所占用
        finally:
            lock.release()  # 无论count调用是否异常都要解锁
        print("我是线程%s我已经循环到%s" % (threading.current_thread().name, i))


def count2(n):
    for i in range(1,99):
        count(n)
        print("我是线程%s我已经循环到%s" % (threading.current_thread().name, i))


t1 = threading.Thread(target=count1, name="t1", args=(8,))
t2 = threading.Thread(target=count1, name="t2", args=(5,))
t2.start()
t1.start()
t1.join()
print(num)  # 这个值是不固定的，因为count函数同时被count1和count2两个线程所操纵
# 再有线程在执行中可能出现中断情况，导致num的输出结果混乱
# 避免这种情况发生的一个方式就是要讲count这个公用线程上锁
# 当这个线程在执行中时不允许再次执行，也就是不允许其他线程的调用，直到当前进程执行
# 完毕
"""
线程Lock类封装的功能就是实现对线程中的某段程序上锁，当当前线程在执行这段
上了锁的程序时，后面需要执行这段程序的线程只能处于等待状态，知道前面的线程
将这段程序执行完并解锁
"""



