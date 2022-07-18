# 嵌套函数 结合 函数对象 使用
def calc(oper):
    # 定义加法函数
    def add(param1,param2):
        return param1+param2
    # 定义减法函数
    def sub(param1,param2):
        return param1-param2
    # 定义错误函数
    def error(*param):
        return '不正确的输入'
    if oper=='+':
        # 返回对嵌套函数对象的调用
        return add
    elif oper=='-':
        # 返回对嵌套函数对象的调用
        return sub
    else:
        # 返回对嵌套函数对象的调用
        return error


method_add=calc('+')
method_sub=calc('-')
method_multi=calc('*')


print(method_add) # <function calc.<locals>.add at 0x00000281211D7438
print(method_sub) # <function calc.<locals>.sub at 0x00000281211D74C8>
print(method_multi) # <function calc.<locals>.error at 0x00000281211D7678>

print(type(method_add)) # <class 'function'>
print(type(method_sub)) # <class 'function'>
print(type(method_multi)) # <class 'function'>

# 既然是函数对象，就可以接收参数，带上小括号，就是对函数对象指向的函数体的调用
print(method_add(1,2)) # 3
print(method_sub(1,2)) # -1
print(method_multi(1,2)) # 不正确的输入