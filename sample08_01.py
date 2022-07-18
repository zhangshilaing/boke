# Dictionary(字典)：用于存储无序，键不可重复的键值对的序列
# 语法格式：{键1：值1，键2：值2，···，键n：值n}

# 创建空字典的方式1：使用一对英文大括号{}
dict1={}
print('空字典对象：{0}'.format(dict1)) # 空字典对象：{}
print('类型为：{0}'.format(type(dict1))) # 类型为：<class 'dict'>

# 创建空字典的方式2：使用dict()函数
dict1=dict()
print('空字典对象为：{0}'.format(dict1)) # 空字典对象为：{}
print('类型为：{0}'.format(type(dict1))) # 类型为：<class 'dict'>
print(len(dict1)) # 0
dict2={'秦皇':'嬴政','汉武':'刘彻'}
print('初始化字典：{0}'.format(dict2)) # 初始化字典：{'秦皇': '嬴政', '汉武': '刘彻'}

# 对字典对象的键使用keys()函数进行统计
print('字典对象的所有键为：{0}'.format(dict2.keys())) # 字典对象的所有键为：dict_keys(['秦皇', '汉武'])

# 对字典对象的值使用values()函数进行统计
print('字典对象的所有键为：{0}'.format(dict2.values())) # 字典对象的所有键为：dict_values(['嬴政', '刘彻'])

# 对字典对象的键值对使用items()函数进行统计
print('字典对象的所有键值对为：{0}'.format(dict2.items())) # 字典对象的所有键值对为：dict_items([('秦皇', '嬴政'), ('汉武', '刘彻')])

# 使用字典对象[键名]获取键对应的值的内容，使用不存在的键名获取值时，抛出异常
print(dict2['秦皇']) # 嬴政
# 下句执行出错：KeyError: '唐宗
# print(dict2['唐宗'])

# 使用字典对象的get(键名)函数获取键对应的值的内容，使用不存在的键名获取值时，不抛出异常，结果为None
print(dict2.get('秦皇')) # 嬴政
print(dict2.get('唐宗')) # None