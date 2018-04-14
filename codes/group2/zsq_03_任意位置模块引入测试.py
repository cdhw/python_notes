#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_03_任意位置模块引入测试
# @time: 2018/4/14 11:26
"""通过sys模块的path属性我们可以把我们自定义的模块添加进去，这样在任意一个
模块中都可以用import语句引入我们定义的模块，现在我们测试a.py这个模块的引入
在当前位置，我们要成功引入a.py模块(编辑器不报错的话）的话需要使用语句'import group2.a' 但是如果
说我们想要直接使用语句'import a' 怎样实现呢？"""
import sys
# sys.path.append("/group2/a.py")  # 运行时修改运行结束失效
# import test
# __import__("a")
sys.path.append("../test1.py")
import test1

