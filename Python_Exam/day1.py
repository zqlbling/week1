'''
1. 输入班级的班号、人数、当前所学课程，并且原样输出。（30分）
'''
grade = input("请输入班级的班号：")
people = input("请输入班级的人数：")
study = input("请输入当前所学课程：")
print("班号是：{0}，班级人数：{1}，当前所学课程：{2}。\n".format(grade,people,study))

'''
2. 输入一个数字，求其绝对值。（30分）
'''
num = input("请输入一个数：")
num = int(num)
print("{0}的绝对值是{1}\n".format(num,num.__abs__()))

'''
3.输入一个数字，判断其是否大于60，如果大于60则输出及格，否则输出不及格（40分）
'''
a = input("请输入一个数字：")
a = int(a)
if a>60:
    print("及格")
else:
    print("不及格")
