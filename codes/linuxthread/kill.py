#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: kill
# @time: 2018/4/2 17:26
import os

process = "/tomcat/tomcat.lock"
os.system("ps -ef|grep apache-tomcat-6.0.35|grep -v grep >%s" % process)  # 将进程信息写入lock文件
if not (os.path.getsize(process)):  # 判断文件大小，当tomcat没有运行时上一步写入lock的内容为空
    os.system("/tomcat/apache-tomcat-6.0.35/bin/startup.sh")

