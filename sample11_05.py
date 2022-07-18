# Python函数的参数多种多样，比较灵活
# 1、位置函数：调用函数时，默认必须以正确的顺序传入参数，调用时传入的参数数量必须和函数声明时定义的数量一致
def method(name,age):
    print('姓名为：%s，年龄为：%d'%(name,age))
method('temptation',15) # 姓名为：temptation，年龄为：15

# 下句执行出错：TypeError: %d format: a number is required, not str
# method(16,'temptation')

# 下句执行出错：TypeError: method() takes 2 positional arguments but 3 were given
# method('temptation',15,'male')

# 下句执行出错：TypeError: method() missing 1 required positional argument: 'age'
method('temptation')