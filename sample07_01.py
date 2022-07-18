# Set(集合)：用来存储无序、不可重复的元素的容器
# 语法结构：{元素1，元素2，···，元素n}
# 创建空集合
set1={}
print('空集合为：{0}'.format(set1)) # 空集合为：{}
print('数据类型为：{0}'.format(type(set1))) # 数据类型为：<class 'dict'>
# 从上句的执行结果得知，使用一对英文大括号创建的不是一个空集合对象，而是一个空字典对象

# 正确创建空集合的方式：
set1=set()
print('空集合为：{0}'.format(set1)) # 空集合为：set()
print('数据类型为：{0}'.format(type(set1))) # 数据类型为：<class 'set'>

set2={'中国','USA',123}
print('集合为：{0}'.format(set2)) # 集合为：{'中国', 123, 'USA'} 或 集合为：{123, 'USA', '中国'},多次执行程序，可能会得到不同的元素位置的结果

set3={'中国','USA',123,'中国',123}
print('集合为：{0}'.format(set3)) # 集合为：{123, '中国', 'USA'}

# len()函数：获取集合对象中元素的个数
print('集合set1的长度为：{0}'.format(len(set1))) # 集合set1的长度为：0
print('集合set2的长度为：{0}'.format(len(set2))) # 集合set2的长度为：3
print('集合set3的长度为：{0}'.format(len(set3))) # 集合set3的长度为：3
