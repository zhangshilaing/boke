# 变量作用域：全局变量 和 局部变量
# 下句的变量i定义在python的代码文件中，且在函数外，这个i是全局变量
i=123
def method():
    # 函数中不作任何修饰的变量，是局部变量
    # 在函数中声明的局部变量在函数中可以被访问，但在函数外不能被访问
    j=456
    print('函数内访问：{0}'.format(i)) # 函数内访问：123
    print('函数内访问：{0}'.format(j)) # 函数内访问：456
method()
print('函数外访问i：{0}'.format(i)) # 函数外访问i：123
# 下句未执行，就提示错误：Unresolved reference 'j'
# 下句执行出错：NameError: name 'j' is not defined
# print('函数外访问j：{0}'.format(j))
