# 推导式：从一个或者是多个迭代器快速创建序列的方法，将循环和条件判断结合起来，可以避免冗长的代码。
# 列表推导式：
# 语法格式：[表达式 for item in 可迭代对象 if 条件判断]
print([i for i in range(1,5)])  # [1, 2, 3, 4]
print([i*2 for i in range(1,5)])  # [2, 4, 6, 8]
print([i*2 for i in range(1,5) if i%3!=0])  # [2, 4, 8]
print([(row,col) for row in range(1,4) for col in range(1,3)])  # [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]
print([i for i in 'temptation'])  # ['t', 'e', 'm', 'p', 't', 'a', 't', 'i', 'o', 'n']
