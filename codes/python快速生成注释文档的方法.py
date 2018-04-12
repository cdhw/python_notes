#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: python快速生成注释文档的方法.py
# @time: 2018/3/10 13:28
import sys
"""
文档快速生成注释的方法介绍,首先我们要用到__all__属性
在Py中使用为导出__all__中的所有类、函数、变量成员等
在模块使用__all__属性可避免相互引用时命名冲突

"""


__all__ = ['Login', 'check', 'Shop', 'upDateIt', 'findIt', 'deleteIt', 'createIt']


class Login:
    """
    测试注释——可以写上此类的作用说明等
    例如此方法用来写登录

    """
    pass

    def __init__(self):
        """
        此处注释你的类实例化的时候需要初始化的哪些属性，也就是对象最初封装的属性值
        例如，如果涉及到登录，我们可能要用到用户名username，密码password等等
        """
        pass

    def check(self):
        """
        协商你要实现的功能说面
        功能有很多，包括验证、判断语句、验证码等等
        """
        pass


class Shop:
    """
    商品类所包含的属性及其方法
    update 改/更新
    find 查找
    delete 删除
    create 添加
    """

    def __init(self):
        """
        初始化商品的价格、日期、分类等等
        """
        pass

    def upDateIt(self):
        """
        更新商品信息
        """
        pass

    def findIt(self):
        """
        查找商品信息
        """

    def deleteIt(self):
        """
        删除过期下架商品信息
        """
        pass

    def createIt(self):
        """
        创建新商品及上架信息
        """
        pass


if __name__ == "__main__":
    import python快速生成注释文档的方法
    # print(help(python快速生成注释文档的方法))


print(help(sys))  # 查看对象的详细说明、包括所有注释及其各种说明
