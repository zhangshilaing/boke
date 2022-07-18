# 需求：字符串abcdefg，获取其反转的值gfedcba
str='abcdefg'

# 写法一：字符串的切片写法
print(str[::-1])  # gfedcba

# 写法二：字符串转换成列表，再利用列表的reverse()函数做反转，再遍历列表做字符串的拼接
list1=[]
for item in str:
    list1.append(item)
print('字符串转换成列表：{0}'.format(list1))  # 字符串转换成列表：['a', 'b', 'c', 'd', 'e', 'f', 'g']
list1.reverse()
print('反转后的列表：{0}'.format(list1))  # 反转后的列表：['g', 'f', 'e', 'd', 'c', 'b', 'a']
result=''
for item in list1:
    result+=item
print('遍历列表拼接字符串：{0}'.format(result))  # 遍历列表拼接字符串：gfedcba

# 写法三：列表的内置函数结合字符串的内置函数。
list1=list(str)
print('字符串转换成列表：{0}'.format(list1))  # 字符串转换成列表：['a', 'b', 'c', 'd', 'e', 'f', 'g']
list1.reverse()
print('反转后的列表：{0}'.format(list1))  # 反转后的列表：['g', 'f', 'e', 'd', 'c', 'b', 'a']
# 使用字符串的内置函数str.join(iterable)
#说明： Return a string which is the concatenation of the strings in iterable. A TypeError will be raised if there are
#   any non-string values in iterable, including bytes objects. The separator between elements is the string providing this method.
print('列表转换成字符串：{0}'.format(''.join(list1)))  # 列表转换成字符串：gfedcba

