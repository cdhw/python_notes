#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_24_什么是类的静态方法？
# @time: 2018/4/5 8:19
"""我们知道实例方法是类的实例都能够访问的方法，静态方法是一种普通函数(没有self参数
有self参数代表是实例方法，有cls参数代表是类方法）
，位于类的命名空间中
，但是不会对任意实例进行操作，类的定义方式是：@staticmethod（装饰器）
类对象和实例都可以访问静态方法"""


class Employee(object):
    def __init__(self, name, age=18, salary=2000, role="basic"):  # 扩展属性
        self.name = name
        self.age = age
        self.salary = salary
        self.role = role

    @property
    def get_age(self):  # 获取属性的值
        return self.age

    @get_age.setter
    def get_age(self, age):  # 给属性赋值
        if 18 < age < 60:
            self.age = age
        else:
            print("invalid parameter \r \n")

    @classmethod
    def transport(cls):
        print("take shuttle bus")

    @staticmethod
    def hello_world():  # 此处不能加self，加了会被认为是一个普通参数，无法识别类和实例
        print("Hello there")


michael = Employee('michael')
# michael.hello_world()
# Employee.hello_world()
Employee.transport()  # 类访问类方法
michael.transport()  # 实例访问类方法 因为实例也属于当前类型
michael.age = 60
print(michael.get_age)  # 装饰器 property将get_age方法转换成了属性
michael.get_age = 30
print(michael.age)

