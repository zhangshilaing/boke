# for循环
# 语法格式：
# for var in sequence：
#       循环体

# range：一种不可变序列类型
# 通过range()函数，生成数字序列（number sequence）
print(range)  # <class 'range'>
print(range(5))  # range(0, 5)
print(range(1,5,2))  # range(1, 5, 2)

# range()函数传入一个参数，表示生成了从0到参数值减1的范围的数字序列
for i in range(3):
    print(i)  # 0 1 2

# range()函数传入两个参数，表示生成了一个区间范围（从第一个参数到第二个参数减1）的数字序列
for i in range(4,7):
    print(i)  # 4 5 6

# range()函数传入三个参数，表示按步长（间隔数）生成一个区间范围（从第一个参数到第二个参数减1）的数字序列
for i in range(1,10,2):
    print(i) # 1 3 5 7 9
