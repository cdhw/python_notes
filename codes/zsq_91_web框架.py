#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_91_web框架
# @time: 2018/3/31 15:25
from flask import Flask
from flask import request


# def application(environ, start_response):
#     method = environ["REQUEST_METHOD"]
#     path = environ["PATH_INFO"]
#     if method == "GET" and path == "/":
#         return handle_home(environ, start_response)
#     if method == "POST" and path == "/signin":
#         return handle_home(environ, start_response)
app = Flask(__name__)  # 创建flask框架对象app，封装了一个__name__属性


@app.route("/", methods=["GET", "POST"])  # app的route作为装饰器修饰home函数
def home():
    return "<h1>Home</h1>"


@app.route("/signin", methods=["GET"])
def signin_form():
    return '''<form action="/signin" method="post">
    <p><input name="username"></p>
    <p><input name="password" type="password"></p>
    <p><button type="submit">Sign In</button></p>
    </form>
    '''


@app.route("/signin", methods=["POST"])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username'] == "admin" and request.form['password'] == 'password':
        return "<h3> Hello, admin!</h3>"
    return '<h3> Bad username or password </h3>'


if __name__ == "__main__":
    app.run()


# web框架实现了一个关键功能：
# 根据url的不同让wsgi服务器调用不同的函数，从而获得不同的返回值




