# 结合嵌套函数的变量的作用域，嵌套函数的局部变量使用nonlocal关键字修饰，会在该嵌套函数的上一级函数（被嵌套函数）中寻找同名的变量
# 注意：使用nonlocal关键字修饰的变量从上一级函数中寻找，如果上一级不是函数，就无法绑定了
i=123
print('函数外访问i：{0}'.format(i))
j=222
def outer():
    nonlocal j
    j=456
    print('函数内访问i：{0}'.format(i))
    print('函数内访问j：{0}'.format(j))

    def inner():
        return

    inner()
outer()