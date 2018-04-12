#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_89_WSGI协议
# @time: 2018/3/31 9:15
from  wsgiref.simple_server import make_server
"""
什么是WSGI？
    可以实现web服务功能的程序接口
    也就是当我们需要用到web服务器的某些功能时，我们直接调用WSGI接口即可
    WSGI可以调用到web服务器的功能，但是我们必须得通过传参告诉web服务器
    具体的资源或者应用程序

"""
# 定义一个WSGI接口函数，只要函数符合WSGI标准就可以被WSGI服务器所调用


def application(environ, start_response):
    start_response("200 ok", [("Content-Type", "text/html")])
    return [b'<h1>hello</h1>']
# application是一个能被web服务器所调用的函数，因为他符合web服务器的标准


httpd = make_server('', 8000, application)  # 创建一个服务器对象，服务器对象调用的函数是application
httpd.serve_forever()  # 服务器进入监听状态
# 这样做虽然能够使wsgi服务器调用此函数，但是灵活性很差，所有的url请求都是调用的同一个函数
# 我们需要做到不同的url能够调用到不同的函数，这才能实现web app的灵活多样性，这就是我们说的web框架



