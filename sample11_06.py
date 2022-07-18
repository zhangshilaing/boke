# 2、关键字参数：使用关键字参数允许函数调用时参数的顺序和函数声明时的参数顺序可以一致，也可以不一致
def method(name,age):
    print('姓名为：%s,年龄为：%d'%(name,age))

method(name='temptation',age=16) # 姓名为：temptation,年龄为：16
method(age=16,name='temptation') # 姓名为：temptation,年龄为：16

# 注意：在函数调用时，一旦其中一个参数使用了关键字参数，其后的所有参数都要使用关键字参数
# 下句未执行，已经提示出错：Cannot appear past keyword arguments or *arg or **kwarg
# 下句执行出错：SyntaxError: positional argument follows keyword argument
# method(name='temptation',16)
method('temptation',age=16) # 姓名为：temptation,年龄为：16