# zip()函数：压缩函数，结合dict()字典构造函数将两个列表的可迭代对象压缩成一个字典对象
# 两个具有相同元素个数的可迭代对象
temp=zip(['安徽','江苏','浙江'],['合肥','南京','杭州'])
print(temp) # <zip object at 0x000001FD1ECBC8C8>
print(type(temp)) # <class 'zip'>
dict1=dict(temp)
print(dict1) # {'安徽': '合肥', '江苏': '南京', '浙江': '杭州'}
# 两个具有不同元素个数的可迭代对象,按照相同索引进行压缩
temp2=zip(['安徽','江苏','浙江'],['合肥','南京','杭州','苏州'])
dict2=dict(temp2)
print(dict2) # {'安徽': '合肥', '江苏': '南京', '浙江': '杭州'}