#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_36_数据优化方案
# @time: 2018/4/12 6:23
"""优化数据库：
数据库优化从6个层次来说：
1、  减少数据访问（减少磁盘访问）
    1、创建并使用正确的索引
    2、只通过索引访问数据
    3、优化SQL执行计划

2、  返回更少数据（减少网络传输或磁盘访问）
    1、数据分页处理
    2、只返回需要的字段

3、  减少交互次数（减少网络传输）
    1、batch DML
    2、In List
    3、Fetch Size
    4、使用存储过程
    5、优化业务逻辑
    6、使用ResultSet游标处理记录

4、  减少服务器CPU开销（减少CPU及内存开销）
    1、使用绑定变量
    2、合理使用排序
    3、减少比较操作
    4、大量运算在客户端处理

5、  利用更多资源（增加资源）
    1、客户端多进程并行处理
    2、数据库并行处理
6、  常见的SQL语句优化

1、索引
2、外键
3、事务
4、join代替子查询
5、"""
