L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0], L[1], L[2])
r = []
n =3
for i in range(n):
    r.append(L[i])
print(r)
print("______________________")
print(L[1:])
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-2:])
print(L[-2:-1])
L = list(range(100))
print(L)
#通过切片取出前10个数
print(L[0:10])
#通过切片取出后10个数
print(L[:-11:-1])
print(L[-10:])
#前11-20个数
print(L[10:20])
#前10个数，每两个取一个
print(L[:10:2])
#所有数，每5个取一个
print(L[::5])
#原样复制列表
print(L[:])
#tuple也是一种列表（list)，唯一区别是tuple不可修改，因此，tuple也可以用切片操作，操作的结果仍然是tuple
yuan_zu=(0,1,2,3,4,5)
print(yuan_zu[:3])
#字符串'xxx'也可以看成是一种list，每个元素就是一个字符，因此字符串也可以用切片操作，操作结果仍然是字符串
user_name="zhangshiqiang"
print(user_name[:3])
#利用字符串的切片操作去除字符串两端的空格、实现字符串trim()函数的功能
girl="beautiful    "
print(girl[:-4])
print(girl.strip())

