#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_21_单例模式二
# @time: 2018/4/4 18:14


class Be(object):
    di = {}

    def __new__(cls, *args, **kwargs):
        ob = super().__new__(cls, *args, **kwargs)
        ob.__dict__ = cls.di
        return ob


a = Be()
b = Be()
print(id(a))
print(id(b))
# a b拥有相同的属性和行为，且属性和行为存在一个地址，所以是单例





