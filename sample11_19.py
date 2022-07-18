# 嵌套函数的使用
# 定义计算函数
def calc(param1,param2,oper):
    # 定义加法函数
    def add(param1,param2):
        return param1+param2

    # 定义减法函数
    def sub(param1,param2):
        return param1-param2
    if oper=='+':
        return add(param1,param2)
    elif oper=='-':
        return sub(param1,param2)
    else:
        return '不正确的输入'
print(calc(1,2,'+')) # 3
print(calc(1,2,'-')) # -1
print(calc(1,2,'*'))# 不正确的输入

# 下句未执行，就提示出错：Unresolved reference 'add'
# 下句执行出错：NameError: name 'add' is not defined
# add(1,2)


