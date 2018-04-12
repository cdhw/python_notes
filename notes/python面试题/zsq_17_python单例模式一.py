#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_17_python单例模式
# @time: 2018/4/4 11:45
# 所谓单例模式，就是让类只能产生一个实例
# 单例的第一种实现：
import os

"""class Animal(object):
    apple = 4

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


a = Animal()
print("查看实例是否将类变量当做了属性")
print(hasattr(a, "apple"))
print(a)
print("实例a的属性和方法有：")
print(a.__dict__)
b = Animal()
print(b)
c = Animal()"""


# 单例的第二种实现：让所有实例共享同一套属性和方法,从逻辑上实现了单例
class Member(object):

    name = "jack"
    sex = "boy"
    dic = {}

    def __new__(cls, *args, **kwargs):
        ob = super().__new__(cls, *args, **kwargs)
        ob.__dict__ = cls.dic
        return ob


print(Member.__dict__)  # 查看Member类对象的所有属性和方法
m = Member()
m.name = "tom"
print(m.__dict__)  # 获取的是m实例区别于Member类的所有属性'''
n = Member()
print("实例比较：")
print(m)
print(n)

'''m = Member()
m.girl = "linda"
print(m.__dict__)
n = Member()
n.boy = "tom"
print(m.boy)
print(n.girl)
print(Member.__dict__)
print(m)
print(n)'''
# 虽然生成了两个实例，但是他们公用同一套属性和方法，都在_dic字典中
# 单例的第三种实现


'''class Singleton2(type):
    def __init__(cls, name, bases, dict):
        super(Singleton2, cls).__init__(name, bases, dict)
        cls._instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton2, cls).__new__(cls,*args, **kw)
        return cls._instance


class MyClass3(object):
    __metaclass__ = Singleton2


one = MyClass3()
two = MyClass3()

two.a = 3
print(one.a)
# 3
print(id(one))
# 31495472
print(id(two))
# 31495472
print(one == two)
# True
print(one is two)'''
# True
os.rename("zsq_17_python单例模式.py", "zsq_17_python单例模式一.py")




def run(cls):
    def hit(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = cls(*args, **kwargs)
        return cls.instance
    return hit


@run
class M(object):
    pass

a = M()
b = M()
print(a == b)



