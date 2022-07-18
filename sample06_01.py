# Tuple(元组)是一种数据类型，和List(列表)类似，但是元组不能去新增、修改、删除元素，元组是不可变序列
# 语法格式1：（元素1，元素2，···，元素n）
# 语法格式2： 元素1，元素2，···，元素n
tuple1=('中国','USA',123)
print('初始化元组：{0}'.format(tuple1))
print('类型为{0}'.format(type(tuple1)))
tuple2='中国','USA',123
print('初始化元组：{0}'.format(tuple2))
print('类型为{0}'.format(type(tuple2)))

# 元组虽然不支持新增、修改、删除的操作，但是可以使用连接操作形成新的元组
tuple3=('Japan',456)
print('tuple3的地址为{0}'.format(id(tuple3)))
print(tuple1+tuple3)
print('tuple1+tuple3地址为{0}'.format(id(tuple1+tuple3)))