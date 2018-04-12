#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_94_通过redis限制用户登录次数
# @time: 2018/4/3 9:31
import redis
import sys
import time
r = redis.StrictRedis(host='127.0.0.1', port=6379)
r.set('foo', '字节')  # 存入内存的‘字节’是被编码了的字节码
print(r.get('foo').decode())
