#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_20_特殊函数__len__(self)
# @time: 2018/3/11 20:15
#  如果一个类表现得像一个list， 要获取有多少个元素，就得使用len()函数
# 要让len()函数正常调用，就必须给类提供一个特殊方法__len__()，它用于返回元素的个数
# 例如，我们创建了一个Students类，需要把名单传进去


class Student(object):
    def __init__(self, *args):
        self.names = args

    def __len__(self):
        return len(self.names)


# 只要正确实现了__len__()方法， 就可以用len()函数返回Students对象的长度
s = Student("Bob", "jack", "Tom")
print(len(s))


class Beauty(object):
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)


b = Beauty(["Mary", "Jane", "Linda", "Andy"])
print(len(b))


# 题型：一个数列，规律是0,1,1,2,3,5,8，需要编写一个Fib类，Fib(10)表示数列的前10个元素，print Fib(10)可以打印出数列的前10个元素
#
class Fib(object):
    def __init__(self, num):
        a, b, L = 0, 1, []
        for i in range(num):
            L.append(a)
            a, b = b, a+b

        self.nums = num

    def __len__(self):
        return len(self.nums)


