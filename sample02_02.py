# 问题： 理解Python中布尔类型和数值类型的关系
# 内置函数isinstance（）判断变量是否为某种数据类型的实现
i=123
print(isinstance(i,int)) #True

flag=True
print('变量flag是否为bool类型的实现：',isinstance(flag,bool)) # 变量flag是否为bool类型的实现： True
print('变量flag是否为int类型的实现：',isinstance(flag,int)) # 变量flag是否为int类型的实现： True
print('变量flag是否为float类型的实现：',isinstance(flag,float)) # 变量flag是否为float类型的实现： False
print('变量flag是否为complex类型的实现：',isinstance(flag,complex)) # 变量flag是否为complex类型的实现： False

print(True) # True
print(False) # False
print(True+False) # 1
print(True+True) # 2
print(False+False) # 0
print(False+True) # 1
print(True+123) # 124
print(False+123) # 123

# 注意：Python2的数据类型中没有布尔类型，用数字0对应False，用数字1对应True；
#      python3中，把True、False两个关键字用起来，做算术运算时，等价于1和0
