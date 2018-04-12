#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_86_mysql
# @time: 2018/3/28 18:11
# 导入mysql驱动
import mysql.connector
# 创建mysql连接对象
conn = mysql.connector.connect(user="root", password="zsqq007", database="python")
# 创建游标对象
cursor = conn.cursor()
# 列举所有数据库
'''cursor.execute("select*from user")
re = cursor.fetchall()
for y in re:
    print(y)'''
# cursor.execute("create table if not exists user (id varchar(20) primary key, name varchar(20))")
# cursor.execute("insert into user values ('num1','tom'),('num2', 'jack')")
# cursor.execute("insert into user value (%s, %s)", ['num4', 'henry'])
# print(cursor.rowcount)
# cursor.execute("select name from user where id = %s", ('num3',))
cursor.execute("select * from user")
data = cursor.fetchall()  # 获取元组列表，每一个元组就是每一行的字段值，但是没有附带字段名字
print(data)
cursor.close()
conn.commit()
conn.close()
