# 判断
# a = 1
# b = 2

# if a==1:
#     print("hello")

# if a > b:
#     printf("a比b大")
# else:
#     print("b更大")

# age = int(input("请输入你的年龄:"))   #input方法输入的是字符串，要用到是需要进行数据类型转换
# if age > 60:
#     print("您可以退休了！")
# elif age > 30:
#     print("您的责任还很重！")
# elif age > 20:
#     print("请规划好您的未来！")
# else:
#     print("好好学习！")

# if age > 20 and age <=30:
#     print("11111")
# elif age > 30 and age <= 40:
#     print("22222")
# elif age >40 and age <=60:
#     print("33333")
# else:
#     print("44444")

# a = input("请输入年龄：")
# if a == "":
#     print("不能为空！")
#     exit()
# if a in "0123456789":         #in 用来判断a的值是不是在某个值、数组、字典里面
#     a = int(a)
# else:
#     print("请输入正确的年龄！")
#     exit()   #退出方法

# if a > 5:
#     print("大")
# else:
#     print("小")


# a = "sada"
# if type(a) is int:   #is 用来判断数据类型
#     print("是数字")
# elif type(a) is str:
#     print("是字符串")
# else:
#     print("其他")



#while 循环

# a = 1
# while a < 10:
#     print("11111")
#     a += 1

#录入10个同学的成绩，姓名和成绩对应上，大于60和小于60分开存放
# hgrade = {}
# lgrade = {}
# studentlist = ["张三","李四","王五","六六","狗蛋","麻子","平安","中国","邮政","快递"]
# a = 0
# while a < len(studentlist):
#     grade = int(input("请输入"+studentlist[a]+"的成绩："))   #数据类型的转换
#     if grade >= 60:
#         hgrade[studentlist[a]] = grade
#     else:
#         lgrade[studentlist[a]] = grade

#     a += 1
# print("大于60分的：",hgrade)
# print("小于60分的：",lgrade)

#for 循环

# a = "你好，今天吃了吗？"
# a = ["张三","李四","王五","六六","狗蛋","麻子","平安","中国","邮政","快递"]
# for i in a:
#     print(i)    #i遍历对象中的每一个值

#range(0,100,3)   自动生成一个数列  左闭右开   0到100中 步长为3 

# b = list(range(0,100,3))
# print(b)

#录入10个同学的成绩，姓名和成绩对应上，大于60和小于60分开存放
# hgrade = {}
# lgrade = {}
# studentlist = ["张三","李四","王五","六六","狗蛋","麻子","平安","中国","邮政","快递"]
# for a in studentlist:
#     grade = int(input("请输入"+a+"的成绩："))   #数据类型的转换
#     if grade >= 60:
#         hgrade[a] = grade
#     else:
#         lgrade[a] = grade
# print("大于60分的：",hgrade)
# print("小于60分的：",lgrade)

#打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"X",i,"=",i*j,end="  ")
#     print()

#打印模拟红绿灯：红灯30次，绿灯35次，黄灯3次
# i = 1
# while i == 1:
#     a = 30
#     b = 30
#     c = 3
#     while a > 0:
#         print("红灯还有",a,"秒结束")
#         a -= 1
#     while b > 0:
#         print("绿灯还有",b,"秒结束")
#         b -= 1
#     while c > 0:
#         print("黄灯还有",c,"秒结束")
#         c -= 1

# while True:
#     light = {"红灯":30,"绿灯":35,"黄灯":3}
#     for i in light:
#         for j in range(light[i]):
#             print(i,"还有",light[i]-j,"秒结束")



#实现注册功能，输入账号(5-8位，小写字母开头)密码(6-12位)，存到字典中
# user={}
# username = input("请输入账号：")
# password = input("请输入密码：")
# if username == "" or password == "":
#     print("不能为空！")
#     exit()
# if len(username) >= 5 and len(username) <=8: 
#     if len(password) >= 6 and len(password) <=12:
#         if username[0:1] in "qwertyuiopasdfghjklzxcvbnm":
#             user["username"] = username
#             user["password"] = password
#             print(user)
#             print("注册成功！")
#         else:
#             print("账号的首字母必须小写！")
#     else:
#         print("请输入密码数大于等于6且小于等于12！")
# else:
#     print("请输入账号数大于等于5且小于等于8！")

    
# def 方法名(变量参数)   def:方法的声明,checkname:方法的名字,username:方法的参数
# def checkname (username):
#     if len(username) >= 5 and len(username) <=8: 
#         if username[0:1] in "qwertyuiopasdfghjklzxcvbnm":  
#             print("注册成功！")
#         else:
#             print("账号的首字母必须小写！")
#     else:
#         print("请输入账号数大于等于5且小于等于8！")

# checkname("4dawdawd")

#异常捕获   
# try:  except Exception as e (异常类打印错误信息): 
#异常类





