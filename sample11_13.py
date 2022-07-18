# global 关键字：用来修饰变量为全局变量
i=123
def method():
    # 下句未执行，就提示出错：Statement seems to have no effect
    # global j=456
    global j
    j=456
    print('函数内访问i：{0}'.format(i)) # 函数内访问i：123
    print('函数内访问j：{0}'.format(j)) # 函数内访问j：456
method()
print('函数外访问i：{0}'.format(i))  # 函数外访问i：123
print('函数外访问j：{0}'.format(j))  # 函数外访问j：456