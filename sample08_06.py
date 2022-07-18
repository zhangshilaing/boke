# copy()函数：复制功能，但是是浅拷贝
# 使用copy()函数时，如果键对应的值的类型是不可变型（数值、字符串、元组、frozenset），复制出来的字典的内容发生变化时，不会影响被复制字典的内容
dict1={1:'python',2:'java',3:'php'}
print('dict1:{0}'.format(dict1)) # dict2:{1: 'python', 2: 'java', 3: 'php'}
dict2=dict1.copy()
print('dict2:{0}'.format(dict2)) # dict2:{1: 'python', 2: 'java', 3: 'php'}
# 按键移除了对应键值对
del dict2[2]
print('dict2:{0}'.format(dict2)) # dict2:{1: 'python', 3: 'php'}
print('dict1:{0}'.format(dict1)) # dict1:{1: 'python', 2: 'java', 3: 'php'}
dict2[3]='C#'
print('dict2:{0}'.format(dict2)) # dict2:{1: 'python', 3: 'C#'}
print('dict1:{0}'.format(dict1)) # dict1:{1: 'python', 2: 'java', 3: 'php'}
print('dict1的键1对应的值的内存地址：{0}'.format(id(dict1[1])))
print('dict2的键1对应的值的内存地址：{0}'.format(id(dict2[1])))
print('dict1的键2对应的值的内存地址：{0}'.format(id(dict1[2])))
print('dict2的键2对应的值的内存地址：{0}'.format(id(dict2[2])))
# 使用copy()函数时，如果键对应的值的类型是可变型（列表、非frozenset集合），复制出来的字典的内容发生变化时，会影响被复制字典的内容
dict3={1:['中国','韩国'],2:['美国','英国']}
print('dict3:{0}'.format(dict3)) # dict3:{1: ['中国', '韩国'], 2: ['美国', '英国']}
dict4=dict3.copy()
print('dict4:{0}'.format(dict4)) # dict4:{1: ['中国', '韩国'], 2: ['美国', '英国']}
dict4[2].remove('英国')
print('dict4:{0}'.format(dict4)) # dict4:{1: ['中国', '韩国'], 2: ['美国']}
print('dict3:{0}'.format(dict3)) # dict3:{1: ['中国', '韩国'], 2: ['美国']}
print('dict3的键1对应的值的内存地址：{0}'.format(id(dict3[1]))) # dict3的键1对应的值的内存地址：1364309464072
print('dict4的键1对应的值的内存地址：{0}'.format(id(dict4[1]))) # dict4的键1对应的值的内存地址：1364309464072
print('dict3的键2对应的值的内存地址：{0}'.format(id(dict3[2]))) # dict3的键2对应的值的内存地址：1364339049992
print('dict4的键2对应的值的内存地址：{0}'.format(id(dict4[2]))) # dict4的键2对应的值的内存地址：1364339049992

