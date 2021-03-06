# 集合中的元素通过什么保证无序状态下可以被找到？
set1=set([123])
print('集合为：{0}'.format(set1))

# 下句描述的是往集合对象容器中放入的元素的类型为列表类型，执行出错
# 下句执行出错：TypeError: unhashable type: 'list'
# set1={[123]}
# print('集合为：{0}'.format(set1))

# 下句描述的是往集合对象容器中放入的元素类型为元组类型，执行正确
set1={(123,)}
print('集合为：{0}'.format(set1)) # 集合为：{(123,)}

# hash()函数：返回对象的哈希值（这个哈希值是否存在，保证在无序的情况下，是否被找到）
# 下句执行出错：TypeError: unhashable type: 'list'
# print(hash([123]))
# 元组对象有相应的哈希值
print(hash((123,))) #哈希值： 3429901387204
print(id((123,))) # 内存中的地址：2650467457096

