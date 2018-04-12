#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_37_对象的__getattr__方法
# @time: 2018/3/15 15:34
# 实例化对象的__getattr__()方法是在试图获取对象没有的属性时会被触发


class Animal(dict):
    # pass
    def __getattr__(self, key):  # 抓住__getattr__的定义：当对象试图访问未知属性时，会触发此方法
        # 此方法会尝试给对象返回此未知属性的值，也就是此方法的返回值就是给对象绑定的这个未知属性的值

        try:
            # print("here")
            # print("key的值是："+key)
            # print("key的类型是")
            # print(type(key))
            return self[key]  # __getattr__方法返回了元素值
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)


a = Animal(name="cat", user="zhang", password=123)  # name、user、password都不是a的属性
# print(dir(a))
print(a.name)  # a在访问name非属性时会触发__getattr__方法，__getattr__方法再返回元素值就实现了字典元素属性访问方式
di = {"apple": 1, "orange": 2}
print(hasattr(di, "apple"))
