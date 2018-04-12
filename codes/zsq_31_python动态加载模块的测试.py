#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-13 11:10
# @Author  : Henry
# @File    : zsq_31_python动态加载模块的测试.py
# @Software: PyCharm
from zsq_30_python元类 import Hello

h = Hello()
h.hello()
# 当你用python解释器执行当前文件时，python解释器就会载入zsq_30_python元类模块并依次执行Hello类中的所有语句
# 执行结果就是动态创建出一个Hello的class对象
print(type(Hello))  # Hello就是一个类
print("_______________________")
print(type(h))  # 而h是一个实例化的类，所以是class Hello 一个实实在在的Hello类
# class的定义的实现是python解释器执行它时动态创建的，解释器执行class的定义语句并定义出类使用的
# 的是type()函数
# type()函数既可以返回一个对象的类型，又可以创建出新的类型
# 例如我们可以通过type()函数创建出Hello类，而不需要通过 class Hello(object)来定义Hello类
print("_______________________")


def fn(self, name= "world"):
    print("Hello, %s." % name)


Hell = type("Hell", (object,), dict(hello=fn))  # 创建Hello class
h = Hell()
print("XXXXXXXXXXXXXXXXX")
h.hello()
print("_______________________")
print(type(Hello))
print("_______________________")
print(type(h))
# 要创建一个class对象，type()函数依次传入3个参数
# 1.class的名称 2.继承的父类集合，注意python支持多重继承，如果只有一个父类
# 要记住元组的单元素写法需要一个逗号 3.class的方法名称与函数绑定，这里我们把函数
# fn绑定到了方法名hello上
# 通过tpye函数创建的类和直接写class是完全一样的，因为python解释器遇到class定义语代码时，仅仅是
# 扫描一下class定义的语法，然后调用type()函数创建出class
# 只有类相对于python解释器实实在在存在了，才能被调用
# 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持
# 运行期间动态创建类，这和静态语言有非常大的不同，
# 要在静态语言运行期间创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂
