#coding:utf8
print(abs(-10))
x = abs(-10)
print(x)
f = abs
print(f)
print(f(-100))
def hello():
    print("hello")
hello()
g = hello
g()
hello = 10
g()
cond = False
if not cond:
    pass


def stop():
    print("my name is zhangshiqiang")
# stop()
action = stop
# print(action)
# action()
def start(say, action):
    print(say)
    action()
start("hi",action)


def count(n, total=1):
    for i in range(1,n+1):
        total *= i
    print(total)
count(13)



