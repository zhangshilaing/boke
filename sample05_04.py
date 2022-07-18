#  列表是一种序列，所以可以使用for循环形式进行遍历
list1=['安徽','合肥','铜陵','淮南']

# 使用for···in 进行遍历
for item in list1:
    print(item)
#结果为：　安徽
#      　 合肥
#　　　　　铜陵
#         淮南

# 使用for循环结合enumerate()函数进行遍历，得到索引值和元素值
for i,item in enumerate(list1):
    print('索引值：{0}，元素值：{1}'.format(i,item))
# 结果为：索引值：0，元素值：安徽
#        索引值：1，元素值：合肥
#        索引值：2，元素值：铜陵
#        索引值：3，元素值：淮南

