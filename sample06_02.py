# 创建空元组的方式：
tuple1=()
print('空元组为：{0}'.format(tuple1)) # 空元组为：()
print('类型为：{0}'.format(type(tuple1))) # 类型为：<class 'tuple'>

# 元组中放入元素的顺序决定了其索引值，元素可以重复
tuple2=(123,'中国',123,'中国')
print(tuple2[0]) # 123

# 元素支持拆包操作（unpack）
tuple3=('合肥','铜陵','淮南')
str1,str2,str3=tuple3
print(str1) # 合肥
print(str2) # 铜陵
print(str3) # 淮南

# 在回味变量的系列赋值，可以理解把一个元组赋值给另一个元组
tuple3='合肥','铜陵','淮南'
str1,str2,str3=tuple3
print(str1) # 合肥
print(str2) # 铜陵
print(str3) # 淮南

# 变量前使用*，拆包操作时，将除去星号变量之外的其他常规变量赋值后，剩下的元组中的元素以一个列表的形式赋值给带有星号的变量
str4,*str5=tuple3
print(str4) # 合肥
print(str5) # ['铜陵', '淮南']

# 元组做拆包操作时，只能出现一个星号变量
# 执行出错：SyntaxError: two starred expressions in assignment
# str6,*str7,*str8=tuple3
# print(str6)
# print(str7)
# print(str8)

str6,*str7,str8=tuple3
print(str6) # 合肥
print(str7) # ['铜陵']
print(str8) # 淮南

*str6,str7=tuple3
print(str6) # ['合肥', '铜陵']
print(str7) # 淮南

# 元组拆包时，支持英文下划线_做占位符的使用
str9,_,str10=tuple3
print(str9) # 合肥
print(str10) # 淮南
print(_) # 铜陵

_,_,str11=tuple3
print(str11) # 淮南
print(_) # 铜陵
print(_) # 铜陵

