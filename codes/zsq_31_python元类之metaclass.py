#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-13 13:36
# @Author  : Henry
# @File    : zsq_31_python元类之metaclass.py
# @Software: PyCharm
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
# metaclass，直译为元类，简单的解释：
# 通常我们定义了类之后，就可以根据这个类创建出实例，所以一般流程是，先有了类，再会有对象
# 但是如果说我们通过定义类的方式，而是创建出类呢？那就必须根据metaclass创建出类，这种流程是，先有了metaclass类，再会有对象
# 也就是先定义metaclass类，然后通过metaclass类创建类，再然后创建类的对象
# 所以，metaclass允许你创建类或者修改类，换句话说，你可以认为类是metaclass的对象
# 举个例子：我们先定义一个ListMetaclass类，再自定义一个MyList类，通过可以通过ListMetaclass类给MyList类添加
# 一个add方法
# 先定义ListMetaclass类
# metaclass是类的模板，所以必须从type类型派生


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs["add"] = lambda self, value:self.append(value)
        attrs["name"] = "Jack"
        return type.__new__(cls, "Zhang", bases, attrs)  # 返回一个类：MyList 、__new__()是创建对象的方法
# __new__()方法接收到的参数分别是：
# cls:当前准备创建的类的对象
# name 类的名字
# 类继承的父类集合，是一个元组
# 类的方法和属性集合
# 有了ListMetaclass，我们在自定义类的时候还要指示使用ListMetaclass来定制类，
# 传入关键字参数metaclass


class MyList(list, metaclass=ListMetaclass):  # 传入了关键字参数metaclass后，python解释器再创建类MyList时，就会执行
    # ListMetaclass中的方法中的程序
    pass
# 只要我们传入了关键字参数metaclass,作用就生效了，当python解释器在创建MyList类时，会通过ListMetaclass.__new__()方法
# 来创建，在这个方法里，我们可以修改类的定义，例如，添加新的方法


l = MyList()
l.add("zhang")
print(l)
print("VVVVVVVVVVVVVVVVVVVVVVVV")
print(l.name)
print("AAAAAAAAAAAAAAAAAAAAAAAAA")
print(MyList.__bases__)



