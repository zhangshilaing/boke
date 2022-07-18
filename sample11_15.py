# 结合嵌套函数的变量的作用域
i=123
print('函数外的变量i：{0}'.format(i))
def outer():
    j=456
    print('函数内访问i：{0}'.format(i))
    print('函数内访问j：{0}'.format(j))
    def inner():
        k=789
        print('嵌套函数内访问i：{0}'.format(i))
        print('嵌套函数内访问j：{0}'.format(j))
        print('嵌套函数内访问k：{0}'.format(k))
    inner()
    # 下句未执行，就提示出错：Unresolved reference 'k'
    print('函数内访问k：{0}'.format(k))
outer()
# 下句未执行，已经提示出错：Unresolved reference 'j'
print('嵌套函数内访问j：{0}'.format(j))
# 下句未执行，已经提示出错：Unresolved reference 'k'
print('嵌套函数内访问k：{0}'.format(k))
