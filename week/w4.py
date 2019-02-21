#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
随机生成一个包含1000个字母的字符串，
然后统计该字符串中每个字母的数量，并输出结果（要求结果以字典方式存储）
'''
# import random
# str = "abcdefghijklmnopqrstuvwxyz"
# str1 = ""   # 新的字符串
# for i in range(1000):
#     str1 += random.choice(str)
# print("生成的随机字符串是：",str1)
# dict = {}
# for i in str1:
#     key = dict.get(i)
#     if key==None:dict[i]=1
#     else:dict[i]+=1
# print(dict)




















# import random
# str = "qwertyuioplkjhgfdsazxcvbnm"
# str1 = ""
# for i in range(100):
#     str1 += random.choice(str)
# print("字符串：",str1)
#
# dict = {}
# for i in str1:
#     key = dict.get(i)
#     if key==None:dict[i]=1
#     else:dict[i]+=1
# print(dict)


















import random
str = "qwertyuiopasdfghjklzxcvbnm"
str1 = ""
for i in range(100):
    str1 += random.choice(str)

print(str1)

dict={}
for i in str1:
    key = dict.get(i)
    if key==None:
        dict[i]=1
    else:
        dict[i]+=1
print(dict)