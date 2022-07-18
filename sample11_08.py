# 4、可变参数：参数的数量可变
# ① *argument：元组可变参数，多个参数放入一个元组对象中
# ② **argument：字典可变参数，多个参数放入一个字典对象中
def method1(i,*j):
    print(i,j)
method1(1,2,3) # 1 (2, 3)

def method2(i,**j):
    print(i,j)
# 下句执行出错：TypeError: method2() takes 1 positional argument but 3 were given
# method2(1,2,3)
# 调用形式1：实参直接传入 键=值
method2(1,key1=123,key2=456) # 1 {'key1': 123, 'key2': 456}
# 调用形式2：实参使用字典类型的变量，需要在变量前加上**，说明字典是可变参数
dictionary={
    'key1':123,
    'key2':456
}
method2(1,**dictionary) # 1 {'key1': 123, 'key2': 456}

def method3(*i,j):
    print(i,j)
# 下句执行出错：TypeError: method3() missing 1 required keyword-only argument: 'j'
# method3(1,2,3)
# 下句未执行，就提示错误：Cannot appear past keyword arguments or *arg or **kwarg
# 下句执行出错：SyntaxError: positional argument follows keyword argument
method3(1,j=2,3)