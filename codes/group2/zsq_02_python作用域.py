#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_02_python作用域
# @time: 2018/4/14 10:51
"""模块中，没有任何标记的函数或者变量是出于公开状态的
函数或者变量被'_'或者'__'标记了的是非公开的
下面创建一个测试模块zyy.py，里面放一些变量和函数"""
# open("zyy.py", "w+")
# from group2.zyy import one, _two, a, _a
import group2.zyy
group2.zyy._two()
print(_a)
print(a)
group2.zyy.one()
