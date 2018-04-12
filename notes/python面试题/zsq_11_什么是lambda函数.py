# lambda表达式是定义匿名函数的语法
from functools import reduce
print(reduce(lambda x, y: x * y+1, range(1, 5)))  # 将前两个数的运算结果和后一个数一起继续调用函数







