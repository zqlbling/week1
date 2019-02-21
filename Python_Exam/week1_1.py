#!/usr/bin/env python 
# -*- coding:utf-8 -*-


# 用python语句判断所输入的手机号，是否正确
phone = input("请输入手机号：")
rigth = "138"
rigth1 = "158"
rigth2 = "176"
rigth3 = "152"
rigth4 = "187"
if len(phone)==11:
    if phone.isalnum():
        if phone.startswith(rigth) or phone.startswith(rigth1) \
                or phone.startswith(rigth2) or phone.startswith(rigth3) \
                or phone.startswith(rigth4):
            print("输入正确")
else:
    print("手机号码长度不对")
'''
 编写程序，生成一个包含50个随机整数的列表，随机整数的范围是从-10到10，
 然后将列表中所有的正数存为一个新的子列表，负数存为另一个新的子列表
'''
import random
list1 = []
list2 = []
i=1
while i<52:
    num = random.choice(range(-10, 10))
    i+=1
    if num<0:
        list1.append(num)
    elif num>0:
        list2.append(num)
print("正整数：",list1)
print("负整数",list2)

'''
编写程序，生成一个包含20个随机整数的列表，
然后对其中偶数下标（下标即列表元素的索引）的元素进行降序排列，
奇数下标的元素不变。
'''
list3 = []
list4 = []
j=1
while j<22:
    num = random.choice(range(0, 100))
    j+=1
    if num%2==0:
        list3.append(num)
        list3.sort()
    if num%2!=0:
        list4.append(num)

print(list3)
print(list4)

'''
随机生成一个包含1000个字母的字符串，
然后统计该字符串中每个字母的数量，并输出结果（要求结果以字典方式存储）
'''
list5 = []
list6 = []
j=1
while j<1000:
    str = random.choice("abcdefghijklmnopqrstuvwxyz")
    print(str,end="")


s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python '
