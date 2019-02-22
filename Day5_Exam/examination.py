#!/usr/bin/env python 
# -*- coding:utf-8 -*-


# if you in (depressed, sadness, resignation):
#     print 'me, my sweetheart'
# if feel(you) is 'lonely' or feel(you) is 'neglected':
#     talk_me(this)
# while always:
#     I.take_care(you)
# if you.love() is not me:
# # I will follow in the madness
# # I will
#     break # down...
# for emotion in my.heart:
#     try:
#       your.lover = me
#     except:
#       your.best_friend = me
#     if you.hate(me):
#         love(me)
#     elif I.annoying():
#         # love(me)
#     else:
#         love(me, how='deeply', when='now')



"""
通过用户输入数字，计算阶乘
"""
num = int(input("请输入数字："))
def jc(num):
    if num==1:return 1
    else:return jc(num-1)*num
print(jc(num))




"""
判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，
如果能被整除，则表明此数不是素数，反之是素数。
"""
for i in range(101,201):
    if i%2==0 or i%3==0 or i%5==0 or i%7==0:pass
    else:print(i,end="  ")



"""
将一个列表的数据复制到另一个列表中，并反向排序输出
"""

list = [1,9,5,"name","Yss"]
list1 = []
for i in range(len(list)):
    list1.append(list[i])
print("\n反向排序后：",list1[::-1])


#
# """
# s='The column above illustrates apparently' \
#   ' the polularity of people ' \
#   'doing exercise in a certain year ' \
#   'from 2013 to 2018.Based upon the data,' \
#   'we can see that python is wonderful. ' \
#   'python is wonderful. Python ' \
# 对这段文字中的单词进行数字统计，并且进行个数升序
# （能够生成字典8分，字典中统计数正确7分，进行排序8分，最后实现结果7分）
# """


# s='The column above illustrates apparently' \
#   ' the polularity of people ' \
#   'doing exercise in a certain year ' \
#   'from 2013 to 2018.Based upon the data,' \
#   'we can see that python is wonderful. ' \
#   'python is wonderful. Python'
# s = s.split(" ")
# print(s)    # 切割
# dict = {}
# for i in s:
#     key = dict.get(i)
#     if key==None:dict[i]=1
#     else:dict[i]+=1
# dict1 = {}
# sv = list(dict.values())
# sv.sort()
# print(sv)
#
# for i in sv:
#     for j in dict:
#         if dict[j]==i:
#             dict[j]=i
# print(dict)











# s = 'The column above illustrates apparently' \
#   ' the polularity of people ' \
#   'doing exercise in a certain year ' \
#   'from 2013 to 2018.Based upon the data,' \
#   'we can see that python is wonderful. ' \
#   'python is wonderful. Python'
# s = s.split(" ")    # 切割"  "空格分隔
# print(s)
# dict = {}
# for i in s:
#     key = dict.get(i)
#     if key == None:dict[i]=1
#     else:dict[i]+=1     #统计每个单词的次数
# dict1 = {}
# sv = list(dict.values())
# sv.sort()   # 把次数进行排序
# print(sv)
# for i in sv:
#     for j in dict:
#         if dict[j]==i:
#             dict1[j]=i  #   字典的键值对全部排序输出
# print(dict1)













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

# s='The column above illustrates apparently' \
#   ' the polularity of people ' \
#   'doing exercise exercise exercise in a certain year ' \
#   'from  2013 2013 2013 to 2018.Based upon the data,' \
#   'we can see that python is wonderful. ' \
#   'python is wonderful wonderful wonderful wonderful. Python'
# s = s.split(" ")
# print(s)
# dict = {}
# for i in s:
#     key = dict.get(i)
#     if key==None:dict[i]=1
#     else:dict[i]+=1
#
# dict1 = {}
# sv = list(dict.values())
# sv.sort()
# print(sv)
#
# for i in sv:
#     for j in dict:
#         if dict[j]==i:
#             dict1[j]=i
# print(dict1)


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
print(s)
dict = {}
for i in s:
    key = dict.get(i)
    if key==None:dict[i]=1
    else:dict[i]+=1

dict1 = {}
sv = list(dict.values())
sv.sort()
print(sv)

for i in sv:
    for j in dict:
        if dict[j]==i:
            dict1[j]=i
print(dict1)