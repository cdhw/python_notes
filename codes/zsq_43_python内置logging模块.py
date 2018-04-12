#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_43_python内置logging模块
# @time: 2018/3/17 4:18
# python内置的logging模块，可以非常容易地记录错误信息
import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar("0")
    except Exception as e:
        print("logging捕捉到的异常时红字？")
        logging.exception(e)



print("XXXXXXXXXXXXXXXXXXXXXXXX")

try:
    int([1, 2, 3])
# except TypeError as e:
#     print("错误是")
#     print(e)
except Exception as e:
    print("logging捕获到的")
    logging.exception(e)  # 虽然是红字错误，就像python解释器报错一样，但是用logging模块捕捉到的红字错误不会终止python解释器的工作
finally:
    print("over")
