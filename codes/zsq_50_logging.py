#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_50_logging
# @time: 2018/3/17 11:49
# 代替print查看异常的第三种方式就是logging
# logging不会抛出错误，并且可以输到文件
import logging
logging.basicConfig(level=logging.INFO)


s = "0"
n = int(s)
logging.info("n = %d" % n)
print(10 / n)