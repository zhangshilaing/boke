#字符串常用的内置函数
str1='pythontemptation'

# 1、len():获取字符串长度
print(len(str1)) # 16

# 2、find():检查字符串是否包含给定字符串
# 格式：str.find(sub[,start[,end]])
# 说明：Return the lowest index in the string where substring sub is found within the slice s[start:end].
#     Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.
# 参数：sub---指定检索的给定字符串
#      start---起始索引
#      end---终止索引
print(str1.find('temptation')) # 6
print(str1.find('temptation',0,len(str1 ))) # 6
print(str1.find('temptation',7,len(str1))) # -1

# 3、index():检查字符串是否包含给定字符串（功能类似find()函数，找不到时会超出异常）
# 格式：str.index(sub[,start[,end]])
# 说明：Like find（），but raise ValueError when the substring is not found
# 参数：sub---指定检索的给定字符串
#      start---起始索引
#      end---终止索引
print(str1.index('temptation')) # 6
print(str1.index('temptation',0,len(str1))) # 6
# 执行出错：ValueError: substring not found
# print(str1.index('temptation',7,len(str1))) # -1

# 4、count():统计字符串中给定字符串的个数
# 格式：str.count(sub[, start[, end]])
# 说明：Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional
#      arguments start and end are interpreted as in slice notation.
# 参数：sub---指定检索的给定字符串
#      start---起始索引
#      end---终止索引
print(str1.count('temptation')) # 1
print(str1.count('temptation',0,len(str1))) # 1
print(str1.count('temptation',7,len(str1))) # 0
print(str1.count('temptation',6,len(str1))) # 1
print(str1.count('t',0,len(str1))) # 4

# 5、replace():既有字符串的内容替换为新的字符串
# 格式：str.replace(old, new[, count])
# 说明：Return a copy of the string with all occurrences of substring old replaced by new. If the optional
#      argument count is given, only the first count occurrences are replaced.
# 参数：old---既有字符串
#      new---新的字符串
#      count---可选项，替换不超过多少次
print(str1.replace('python','java')) # javatemptation
print(str1.replace('t','123',3)) # py123hon123emp123ation

# 6、split():按指定内容对字符串进行分隔，得到一个列表，默认按英文空格或换行（使用一对三个单引号的形式或转义字符\r或者是制表符转义字符\t或者使用Tab键）
# 格式：str.split(sep=None, maxsplit=-1)
# 说明：Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most
#      maxsplit splits are done (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).
str2='a b c'
print(str2.split()) # ['a', 'b', 'c']

str2='abc'
print(str2.split()) # ['abc']

str2='''a
b
c'''
print(str2.split()) # ['a', 'b', 'c']

str2='a\rb\rc'
print(str2) # 只显示c，不显示ab
print(str2.split()) # ['a', 'b', 'c']

str2='a\tb\tc'
print(str2) # a	b c
print(str2.split()) # ['a', 'b', 'c']

str2='a b   c'
print(str2) # a b   c
print(str2.split()) # ['a', 'b', 'c']

str3='赏花赏月赏秋香'
print(str3.split('赏')) # ['', '花', '月', '秋香']
str3='唐伯虎赏花赏月赏秋香'
print(str3.split('赏')) # ['唐伯虎', '花', '月', '秋香']

#7、strip():去除字符串两侧（不包含内容）空格
str4=' python is easy '
print(str4) #  python is easy
print(str4.strip()) # python is easy
print(len(str4)) # 16
print(len(str4.strip())) # 14







