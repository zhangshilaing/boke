# 嵌套函数 结合 函数对象 结合 lambda表达式
# 定义计算函数
def calc(oper):
    if oper=='+':
        return  lambda param1,param2: param1+param2
    elif oper=='-':
        return  lambda param1,param2: param1-param2
    else:
        return lambda *param: '不正确的输入'

method_add=calc('+')
method_sub=calc('-')
method_multi=calc('*')

print(method_add) # <function calc.<locals>.<lambda> at 0x0000023792F87438>
print(method_sub) # <function calc.<locals>.<lambda> at 0x0000023792F874C8>
print(method_multi) # <function calc.<locals>.<lambda> at 0x0000023792F87558>

print(type(method_add)) # <class 'function'>
print(type(method_sub)) # <class 'function'>
print(type(method_multi)) # <class 'function'>

print(method_add(1,2)) # 3
print(method_sub(1,2)) # -1
print(method_multi(1,2)) # 不正确的输入