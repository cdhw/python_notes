#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_79_ThreadLocal类对象
# @time: 2018/3/27 10:03
import threading


class Student:
    def __init__(self, name):
        self.name = name


'''def run(name):
    std = Student(name)
    play(std)
    hit(std)


def play(std):
    print(std.name)


def hit(std):
    print(std.name)


t1 = threading.Thread(target=run, name="t1", args=("tom",))
t1.start()'''
"""
以上线程调用的程序是调用了两个函数play和hit，并且参数需要先从run传递到play
和hit，传参显得复杂，我们可以定义一个全局字典,让hit和play两个函数不用传参
便能够直接获取到std.name的值
"""
'''dic = {}


def run(name):
    std = Student(name)
    dic[threading.current_thread().name] = std.name
    hit()
    play()


def hit():
    print("我是hit")
    print(dic[threading.current_thread().name])


def play():
    print("我是play")
    print(dic[threading.current_thread().name])


t1 = threading.Thread(target=run, name="t1", args=("tom",))
t1.start()
# 以上方式可行，但是代码量还是比较多
# 引入threading的ThreadingLocal类，实现以上的功能'''

td = threading.local()  # td在这里好比一个可以用点号将元素转换为绑定属性的字典


def run(name):
    std = Student(name)
    td.student = std.name  # 封装当前线程的一个数据，获取的时候不同的线程获取各自的
    # student的值，在取值的时候加了当前线程名的判断，这些都封装好了ThreadLocal
    # 都封装好了，td就是一个ThreadLocal对象
    hit()
    play()


def hit():
    print("我是hit")
    print(td.student)


def play():
    print("我是play")
    print(td.student)


t = threading.Thread(target=run, args=("tom",), name="t")
t.start()
t1 = threading.Thread(target=run, args=("jack",), name="t1")
t1.start()
# 利用ThreadLocal对象可以为不同的线程绑定一个数据连接
# 一个ThreadLocal变量虽然是全局变量，
# 但每个线程都只能读写自己线程的独立副本,互不干扰。
# ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
