# Python中需要先编写函数的定义（函数的声明），才可以进行调用；反之，出错提示找不到函数

def method1():
    print('这是method1函数')
method1() # 这是method1函数

# 下句不执行时，pycharm已经提示出错：Unresolved reference 'method2'
# 下句执行出错：NameError: name 'method2' is not defined
# method2()
# def method2():
#     print('这是method2函数')


