#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_27_什么是协程？
# @time: 2018/4/5 10:03
"""协程：协程是一个特殊的子进程，子进程就是一个线程，在子进程内部，函数层级的执行是由底层往
高层执行，并且严格按照顺序执行。但是在协程中，各层级是平行的，交替执行"""
'''书中例子：
1、生产者--消费者模型是采用两个线程来操作一个队列，当一个线程在执行取消息
的程序时，对队列程序上锁直到取消息完毕之后解锁让写消息线程操作队列，但是这很容易
发生死锁的情况
2、如果采用协程的方式，生产者生产消息之后，直接通过yield跳转到消费开始执行，待消费者执行完毕
后，切换回生产者继续生产，效率极高'''


def consumer():
    r = ''
    while True:
        n = yield r

        # 当生成器被传入值时，consumer中程序被执行，执行到yield时，程序暂停
        # 直到下一次传入值，之前的程序被激活，当前程序走到yield时，又暂停，等待下一次
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = 'ok'
        print(2)


def produce(k):
    k.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print("[PRODUCER] Producing %s..." % n)
        r = k.send(n)  # 发送后程序暂停，生成器程序暂停后（到yield），下面的程序继续执行
        print(1)
        print("[PRODUCER] Consumer return: %s" % r)
    k.close()


c = consumer()
produce(c)
# 以上线程连接两个层级，两个层级交替执行并相互传递信息实现了协程的效果