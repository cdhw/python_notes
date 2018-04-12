# coding:utf8
from types import MethodType


class Student(object):
    pass


s = Student()
s.name = "zhang"  # 给对象绑定一个属性，只对当前对象生效
print(s.name)


def play(self, who):
    print(who+" is playing basketball")


s.play = MethodType(play, s)  # 给s对象绑定了一个方法
s.play("zhangshiqiang")
#  S.play()  #另外一个对象S是没有此方法的
#  如果说想针对封装的所有对象都能够有play()这个方法，可以针对Student绑定play()方法
Student.play = play  # 给类绑定了play()方法
S = Student()
S.play("李四")
S.play("李四")