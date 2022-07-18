# 交互中接收多个赋值的变量，通过系列赋值结合内置函数eval()把赋值的多个数据内容转换为相应的数值内容
num1,num2,num3=eval(input('输入三个，使用英文逗号,做分隔：'))
print('输入的数字为：',num1,num2,num3,type(num1),type(num2),type(num3))
# 例如如下输入：1，'123',45
# 结果为：输入的数字为： 1 123 45 <class 'int'> <class 'str'> <class 'int'>
