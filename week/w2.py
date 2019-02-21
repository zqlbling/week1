#!/usr/bin/env python 
# -*- coding:utf-8 -*-

'''
编写程序，生成一个包含50个随机整数的列表，随机整数的范围是从-10到10，
然后将列表中所有的正数存为一个新的子列表，负数存为另一个新的子列表
'''
#
# import random
# list1 = []
# list2 = []
# for i in range(50):
#     num = random.choice(range(-10,10))
#     if num>0:list1.append(num)
#     if num<0:list2.append(num)
# print("正数：",list1)
# print("负数：",list2)
















#
# import random
#
# list3 = []
# list4 = []
# for i in range(50):
#     num2 = random.choice(range(-10,10))
#     if num2>0:list3.append(num2)
#     if num2<0:list4.append(num2)
# print(list3)
# print(list4)















import random
list5 = []
list6 = []
for i in range(60):
    num3 = random.choice(range(-11,11))
    if num3 >0:list5.append(num3)
    if num3 <0:list6.append(num3)
print(list5)
print(list6)