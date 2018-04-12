#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_22_单例模式三
# @time: 2018/4/4 18:59
# 判断当前类对象是否拥有某个属性，以此推理是否实例化过，如果实例化过，直接返回之前的实例，
# 之前的实例放在类属性里


"""def singleton(cls):
    def getinstance(*args,**kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = cls(*args, **kwargs)
        return cls.instance
    return getinstance


@singleton
class MyClass:
    a = 1


c1 = MyClass()
c2 = MyClass()
print(c1 == c2) # True"""


def run(cls):
    def hit(*args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = cls(*args, **kwargs)
        return cls.instance
    return hit


@run
class M(object):
    pass

a = M()
b = M()
print(a)
print(b)
# 分析：run函数作为装饰器，把M类对象当做函数装饰，所以M()实例化调用__new__方法时会执行run的函数体程序，然后返回实例
# 装饰器装饰的不仅仅是函数，而是装饰的能够触发程序运行的一切对象，会向程序切入另外一段程序