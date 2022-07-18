# 不可变集合(frozenset)：使用frozenset()函数创建的集合是不可变集合
set1=frozenset({'中国','USA',123})
print('不可变集合为：{0}'.format(set1)) # 不可变集合为：frozenset({123, '中国', 'USA'})
print('类型为：{0}'.format(type(set1))) # 类型为：<class 'frozenset'>

# 下句执行出错：AttributeError: 'frozenset' object has no attribute 'add'
# set1.add(123)
set2={'中国','USA',123}
print('可变集合为：{0}'.format(set2)) # 可变集合为：{'USA', 123, '中国'}
print('类型为：{0}'.format(type(set2))) # 类型为：<class 'set'>
# 下句执行出错：TypeError: unhashable type: 'set'
# 可变集合对象没有相应的哈希值
# print(hash(set2))

# 不可变集合对象有相应的哈希值
print(hash(set1)) # -8397972638737870612

print('集合对象中只能嵌套不可变集合对象元素：{0}'.format(set1)) # 集合对象中只能嵌套不可变集合对象元素：frozenset({'中国', 123, 'USA'})

# 集合对象中的元素类型可以是数值、字符串、元组、不可变集合，不能是列表和可变集合

