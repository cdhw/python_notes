#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-12 9:45
# @Author  : Henry
# @File    : zsq_21_续说python定制类.py
# @Software: PyCharm
# python 类中有许多类似于__slots__、 __len__()的特俗变量或者特殊函数、
# python的class中有许多像__len__()这样具有特殊用途的函数，可以帮助我们定制类、
# 定义一个Student类，打印一个实例：


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):

        return "Student object (name:%s)" % self.name # 打印封装对象的时候就会自动调用此方法
    # 和__init__()一样，也是一个触发方法，达到某个条件自动执行的程序片段

    __repr__ = __str__


print(Student("jack"))  # 打印出来的是一个对象，及其存储地址这种数据没有参考价值，可以进行一个转换
#  在对象中定义一个__str__()方法，可以返回一个好看的字符串

# 如果一个对象想作为一个迭代对象使用，那么这个对象必须实现__iter__()方法，该方法返回一个可迭代对象
# 然后for循环会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到拿到的值是StopIteration错误时退出循环


# 先定义Fib类
class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):  # 斐波那契数,在这里不断地调用__next__()函数就相当于for循环
      self.a, self.b = self.b, self.a+self.b # 不断地循环此段运算，就得到了斐波那契数
      if self.a > 100:
          raise StopIteration # 抛出异常
      return self.a

    def __getitem__(self, item):
        a, b = 0, 1
        # 通过别人传参的类型来判断是想获取一个值，还是一个列表的值
        if isinstance(item, int):
            for x in range(item):
                a, b = b, a+b # 该段程序会被运算item次
            return a  # 运算item次后的a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            L = []
            for x in range(stop):
                if start is None:
                    start = 0
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L


f = Fib()
for i in f:  # 对象被放到for循环当中后就会一直调用__next__方法，一直循环，f对象不断通过__next__函数拿值，拿到值后遍历给i
    print(i)


# 以上是对象作用于for循环的例子，但是它和list作用于for循环是不一样的，对象作用于for循环是靠循环调用某段程序
# 来产生数据供for循环使用，而list是现成的元素值，所以我们不能像列表那样打印出f[1]的值

print("""hello""")
print(f[9])  # 提示对象不支持索引
# 要想该对象支持索引的功能，需要给对象引入__getitem__()方法
# 以上是要获取第item次运算后a的值，但是如果我们要求第n次到第m次运算后a的值的列表，则需要重新传参
print(f[1:8])
print("隔一行")
print(f[:10]) # 前10次运算后a的列表
# 可以通过一些特殊的方法，将对象表现出列表、字典、元组的一些特性

