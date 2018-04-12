#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-13 11:03
# @Author  : Henry
# @File    : zsq_30_python元类.py
# @Software: PyCharm
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
# 例如我们要定义一个Hello的class, 我们就写一个hello.py的模块


class Hello(object):
    def hello(self, name = "world"):
        print("Hello, %s." % name)
# 上面定义的一个类，本身是保存在一个文本文件当中的，如果python解释器不去碰它的话，
# 它本身就是一个除了解释器没有任何作用的文本，就是一个理论上的类，并没有真正地被实现
# 当python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建
# 出一个Hello的class对象，测试如下
#利用type()函数创造类


def fn(self, name="world"):  # 必须要self参数，这是类定义方法所必须的一个参数

    print("Hello, %s." % name)


Hell = type("Hell", (object,), dict(hello=fn))
h = Hell()
print("_______________________")
h.hello()



