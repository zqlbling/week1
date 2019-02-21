import random
'''
请写出一段代码实现删除一个list里面的重复元素
'''
a = {1,1,2,5,9,3}
b = list(set(a))
print("删除重复数字后：",b)

'''
将所有元素进行随机排序
'''
list = [10,30,520,90,10]
random.shuffle(list)
print("随机排序后：",list)

'''
replace()替换
replace("需要替换的","替换内容",替换次数)
'''
a = "hello python I'm YangShasha"
b = a.replace("h","o",2)
print(b)

#元祖中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
tup1 = (20,)
print(type(tup1))   #<class 'tuple'>

#字典
dict = {"name":"Yss","age":18,"from":"Luoyang"}
print(dict['name'])

list = {1,1,2,5,9,2,5,7}
list1 = set(list)   #set去重  去除重复的元素
print(list1)

print("我的姓名是：{:~>8}".format("杨莎莎"))


#字符串属于不可变对象，但是确实需要修改，可以使用io.StringIo()
str = "Hello world"
import io
str1 = io.StringIO(str)
print(str1)
str1.seek(6)
str1.write("W")
print(str1.getvalue())

#推导式生成列表
a = [x*2 for x in range(1,100) if x%8==0]
print(a)

print(12/4)
print(12//4)

#倒叙输出
for i in range(5,0,-1):
    print(i,end=" ")
print("")

l = [x*x for x in range(1,11)]
print(l)

# 输入一个数计算阶乘
sum=0
sum1=1
num = int(input("请输入一个数："))
for i in range(1,num+1):
    sum1 *= i
    sum += sum1
print("阶乘之和是：",sum)
print("另一种方法：")
import math
sum = 0
num = int(input("请输入一个数："))
for i in range(1,num+1):
    sum+=math.factorial(i)
print("阶乘之和是：",sum)


# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=k)and(i!=j)and(j!=k):
                print(i,j,k,end="    ")
    print(" ")