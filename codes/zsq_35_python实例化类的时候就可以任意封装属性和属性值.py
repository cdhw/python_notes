#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_35_python实例化类的时候就可以任意封装属性和属性值
# @time: 2018/3/14 23:35
# 当我们以 A = B()的方式实例化类时，我们可以在B()中封装任意的属性值


class BeautyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['name'] = "zhang"
        return type.__new__(cls, name, bases, attrs)


class Beauty(dict, metaclass=BeautyMetaclass):

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)


b = Beauty(call="hello", names="zhang", age=13, sex="ma")
print(b)
print(b.call)
print(b.names)
print(dir(b))


# class Test(dict):
#     pass
#     # def __getattr__(self, key):
#     #     print("here")
#     #     try:
#     #         return self[key]
#     #     except KeyError:
#     #         raise AttributeError(r"'Model' object has no attribute '%s'" % key)
#         # print("hello")
#         # return self.item 此处无限循环，会导致栈溢出
#
#
# t = Test(("name", "password"))  # t是一个字典
# print(t.__dict__)




