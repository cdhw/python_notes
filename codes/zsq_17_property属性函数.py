#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_17_property属性函数
# @time: 2018/3/11 10:34


class Beauty:
    def __init__(self, name):
        self.name = name

    @property
    def get_name(self):  # 被@property装饰的方法只能return一个数据，也就是只能获取一个属性值，而不能赋值
        return self.name

    # 要想赋值，如下做法
    @get_name.setter
    def get_name(self, name):
        self.name = name


be = Beauty("zhu")
# be.get_name = 1.74  # 因为添加@property之后就表明 get_name属性的值只能来源于一个函数（一段程序）所以不能直接给其赋值
#  添加get_name.setter装饰器之后就可以对get_name属性赋值了
be.get_name = "Mary"
print(be.get_name)  # 限定属性get_name的值来源于一个函数 get_name()

