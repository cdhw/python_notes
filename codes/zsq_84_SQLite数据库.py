#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_84_SQLite数据库
# @time: 2018/3/28 6:11
"""
SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite是C语言写的，体积小，经常被集成到各种应用
程序中去，甚至IOS和Android的App应用中都可以集成
python内置了SQLite3，在python中不需要安装任何东西，直接使用SQLite
什么是？
    表是数据库中存放关系数据的集合，一个数据库含多个表，表和表之间通过外键关联
怎样操作关系数据库？
    首先需要连接到数据库，一个数据库连接称为Connection
    连接到SQLite之后，需要打开游标，称之为Cursor，通过游标Cursor执行SQL语句，然后，获得执行结果
任意数据库要满足怎样的条件才能连接到python？
    Python定义了一套操作数据的API接口，任何数据库要连接到Python，只需要提供符合Python标准
    的数据库驱动即可
Python中怎样使用SQLite这个轻量级、嵌入式、关系型数据库？
    SQLite的数据库驱动程序内置在Python标准库中，所以可以直接操作SQLite数据库
"""
import sqlite3
'''conn = sqlite3.connect('test.db')  # 创建一个数据库连接对象
cursor = conn.cursor()  # 创建一个游标对象
cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
cursor.execute("insert into user (id, name) values (\"1\", \"Jack\")")  # 此处引号用作字符串成员所以需要转义，不代表引号
print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()'''
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("select * from user where id=?", ("1",))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
'''
使用python数据库API接口时，要注意些什么？
    在使用DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用了
在执行了insert(增)、delete(删)、(update)等语句之后，怎样拿到执行结果？
    可以通过rowcount返回的受影响的行数来拿到执行结果。
通过Cursor对象执行select语句时，fetchall()获取到的是一个什么数据类型？
    cursor的select查询时，fetchall方法拿到的是一个结果集，是一个元组列表，每一个元组对应一行字段的记录值，只有值
SQL语句是怎样传参的？
    通过Cursor对象的execute方法执行SQL语句时，若有参数，我们需要把参数按照位置传递给execute方法，
    有几个参数就有个几个"?"占位符
    例如：cursor.execute("select * from user where name=? and pwd=?", ('abc', 'password'))
SQLite支持常见的标准SQl语句和几种常见的数据类型
'''



