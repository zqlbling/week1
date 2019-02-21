#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#不定长参数：
def fun1(arg1,*arg2):
    print(arg1)
    for i in arg2:
        print(i)

fun1(100)
fun1(100,200,300)

# 使用两层循环，生成全排列
mn = [m + n for m in "ABC" for n in "XYZ"]
print(mn)

d = {'x':1,'y':2,'z':3}
for k,v in d.items():
    print(k,"=",v)

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
for i in L:
    L = i.lower()
    for i in L:
        print(i,end="")
    print(" ")

# L = ['Hello', 'World', 'IBM', 'Apple',78,23.6]
# for i in L:
#     if isinstance(i,str):
#         print(i.lower(), end="   ")
#     else:

print(int(1.6)) # 1

# 通过递归计算阶乘
def fun1(x):
    if x==1:
        return 1
    else:
        return x*fun1(x-1)

num = int(input("请输入一个数字："))
print("{0}的阶乘是：{1}".format(num,fun1(num)))

# 使用递归的方式来生成斐波那契数列：
def fibo(n):
    if n<=1:
        return 1
    else:
        return (fibo(n-1)+fibo(n-2))

n = int(input("您要输出几项？"))
if n<=0:
    print("输入有误！")
else:
    print("斐波那契数列：")
    for i in range(n):
        print(fibo(i),end=" ")


# 匿名函数，用lambda关键词创建的小型匿名函数，这种函数省略了用def声明函数的标准步骤
sum = lambda arg1,arg2:arg1+arg2
print("\n",sum(10,20))
