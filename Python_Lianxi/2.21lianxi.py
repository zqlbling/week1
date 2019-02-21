#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 实现100-200里面所有的质数字,打印这些质数并且求出个数
for i in range(100,201):
    if (i%2!=0)and(i%3!=0)and(i%5!=0)and(i%7!=0):
        print("100-200之间的质数有：",i)


# import random
# list=[]
# count=0
# for i in range(100,201):
#     b=1
#     for j in range(2,i):
#         if i%j==0:
#             b=0
#             break
#     if b == 1:
#         list.append(i)
#         count=count+1
import random
list = []
count = 0
for i in range(100,201):
    a = 1
    for j in range(2,i):
        if i%j==0:
            a=0
            break
    if a==1:
        list.append(i)
        count = count+1


print('质数是',list)
print('数量为',count)


# 电脑随机生成1~100随机数，用户输入一个数字，
# 电脑提示用户大或者小，猜错，继续提示；猜对，则程序终止。
import random
a = random.choice(range(1,101))
print(a)
print("请输入1-100之间的数字：")
while 1:
    b = int(input())
    if a==b:
        break
    elif a>b:
        print("输入的数字较小")
    elif a<b:
        print("输入的数字较大")