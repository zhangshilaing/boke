# 问题：创建只有一个元素的元组

# 首先想到的是英文小括号中放入一个元素
# tuple1=(123)
# print('只有一个元素的元组{0}'.format(tuple1)) # 只有一个元素的元组123
# print('类型为{0}'.format(type(tuple1))) # 类型为<class 'int'>

# 如果tuple1这个变量是元组对象的话，那么应该支持索引访问，但是下句执行出错，证明该变量不是元组对象
# 执行出错：TypeError: 'int' object is not subscriptable
# print(tuple1[0])
# 综上所述，上面的在英文小括号中放入一个元素创建只有一个元素的元组的写法是不正确的

# 创建只有一个元素的元组
# 正确的创建方式1：在英文小括号中放入一个元素和一个英文的逗号
tuple2=(123,)
print('只有一个元素的元组{0}'.format(tuple2)) # 只有一个元素的元组(123,)
print('类型为{0}'.format(type(tuple2))) # 类型为<class 'tuple'>

# 正确的创建方式2：放一个元素和一个英文逗号
tuple3=123,
print('只有一个元素的元组{0}'.format(tuple3)) # 只有一个元素的元组(123,)
print('类型为{0}'.format(type(tuple3))) # 类型为<class 'tuple'>
