#!/usr/bin/env python 
# -*- coding:utf-8 -*-


# 打开文件：
f = open("E:\\杨莎莎\\Python\\Python1_Exam\\Python_Lianxi\\text.txt","r+")
# 关闭文件
# f.close()

# 文件的读写
# 写数据(writer)
f = open("E:\\杨莎莎\\Python\\Python1_Exam\\Python_Lianxi\\text.txt","r+")
# f.write("曾经沧海难为水，除却巫山不是云"+"\n")
# f.write("我亦飘零久，十年来，深恩负尽，死生师友"+"\n")
# f.write("老来多健忘，唯不忘相思"+"\n")
# f.write("安能摧眉折腰事权贵，使我不得开心颜"+"\n")
print(f.readline())
print("-"*30)
print(f.read(15))

count = f.readlines()
print(type(count))  #<class 'list'>
i=1
for j in count:
    print("%d:%s"%(i,j))
    i+=1
f.close()

# 获取当前读写的位置 tell()
f = open("E:\\杨莎莎\\Python\\Python1_Exam\\Python_Lianxi\\text2.txt","r")
print(f.read(5))
print("读取当前的位置：",f.tell())  # 10
print(f.read(6))
print("读取当前的位置：",f.tell())  # 12
f.close()

