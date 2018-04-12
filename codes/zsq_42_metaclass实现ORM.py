#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_42_metaclass实现ORM
# @time: 2018/3/16 23:02
# ORM对象关系映射、就是将类的属性值赋给一个对象
# field类实例：用于封装一个字段的名字属性和一个字段的数据类型属性
# StringField类实例：封装了一个具体字段名和字段数据类型是字符串的对象
# IntField类实例：封装了一个具体字段名和字段数据类型是整型的对象
# ModelMetaclass 该类的__new__方法作用于另外一个类，控制另外一个类的生成
# Model类，是所有数据表类的父类，定义了保存字段值到数据库的方法
# 表类，一个表类对应一个数据表，表类中定义了表中的所有字段属性、字段的属性值是封装了该字段名和该字段的数据类型的一个对象


class Field(object):
    """ 封装字段名和字段类型"""
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type


class StringField(Field):
    """封装字段名和字符串类型"""
    def __init__(self, name):
        super().__init__(name, "str")


class IntField(Field):
    def __init__(self, name):
        super().__init__(name, "int")


class ModelMetaclass(type):
    """作用于表类，生成一个目标表类"""
    def __new__(cls, name, bases, attrs):
        if name is "Model":
            return type.__new__(cls, name, bases, attrs)
        print("发现了新的表模型:%s" % name)

        mappings = {}
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
        for i, n in mappings.items():
            attrs.pop(i)
        attrs["__mappings__"] = mappings
        attrs["__table__"] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __getattr__(self, item):
        try:
            self[item]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % item)  #r的作用是去掉转义效果

    def save(self):
        name_list = []
        value_list =[]
        for i, j in self.__mappings__.items():
            name_list.append(i)
            value_list.append(self[i])
        print(name_list, value_list)


class User(Model):
    id = IntField("id")
    user = StringField("user")


u = User(id=123, user="tom")
print(u)
print(u.save())
# print(u.jack)
print(r"\t \r")






