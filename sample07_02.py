  # 集合的增删改查操作
# 创建空集合
set1=set()
print('空集合为：{0}'.format(set1)) # 空集合为：set()

# -------新增操作--------
# add()函数：在集合中添加元素，如果添加的元素在集合中不存在，则随机添加到某个位置；如果添加元素在集合中存在，则不做添加操作。
print('add前：{0}'.format(set1)) # add前：set()
set1.add(123)
print('add后：{0}'.format(set1)) # add后：{123}
set1.add(456)
print('add后：{0}'.format(set1)) # add后：{456, 123}
set1.add(789)
print('add后：{0}'.format(set1)) # add后：{456, 123, 789}
set1.add(123)
print('add后：{0}'.format(set1)) # add后：{456, 123, 789}

# -------修改操作-------
# update()函数：传入的参数为字符串时，会将字符串拆分为单个字符，随机放入集合中
print('update前：{0}'.format(set1)) # update前：{456, 123, 789}
set1.update('abc')
print('update后：{0}'.format(set1)) # update后：{'b', 456, 'c', 'a', 789, 123}
set1.update('中国')
print('update后：{0}'.format(set1)) # update后：{'b', 456, 'c', '中', 'a', '国', 789, 123}
# update函数传入参数为数值时，执行出错
# 下句执行出错：TypeError: 'int' object is not iterable
# set1.update(222)
# print('update后：{0}'.format(set1))
# 为了放入集合中的字符串不被拆分，需要将字符串放入在容器型的对象中，再使用update()函数
set1.update(['日本'])
print('update后(通过传入列表容器)：{0}'.format(set1)) # update后(通过传入列表容器)：{456, '中', 'a', '国', 789, 'b', '日本', 'c', 123}
set1.update(('USA',))
print('update后(通过传入元组容器)：{0}'.format(set1)) # update后(通过传入元组容器)：{'USA', 'a', 456, '中', '国', 'c', 789, 123, '日本', 'b'}
set1.update({'英国',666})
print('update后（通过传入集合容器）：{0}'.format(set1)) # update后（通过传入集合容器）：{'b', 'c', 'USA', 'a', 456, '国', '英国', '中', 789, '日本', 666, 123}
# 对于集合已经存在的元素，进行update()更新操作，没有变化
set1.update([123])
print('update后（通过传入存在元素）：{0}'.format(set1)) # update后（通过传入存在元素）：{'日本', '英国', '国', 456, 'a', 'b', '中', 'c', 789, 'USA', 666, 123}
set1.update((123,))
print('update后（通过传入存在元素）：{0}'.format(set1)) # update后（通过传入存在元素）：{'c', 456, '英国', '国', 'a', 'b', 789, '中', 666, 123, 'USA', '日本'}
set1.update({123})
print('update后（通过传入存在元素）：{0}'.format(set1)) # update后（通过传入存在元素）：{456, 'c', 'USA', '日本', 'a', '英国', '国', 789, '中', 666, 123, 'b'}

# --------删除操作--------
# discard()函数：删除元素，对于集合中不存在的元素进行删除，不会抛出异常
print('discard前：{0}'.format(set1)) # discard前：{'英国', 'b', 'a', 456, '中', 'c', 'USA', 789, '日本', 666, 123, '国'}
set1.discard('USA')
print('discard后：{0}'.format(set1)) # discard后：{'英国', 'b', 'a', 456, '中', 'c', 789, '日本', 666, 123, '国'}
set1.discard('俄罗斯')
print('discard后：{0}'.format(set1)) # discard后：{'英国', 'b', 'a', 456, '中', 'c', 789, '日本', 666, 123, '国'}

# remove()函数：删除元素，对集合中不存在的元素进行删除，会抛出异常
print('remove前：{0}'.format(set1)) # remove前：{'c', 456, '国', 666, 789, '中', 'a', '日本', 'b', 123, '英国'}
set1.remove('日本')
print('remove后：{0}'.format(set1)) # remove后：{'c', 456, '国', 666, 789, '中', 'a', 'b', 123, '英国'}
# 下句执行出错：KeyError: '俄罗斯'
# set1.remove('俄罗斯')
# print('remove后：{0}'.format(set1))

# clear()函数：清空
set1.clear()
print('clear后：{0}'.format(set1)) # clear后：set()
