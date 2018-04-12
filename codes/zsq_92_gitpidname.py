#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_92_获得进程id
# @time: 2018/4/2 17:59
from subprocess import check_output


def get_pid(name):
    return map(int,check_output(["pidof",name]).split())


name = input("请输入进程名字")
idso = get_pid(name)
