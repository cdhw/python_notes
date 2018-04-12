#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_97_单例的3种方式
# @time: 2018/4/4 21:22
print("————————————————————————————————————————————————————————第一种：")
# 通过动态添加类属性来记录是否实例化过(重写__new__)


class Duck(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance


d1 = Duck()
d2 = Duck()
print(d1, d2)


print("————————————————————————————————————————————————————————第二种：")
# 通过将所有实例的属性存放到类对象的一个字典属性当中实现单例的效果


class Cat(object):
    di = {}

    def __new__(cls, *args, **kwargs):
        ob = super().__new__(cls, *args, **kwargs)
        ob.__dict__ = cls.di
        return ob


c1 = Cat()
c2 = Cat()
print(c1, c2)  # 虽然生成了两个实例，但是他们的属性和行为是相同的，本质上就是一个实例
c1.name = "jack"
c2.user = "tom"
print(c1.user, c2.name)


print("————————————————————————————————————————————————————————第三种：")
# 利用装饰器原理，本质同第一种


def run(cls):
    def go(*args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = cls(*args, **kwargs)
        return cls.instance
    return go


@run
class P(object):
    pass


p1 = P()
p2 = P()
print(p1, p2)

