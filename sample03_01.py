# Python中使用一对英文单引号''或一对英文双引号""包裹上内容形成字符串

str1='中国'
str2='中华人民共和国'
print(str1) # 中国
print(type(str1)) # <class 'str'>
print(isinstance(str1,str)) # True
print(str2) # 中华人民共和国
print(type(str2)) # <class 'str'>
print(isinstance(str1,str)) # True

# 多行语句写在一行中可以使用英文分号进行分隔，但是不推荐这样的写法，因为可读性差
str3='中国';str4='中华人民共和国'
print(str3,str4) # 中国 中华人民共和国
print(id(str1)) # 2987328563024
print(id(str3)) # 2987328563024
print(str1 is str3) # True
print(id(str2)==id(str4)) # True

# 长字符串：对于内容较多的字符串，可能写在一行中不够清晰，考虑写在多行中，可以使用一对由三个单引号包裹起来内容

print('''
内容很多，
写一行里看不清楚，
跨行编写
''')
# 内容很多，
# 写一行里看不清楚，
# 跨行编写


