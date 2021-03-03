#  类

class Test():   #类名首字母必须大写
    def __init__(self):    #初始化  参数必须是self
        self.name = "haha"
        self.sex = "男"
        self.age = 20

    def caiyi(self,num):   #self之后可以定义别的参数
        if num ==1:
            print("篮球!")
        elif num == 2:
            print("足球!")
        else:
            print("网球!")
    
#对象的实例化

zhangsan = Test()
zhangsan.caiyi(2)
print(zhangsan.name)


#继承  重写/多态
class Test1(Test):
    def caiyi(self):
        print("修电脑!")

lisi = Test1()
lisi.caiyi()
