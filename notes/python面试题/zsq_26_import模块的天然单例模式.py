#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_26_import模块的天然单例模式
# @time: 2018/4/5 9:50
"""模块也是一个对象，我们引入模块其实就是引入模块的实例，且所有地方都是引用的同一个
模块实例"""
from zsq_25_单例实现的3种方式 import B
# import zsq_25_单例实现的3种方式
m1 = B()
m2 = B()
print(m1, m2)
