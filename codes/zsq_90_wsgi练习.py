#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_90_wsgi练习
# @time: 2018/3/31 11:24
from wsgiref.simple_server import make_server


'''def hit(environ, start_response):  # 定义函数要按照wsgi标准来，这样才可以被服务器所调用
    start_response("200 ok", [("Content-Type", "text/html")])  # 相应头
    return [b'<span> zhangsan! </span>']


httpd = make_server('', 888, hit)
print("服务器监听中...")
httpd.serve_forever()'''


'''def hit(environ, start_response):
    start_response("200 ok", [("Content-Type", "text/html")])
    body = '<h1>hello %s </h1>' % (environ["PATH_INFO"][1:] or "web")
    return [body.encode("utf8")]


httpd = make_server("", 999, hit)
httpd.serve_forever()'''


# def hit(environ, start_response):
#     start_response("200 ok", [("Content-Type", "text/html")])
#     body = "<h1>hello %s </h1>" % (environ["PATH_INFO"][1:] or "web")
#     return [body.encode("utf8")]  # 进行网络传输前，用utf8将其序列化成二进制
#
#
# httpd = make_server("", 666, hit)
# print("httpd start...")
# httpd.serve_forever()
# print("ok")
def hello(environ, start_response):
    start_response("200 ok", [("Content-Type", "text/html")])
    body = "hello %s!" % (environ["PATH_INFO"][1:] or "web")
    return [body.encode("utf8")]


httpd = make_server("", 777, hello)
httpd.serve_forever()
