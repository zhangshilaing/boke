 # 创建空列表方式1、使用[]
list1=[]
print(list1) # []

# 创建空列表方式2、使用list()函数
list1=list()
print(list1) # []

# 列表的特点：元素放入列表的顺序决定其索引值，元素可重复
list1=[123,'中国',123,'中国']
print(list1)  # [123, '中国', 123, '中国']

# max()函数和min()函数：只能用于元素均为数值类型的列表
# 写法一：直接使用列表定义的形式
list1=[1,2,3,4,5]
print(list1)  #  [1, 2, 3, 4, 5]

# 写法二：考虑到输出多个连续的数字，所以可以使用range()函数
list1=range(1,6)
print(list1)  # range(1, 6)

# 写法三：考虑到输出多个连续的数字，所以可以使用range()函数，再使用list()函数，传入生成的range()数值序列，得到数值序列列表
list1=list(range(1,6))
print(list1)  # [1, 2, 3, 4, 5]
print('列表中最大值为：{0}'.format(max(list1)))  # 列表中最大值为：5
print('列表中最小值为：{0}'.format(min(list1)))  # 列表中最小值为：1

# list1=[1,2,'合肥','123',5]
# 下句执行出错：TypeError: '>' not supported between instances of 'str' and 'int'
# print(max(list1))
# 下句执行出错：TypeError: '<' not supported between instances of 'str' and 'int'
# print(min(list1))

# reverse()函数：列表中元素的反转
print('初始化列表：{0}'.format(list1))  # 初始化列表：[1, 2, 3, 4, 5]
list1.reverse()
print('反转后的列表：{0}'.format(list1))  # 反转后的列表：[5, 4, 3, 2, 1]

# sort()函数：列表的排序
print('初始化列表：{0}'.format(list1))   # 初始化列表：[5, 4, 3, 2, 1]
list1.sort()
print('顺序排序后的列表：{0}'.format(list1))  # 顺序排序后的列表：[1, 2, 3, 4, 5]
list1.sort(reverse=True)
print('逆序排序后的列表：{0}'.format(list1))  # 逆序排序后的列表：[5, 4, 3, 2, 1]

