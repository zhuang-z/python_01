"""
print("hello world!") #字符串
print(2333)  #整数
print(2.333) #小数
print(True)  #布尔值  True False
print(())    #元组
print([])    #数组
print({})    #字典

 
锄禾日当午

print("哈哈",2333,2.33)
print("哈哈"+"嘻嘻")
print("哈哈"*100)
print(((1+1)*100-99)/2)
print(2>3)

"""


"""
# 变量 赋值
a = input("请输入a:")
b = input("请输入b:")
print("input获取的内容：",a+b)  #input获取的内容都是以字符串的形式

"""

# print(type("哈哈"))
# print(type(2333))
# print(type(2.33))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))

#数据类型的转换

# a = float(input("请输入a:"))
# b = float(input("请输入b:"))
# print("input获取的内容：",a+b)

# a = "fijfijadija"
# print(type(len(a)))

#计算两个字符串长度之和
# a = input("请输入a:")
# b = input("请输入b:")
# c = len(a)
# d = len(b)
# print("a和b的长度之和为：",c+d)

#元组  下标 0开始

a = (1,2,5,"哈哈","dsa","xixi","xixi",True,False)
# print(a[6])  #输出a元组第七个元素

print(a.index("xixi"))  #输出xixi的下标，从左至右就近原则
print(a.count("xixi"))  #打印有多少个"xixi"


