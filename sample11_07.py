# 3、默认参数：调用参数时，如果相应的形式参数，没有传入实参，则该形式参数有默认参数的就使用默认参数的值，
#             如果相应的形式参数，传入了实参，则该形式参数使用传入的实参的值
def method(name,age=16):
    print('姓名为：%s，年龄为：%d'%(name,age))

method('temptation') # 姓名为：temptation，年龄为：16
method('temptation',99) # 姓名为：temptation，年龄为：99


