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

# print(a[6])  #输出a元组第七个元素   正着数0、1、2、3……  倒着数-1、-2、-3……

#切片
# print(a[0:3])   #左闭右开  0可以省略，最后可以不写
# print(a[3:7])
# print(a[7:])


#只能操作一维元组
# print(a.index("xixi"))  #输出xixi的下标，从左至右就近原则
# print(a.count("xixi"))  #打印有多少个"xixi"

#二维元组

# b = (a,"哈哈","嘻嘻")
# print(b[0][2])   #打印a元组里面的第三个元素  并列执行：b的第一项，a的第三项


#数组   元组一旦写好过后是不可以修改的，但数组是可以修改的。

# a = [1,2,5,"哈哈","dsa","xixi","xixi",True,False]

# a.append("append")   #向数组中添加数据，添加在最末尾

# a.insert(0,"insert")  #向数组指定位置插入数据

# a.pop(6)   #剪切指定下标的数据

# print(a)

# b = ["你好","不好"]

# a.extend(b)  #合并数组 将b合并到a中

# a.remove("xixi")  #删除固定的值，0可以是"0"也可以是"False",1可以是"1"也可以是"True"

# print(a)

#a.clear()    清空数组



#字典的值没有顺序；字典的结构必须是键值对：key:value

a = {"name":"zhangsan",
     "sex":"nan",
     "age":25
    }
#取值
print(a["name"])       #写入不存在的key第一个代码会报错，第二个会显示None
b = a.get("name")
print(b)

#新增
a["high"] = "183cm"
print(a)
a.update(grd = 1111)
print(a)

#修改
a["name"] = "lisi"
print(a)

#剪切
b = a.pop("name")
print(b)


#数组和字典的删除  del a["name"]  del a[0]



