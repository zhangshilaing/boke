# 函数对象：Python中一切皆是对象，函数也是对象，函数名是对象名
def method1():
    return '这是自定义函数'
print(method1()) # 这是自定义函数
print(method1) # <function method1 at 0x000001E8FFE271F8>
print(type(method1)) # <class 'function'>

# 定义一个变量，将函数对象赋值给它，则这个变量就是一个函数对象
method2=method1
print(method2) # <function method1 at 0x000001ED210771F8>
print(type(method2)) # <class 'function'>
print(method2()) # 这是自定义函数

