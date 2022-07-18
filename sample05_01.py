# 理解容器的意义：使用的方便和便于控制，例如：水桶、水杯、毛笔等

# List（列表）是一种数据结构，用于存储有序可重复的序列
# 语法格式：[元素1，元素2，···，元素n]
# 特点:列表中的元素的数据类型可以相同，也可以不相同，支持数值、字符串或其他数据类型的元素，
#     放到列表中的元素的顺序决定其索引值。
list1=['中国','USA',123]
print('初始化：',list1)  #  初始化： ['中国', 'USA', 123]

# -----获取操作-----
# len()函数：获取列表中元素的个数
print('list1的元素的个数：{0}'.format(len(list1)))  # list1的元素的个数：3

# in关键字和not in关键字：判断元素是否在列表中。
print('中国是否在列表中：{0}'.format('中国'in list1))  # 中国是否在列表中：True
print('123是否在列表中：{0}'.format(123 in list1))  # 123是否在列表中：True

# count(元素名称)函数：获取列表中某个元素的个数
print('list1中123的个数：{0}'.format(list1.count(123)))  # list1中123的个数：1
print('list1中中国的个数：{0}'.format(list1.count('中国')))  # list1中中国的个数：1
print('list1中日本的个数：{0}'.format(list1.count('日本')))  # list1中日本的个数：0

# index(元素名称)函数：获取列表中元素的索引位置。
print('list1中元素中国的索引位置：{0}'.format(list1.index('中国')))  # list1中元素中国的索引位置：0
print('list1中元素123的索引位置：{0}'.format(list1.index(123)))  # list1中元素123的索引位置：2

# 类似字符串序列的索引和切片操作，列表也可以进行索引和切片操作
print('list1[0]:{0}'.format(list1[0]))  # list1[0]:中国
print('list1[1:3]:{0}'.format(list1[1:3]))  # list1[1:3]:['USA', 123]
print('list1[1:2]:{0}'.format(list1[1:2]))  # list1[1:2]:['USA']

# -----新增操作-----
# append()函数：添加元素，在列表的尾部（最右侧）添加
print('初始化列表：{0}'.format(list1))  #  初始化列表：['中国', 'USA', 123]
list1.append(456)
print('append添加元素后的列表：{0}'.format(list1))  #  append添加元素后的列表：['中国', 'USA', 123, 456]

# insert()函数：添加元素，在列表的指定索引位置添加。
print('初始化列表：{0}'.format(list1))  # 初始化列表：['中国', 'USA', 123, 456]
list1.insert(1,'England')
print('insert添加元素后的列表：{0}'.format(list1))  # insert添加元素后的列表：['中国', 'England', 'USA', 123, 456]

# extend()函数：扩展列表，在原有列表尾部（最右侧）扩展添加新列表的内容
list2=['法兰西',888]
print('初始化列表：{0}'.format(list1))  # 初始化列表：['中国', 'England', 'USA', 123, 456]
list1.extend(list2)
print('extend扩展列表后的列表：{0}'.format(list1))  # extend扩展列表后的列表：['中国', 'England', 'USA', 123, 456, '法兰西', 888]

# -----修改操作-----
# 修改元素：首先索引获取到要修改的元素，再进行内容的修改即可
print('初始化列表：{0}'.format(list1))  # 初始化列表：['中国', 'England', 'USA', 123, 456, '法兰西', 888]
list1[1]='俄罗斯'
print('修改元素后的列表：{0}'.format(list1))  # 修改元素后的列表：['中国', '俄罗斯', 'USA', 123, 456, '法兰西', 888]

# -----删除操作-----
# pop()函数：移除元素，无参时移除列表尾部的那个元素，有参时删除索引位置的元素。
print('初始化列表：{0}'.format(list1))  # 初始化列表：['中国', '俄罗斯', 'USA', 123, 456, '法兰西', 888]
list1.pop()
print('pop无参时移除元素后的列表：{0}'.format(list1)) # pop无参时移除元素后的列表：['中国', '俄罗斯', 'USA', 123, 456, '法兰西']
list1.pop(1)
print('pop有参时移除元素后的列表：{0}'.format(list1))  # pop有参时移除元素后的列表：['中国', 'USA', 123, 456, '法兰西']

# remove()函数：移除元素，移除列表中指定内容的元素
print('初始化列表：{0}'.format(list1)) # 初始化列表：['中国', 'USA', 123, 456, '法兰西']
list1.remove(123)
print('remove移除元素后的列表：{0}'.format(list1))  # remove移除元素后的列表：['中国', 'USA', 456, '法兰西']

# del 关键字：移除元素
print('初始化列表：{0}'.format(list1))  # 初始化列表：['中国', 'USA', 456, '法兰西']
del list1[1]
print('del移除元素后的列表：{0}'.format(list1))  # del移除元素后的列表：['中国', 456, '法兰西']

# clear()函数：清空列表
print('初始化列表：{0}'.format(list1))  # 初始化列表：['中国', 456, '法兰西']
list1.clear()
print('clear清空列表后的列表：{0}'.format(list1)) # []