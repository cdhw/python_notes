#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_88_SQLAlchemy
# @time: 2018/3/30 15:03
from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
"""
我们可以使用元组列表来表示mysql数据库表的结构、
表的每一行数据就是一个元组，也就是列表的元素
python的DB-API程序返回的数据结构就是元组列表,但是元组列表只能看到一行的
字段值，究竟有哪些字段不是很清楚，所以我们要用类来表示表结构，通过
类对象来操作表
可以用一个类对象来封装一行数据，表的字段名作为类的属性名，表的字段
值作为类的属性值
这样一个表有n行数据，则有n类对象
"""


class Student(object):
    def __init__(self, idd, name):
        self.id = idd
        self.name = name


# 这样表的数据结构就是：
# print([Student('12', 'jack'), Student('13', 'tom')])
# 把关系数据库表的结构映射到对象中去的方式，我们称作对象关系映射(ORM)
# 完成映射转换任务的程序我们称作ORM框架
# python中最有名的ORM框架就是SQLAlchemy
# 用declarative_base()方法创建用于封装表行数据对象的基类
# delcarative_base是sqlalchemy.ext.delcarative模块下的一个方法
Base = declarative_base()  # Base是一个类，封装了ORM的功能
# 定义User类，用于封装user表的行数据


class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


class Book(Base):
    __tablename__ = 'book'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    user_id = Column(String(20), ForeignKey('user.id'))


engine = create_engine("mysql+mysqlconnector://root:zsqq007@localhost:3306/python")
DBsession = sessionmaker(bind=engine)
session = DBsession()
'''new_user = User(id="num5", name="mary")
session.add(new_user)'''
# users = session.query(User).filter(User.id == 'num5').one()  # 直接获得一个映射了id为num5那一行数据的对象
# print(users.name)
user = session.query(User).filter(User.id == 'num4').one()  # 获取对象列表
print(user.name)
# new_book = Book(id="b1", name="php", user_id="num1")
# session.add(new_book)
# print(user[0].name)
# print(type(user))  # 查看对象的类型
session.commit()
session.close()









