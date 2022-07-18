# 使用for循环对字典进行遍历
dict1={'秦皇':'嬴政','汉武':'刘彻'}
print('初始化字典：{0}'.format(dict1)) # 初始化字典：{'秦皇': '嬴政', '汉武': '刘彻'}

# 只使用for循环的遍历，遍历得到的是字典的键
for i in dict1:
    print(i) # 秦皇 汉武

# 结合for循环和字典的keys()函数，遍历得到的是字典的键
for i in dict1.keys():
    print(i) # 秦皇 汉武

# 结合for循环、字典的keys()函数和通过键获取值的两种方式，遍历得到的字典的键和值
for key in dict1.keys():
    print(key,dict1[key]) # 秦皇 嬴政 汉武 刘彻
    print(key,dict1.get(key)) #秦皇 嬴政 汉武 刘彻

# 结合for循环、字典的items()函数，遍历得到的字典的键值对（每个键值对都是一个元组，再通过系列赋值）
for key,value in dict1.items():
    print(key,value) #  #秦皇 嬴政 汉武 刘彻

