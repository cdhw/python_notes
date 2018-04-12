#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_85_SQLite数据库习题
# @time: 2018/3/28 7:05
import sqlite3, os
'''try:
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    cursor.execute("select*from user where id=?", ("1",))
    result = cursor.fetchall()
    print(result)
except:
    print("error!")
finally:
    cursor.close()
    conn.close()'''
# 如果当前模块所在目录下有与数据库文件同名的模块文件，为了不产生混淆，将其删除
# 查找指定分数段的人名
# db_file = os.path.join(os.path.dirname(__file__), "test.db")
# if os.path.isfile(db_file):
#     os.remove(db_file)


def get_score(num1, num2):
    cursor.execute("select name from student where score between ? and ? order by score", (num1, num2))
# cursor.execute函数的第二个参数是参数元组，和前面的占位符一一对应


conn = sqlite3.connect("info.db")
cursor = conn.cursor()
# try:
cursor.execute("create table if not exists student (id varchar(20) primary key, name varchar(30), score int(100))")
# except:
#     print("create table filed")
# finally:
# cursor.execute("insert into student values ('num1', 'tom', 79), ('num2', 'jack', 88)")
# cursor.execute("select*from student")
get_score(50, 90)
students = cursor.fetchall()
# num = len(students)
# print(num)
print(students)
cursor.close()
conn.commit()  # 提交事务
conn.close()






