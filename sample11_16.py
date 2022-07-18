# 结合嵌套函数的变量的作用域，不论被嵌套函数还是嵌套函数，局部变量使用 global 关键字修饰，变成全局变量
i=123
print('函数外的变量i：{0}'.format(i)) #函数外的变量i：123
def outer():
    global j
    j=456
    print('函数内访问i：{0}'.format(i)) # 函数内访问i：123
    print('函数内访问j：{0}'.format(j)) # 函数内访问j：456

    def inner():
        global k
        k=789
        print('嵌套函数内访问i：{0}'.format(i)) # 嵌套函数内访问i：123
        print('嵌套函数内访问j：{0}'.format(j)) # 嵌套函数内访问j：456
        print('嵌套函数内访问k：{0}'.format(k)) # 嵌套函数内访问k：789
    inner()
    print('函数内访问k：{0}'.format(k)) # 函数内访问k：789

outer()
print('嵌套函数内访问j：{0}'.format(j)) # 嵌套函数内访问j：456
print('嵌套函数内访问k：{0}'.format(k)) # 嵌套函数内访问k：789