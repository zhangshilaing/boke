# 字典的键：通过hash()函数判断某个变量或表达式是否可以成为字典的键

# 数值、字符串可以hash
print(hash(123)) # 123
print(hash(123.45)) # 1037629354146168955
print(hash('temptation')) # -8083951146728523746

# 列表不能hash，不能成为字典的键
# 下句执行出错：TypeError: unhashable type: 'list'
# print(hash([]))
# print(hash([1,2,3]))

# 元组可以hash
print(hash(())) # 3527539
print(hash((123,))) # 3429901387204

# 集合不能hash，但是frozenset集合可以hash
# 下句执行出错：TypeError: unhashable type: 'set'
# print(hash(set()))
print(hash(frozenset())) # 133146708735736

# 下句执行出错：TypeError: unhashable type: 'list'
# print({[]:123})
# 下句执行出错：TypeError: unhashable type: 'set'
# print({set():123})
