#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 定位到某个位置 seek()
# seek(offset,from)   offset:偏移量   from:方向
# 0表示文件开头  1表示当前位置  2表示文件末尾

f = open("E:\\杨莎莎\\Python\\Python1_Exam\\Python_Lianxi\\text2.txt","r")
str = f.read(30)
print("读取的数据是：",str)

# 查找当前位置
position = f.tell()
print("当前的位置是：",position)

# 重新设置位置
f.seek(5,0)

# 查找当前位置
position = f.tell()
print("当前位置是：",position)

f.close()