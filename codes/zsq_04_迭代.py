#coding:utf-8
#如果给定一个list或者tuple，我们可以通过for循环来遍历这个list或者tuple，这种遍历我们称为迭代(lteration)
#在python中，迭代是通过 for ... in来完成的， 而很多语言比如C语言， 迭代list是通过下标完成的，比如Java代码：
# for (i=0; i<list.length; i++){
#      n = list[i]
# }
#pythond 的for循环抽象程度比较高，只要是可以迭代的对象都可以使用for循环
# d = {"a":1, "b":2, "c":3}
# for key in d:#key 代表键 是随机取的
#     print(d[key])
#
#
# for value in d.values():
#     print(value)
#
#
# for key,value in d.items():
#     print((key,value))
#
#
# #字符串应用于迭代
# name = "jackson"
# for ch in name:
#     print(ch)
# #总结：只要对象可以迭代，我们就可以把它应用于for循环，而不需要关心它是否是哪种数据类型
# #判断一个对象是否是可迭代对象的方法：
# #调用collections模块的Iterable类型判断：
# from collections import Iterable
# judge1 = isinstance("abc", Iterable) #str是否可迭代
# print(judge1)
# judge2 = isinstance([1,2,3], Iterable)
# print(judge2)
# judge3 = isinstance(123, Iterable)
# print(judge3)
# #实现索引-值的for循环迭代
# for i, value in enumerate(["a","b","c"]):
#     print((i,value))
# #在python中，引入两个变量的for循环是很常见的
# for x, y in [(1,1), (2,4), (3,9)]:
#     print(x, y)
#应用迭代的方式查询出一个列表中的最大值和最小值,并返回一个tuple
List= [2,8,1,4,5]
def findMinAndMax(L):
    return (None, None)
num = len(List)
for i in range(1,num):#外圈为需要比较的轮次num-1轮
    for j in range(num-i):#内圈为每轮需要比较的次数
        if(List[j]>List[j+1]):
            last = List[j]
            List[j]=List[j+1]
            List[j+1]=last
print((List[0],List[num-1]))
if findMinAndMax([]) == (None, None):
    print("测试成功")
elif findMinAndMax([7]) !=(7):
    print("测试失败")
elif findMinAndMax([7, 1]) != (1, 7):
    print("测试失败")
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print("测试失败")
else:
    print("测试成功")