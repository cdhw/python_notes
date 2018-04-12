#coding=utf8
#在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print(fact(4))
#分析：fact(n-1)=(n-1)*fact(n-2)=(n-1)*(n-2)*fact(n-3)=(n-2)*(n-2)*(n-3)*fact(n-4)...*fact(n-(n-1))结束

print(fact(1000))#每一次函数调用占用的栈帧是不会被释放的，要保留到最后的乘法运算结束之后才会被释放，
# 程序的运算流程是实现所有的递归函数后再实现乘法运算
#解决栈溢出的方法：尾部递归优化，即在函数return处不要加入运算，直接调用函数，这样一来，只会占用一个栈帧
def fact(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1 ,num*product)
#以上原理是让程序不断地调用同一个函数，且下一次调用的第一个参数是上一次调用的第一个参数减一
#下一次调用的第二参数是上一次调用的第二个参数乘于下一次调用的第一个参数，直到第一个参数为1停止调用
#以上流程其实就是for循环