#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: test2
# @time: 2018/3/17 17:28
import test1 as zhang
f = zhang.Fruit()
print("判断是否导入Fruit类")
print(f.taste())
print("判断是否导入Animal类")
try:
    a = zhang.Animal()
except NameError as e:
    print("导入Animal类的结果:")
    print(e)
try:
    print(zhang.apple)
except NameError as e:
    print("导入apple属性的结果：")
    print(e)
finally:
    print("导入apple属性成功")
try:
    print(zhang.orange)
except NameError as e:
    print("导入orange属性的结果:")
    print(e)
print(type(zhang))
print(zhang.os)
