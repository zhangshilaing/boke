# Python中的字符串是一种序列
str1='abcdefg'
# 字符串：a   b   c   d   e   f   g
# 索引值：0   1   2   3   4   5   6 （从左向右）
# 索引值：-1 -2  -3  -4  -5  -6  -7  (从右向左)

print(str1) # abcdefg

# 字符串的操作
# 1、+：字符串之间进行拼接
print(str1+'temptation') # abcdefgtemptation
# 执行出错：TypeError: can only concatenate str (not "int") to str
# print(str1+123)

# 2、*：重复输出字符串
print(str1*2) # abcdefgabcdefg

# 3、[]:通过索引获取字符串中字符内容
#      规则：索引值从0开始
print(str1[0]) # a
print(str1[1]) # b

# 4、[m:n] :通过切片操作截取字符串中的一部分或全部
#    语法格式：变量名称[起始索引:终止索引]
#    语法规则：包左不包右，索引值从左向右以0作为起始值，从右向左以-1作为起始值
# [:]:提取字符的全部内容（切片）
print(str1[:]) # abcdefg
print(str1[0:2]) # ab
print(str1[0:4]) # abcd
print(str1[1:-2]) # bcde
print(str1[1:-1]) # bcdef
print(str1[3:]) # defg
print(str1[:3]) #abc

# 5、[m:n:s]:结合步长（间隔数）通过切片操作截取字符串的一部分或全部
#   语法格式：变量名称[起始索引：终止索引：步长]
print(str1[0:6:2]) # ace

# 需求：对于已知的字符串，通过代码操作得到逆向内容
# 比如：abcdefg，通过代码操作得到gfedcba
# 写法1：理解序列的含义，理解起始索引、终止索引、步长（间隔数）的正负值的含义
print(str1[::-1]) # gfedcba
#写法2：考虑字符串对象自身是否有反转函数，查看文档进行测试
# print(str1.reverse())
# 执行出错：AttributeError: 'str' object has no attribute 'reverse'

# 6、in：如果字符串中包含有给定的字符串，返回True
#    not in：如果字符串中不包含有给定的字符串，返回False
print('天'in'天融信') # True
print('天下'in'天融信') # False
print('天'not in'天融信') # False




