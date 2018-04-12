#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_25_单例实现的3种方式
# @time: 2018/4/5 9:13
print("一一一一一一一一一一一一一一一一一一一一一")


class Money(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance


m1 = Money()
m2 = Money()
print(m1, m2)
print("一一一一一一一一一一一一一一一一一一一一一")


class Monkey(object):
    dic = {}

    def __new__(cls, *args, **kwargs):
        ob = super().__new__(cls)
        ob.__dict__ = cls.dic
        return ob


k1 = Monkey()
k2 = Monkey()
print(k1, k2)
print("一一一一一一一一一一一一一一一一一一一一一")


def decorate(cls, *args, **kwargs):
    def decoration():
        if not hasattr(cls, "instance"):
            cls.instance = cls(*args, **kwargs)
        return cls.instance
    return decoration


@decorate
class Milk(object):
    pass


n1 = Milk()
n2 = Milk()
print(n1, n2)


print("用于import天然单例的测试类")


class B(object):
    pass



