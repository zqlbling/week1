#!/usr/bin/env python
# -*- coding:utf-8 -*-
import turtle
'''
运动命令
forward(d)  向前移动d长度
backword(d) 向右移动d长度
right(d)    向右转动d度
left(d)     向左转动d度
goto(x,y)   移动到坐标为(x,y)的位置
speed(speed)     笔画绘制的速度[0,10]

笔画控制命令
penup()    笔画抬起，在移动时不会划线
pendown()  笔画落下
setheading(d)   改变海龟的朝向
pensize(d)  笔画的宽度
pencolor(colorstr)  笔画颜色
reset() 恢复所有设置，清空窗口，重置turtle状态
clear() 清空窗口，不会重置turtle
circle(r,e) 绘制一个圆形，r为半径，e为次数(可以不写)

其他命令
done()  程序继续执行
'''
#创建实例
t = turtle.Turtle()
# t.right(90)
# t.forward(100)
'''

t.penup()
t.goto(100,100)
t.pendown()
# 设置画笔颜色
t.pencolor("green")
# 设置填充颜色
t.fillcolor("yellow")
# 开始填充
t.begin_fill()
for i in range(2):
    t.forward(100)
    t.right(90)
    t.forward(150)
    t.right(90)

# 结束填充
t.end_fill()
'''

# 全部封装成函数--设置颜色函数
def setColor(color):
    t.pencolor(color)
    # 设置填充颜色
    t.fillcolor(color)
    # 隐藏箭头
    t.hideturtle()

def setPen(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)

# x  y是长方形的左下角
def rect(x,y,w,h,color):
    setColor(color)
    setPen(x,y)
    t.setheading(90)
    t.begin_fill()
    for i in range(2):
        t.forward(h)
        t.right(90)
        t.forward(w)
        t.right(90)
    t.end_fill()

# 里面是一周的天气温度
temps = [16,17,22,30,21,27,24]
def line_chart(x,y,color,temps,pixel,space):
    setPen(x,y)
    setColor(color)
    for i,j in enumerate(temps):
        x1 = x + (j + 1) * space
        y1 = y + j * pixel
        t.goto(x1,y1)

line_chart(0,0,'red',temps,10,30)

# rect(100,100,200,100,"green")
# 最后一步一定要写
turtle.done()