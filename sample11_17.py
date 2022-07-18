# 结合嵌套函数的变量的作用域，嵌套函数的局部变量使用nonlocal关键字修饰，会在该嵌套函数的上一级函数（被嵌套函数）寻找同名的变量，
#   如果找到则绑定之
i=123
print('函数外的变量i：{0}'.format(i)) # 函数外的变量i：123
def outer():
    j=456
    print('函数内访问i：{0}'.format(i)) # 函数内访问i：123
    print('函数内访问j：{0}'.format(j)) # 函数内访问j：456

    k=666
    def inner():
        nonlocal k
        k=789
        print('嵌套函数内访问i：{0}'.format(i)) # 嵌套函数内访问i：123
        print('嵌套函数内访问j：{0}'.format(j)) # 嵌套函数内访问j：456
        print('嵌套函数内访问k：{0}'.format(k)) # 嵌套函数内访问k：789
    inner()
    print('函数内访问k：{0}'.format(k))
    # 如果把12行注释掉，则执行结果为：函数内访问k：666
    # 如果把12行不注释掉，则执行结果为：函数内访问k：789

outer()

