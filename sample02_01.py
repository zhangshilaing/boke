# Python中的基本数据类型：六种
# Number（数值），String(字符串)，List（列表），Tuple（元组），Set（集合），Dictionary（字典）

# Number（数值）：细分为四种
# int（整型）、float（浮点型）、bool（布尔类型）、complex（复数型）
i=123
print(i)
print(type(i)) # <class 'int'>

j=1.21
print(j)
print(type(j)) # <class 'float'>

flag1=False
print(flag1)
print(type(flag1)) # <class 'bool'>

flag2=True
print(flag2)
print(type(flag2)) # <class 'bool'>

# 注意：下语句中的j和前面的变量j无关，表示为复数的虚部标识符号
k=1+2j
print(k)  # (1+2j)
print(type(k)) # <class 'complex'>


