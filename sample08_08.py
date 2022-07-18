# 推导式：从一个或者是多个迭代器快速创建序列的方法，将循环和条件判断结合起来，可以避免冗长的代码
# 字典推导式：
# 语法格式：{表达式 for item in 可迭代对象 if 条件判断}
#         {键表达式：值表达式 for item in 可迭代对象 if 条件判断}
dict1={'秦皇':'嬴政','汉武':'刘彻','唐宗':'李世民'}
print(dict1) # {'秦皇': '嬴政', '汉武': '刘彻', '唐宗': '李世民'}
print({key for key in dict1}) # {'秦皇', '汉武', '唐宗'}
print({key:dict1.get(key) for key in dict1}) # {'秦皇': '嬴政', '汉武': '刘彻', '唐宗': '李世民'}

# 获取皇帝名字中多于1的姓刘的名字
print({key:dict1.get(key) for key in dict1 if dict1.get(key).count('刘')>=1}) # {'汉武': '刘彻'}