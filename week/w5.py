#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python ' \
对这段文字中的单词进行数字统计，并且进行个数升序
（能够生成字典8分，字典中统计数正确7分，进行排序8分，最后实现结果7分）
"""
s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python'
s = s.split(" ")
print(s)    # 切割后输出
dict = {}
for i in s:
    key = dict.get(i)
    if key==None:dict[i]=1
    else:dict[i]+=1 # 统计每个单词的个数

dict1 = {}
sv = list(dict.values())
sv.sort()
print(sv)   # 输出每个单词的次数  升序

for i in sv:
    for j in dict:
        if dict[j]==i:
            dict1[j]=i
print(dict1)