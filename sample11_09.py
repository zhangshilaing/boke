# Python的函数可以没有返回值，可以有一个返回值，也可以有多个返回值

# 没有返回值的函数写法1：
def method1():
    print('这是没有返回值的函数')
method1()  # 这是没有返回值的函数

# 没有返回值的函数写法2：
def method2():
    print('这是没有返回值的函数')
    # 函数体中的return语句不接任何返回内容，也就是无返回
    return
method2() # 这是没有返回值的函数

# 没有返回值的函数写法3：
def method3():
    print('这是没有返回值的函数')
    # 函数体中的return语句返回None关键字，也是无返回
    return None
method3() # 这是没有返回值的函数