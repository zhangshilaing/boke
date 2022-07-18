# 问题：int()函数和eval()的区别？
# 答：int()函数不能用于非整型数值内容的字符串；
#    eval()函数可以用于整型数值内容的字符串，也可以用于非整型数值内容的字符串
#     不能使用数字前导（即形如：0+某个数值内容的形式）
print(int('3')) # 3
print(type(int('3'))) # <class 'int'>
# 执行出错：ValueError: invalid literal for int() with base 10: '3.14'
# print(int('3.14'))

print(eval('3')) # 3
print(type(eval('3')))  # <class 'int'>
print(eval('3.14')) # 3.14
print(type(eval('3.14'))) # <class 'float'>
# 执行错误：SyntaxError: invalid token
# print(eval('03'))