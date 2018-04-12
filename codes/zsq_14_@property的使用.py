#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_14_@property的使用
# @time: 2018/3/10 15:12


# 在给对象绑定属性时，我们可以直接给对象添加属性并赋值，这样直接暴露属性的方法，操作简单，但是没法限制属性的取值
# class Student(object):
#     def set_score(self, score):
#         if not isinstance(score, int):
#             raise ValueError("it must be an integer! ")
#         if score < 0 or score > 100:
#             raise ValueError("it must between 0~100!")
#         self.score=score
#
#
# s = Student()
# s.score = 999
# print(s.score)
# s.set_score(99)  # 分数为9999，这是不合理的，必须得限制一个范围
# 为了限制score的范围，我们可以通过添加一个set_score()方法来设置成绩，再通过一个get_score()方法来获取成绩，这样就可以限定属性的取值了
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter  #该装饰器用来给属性赋值
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("It must be an integer!")
        if value < 0 or value > 100:
            raise ValueError("It must be between 0~100")
        self._score = value


s = Student()
s.score = 60
print(s.score)
s.score = 88
print(s.score)


