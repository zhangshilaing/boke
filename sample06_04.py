# 推导式：从一个或者是多个迭代器快速创建序列的方法，将循环和条件判断结合起来，可以避免冗长的代码

# 生成器推导式（生成元组）
# 语法格式：（表达式 for item in 可迭代对象 if 条件判断）
print((i for i in range(1,5))) # <generator object <genexpr> at 0x0000017A4EA7B848>
obj=(i for i in range(1,5))
print(obj) # <generator object <genexpr> at 0x000001C2206DB8C8>

for item in obj:
    print(item,end=' ') # 1 2 3 4
# 生成器推导式生成的元组只能被遍历一次，再次遍历时无数据
for item in obj:
    print(item,end=' ')
# 换行
print()

# 使用元组创建形式创建的元组，可以被遍历多次
tuple1=(1,2,3,4,5)
for i in tuple1:
    print(i,end=' ') # 1 2 3 4 5

print()

for i in tuple1:
    print(i,end=' ') # 1 2 3 4 5