# 函数：由一组语句组成实现某个功能的结构，是代码复用的体现
# python中的函数分为：
# 1、内置函数
# 2、标准库函数（通过import语句导入模块后，在进行使用）
# 3、第三方库函数（通过pip install 下载并安装第三方库之后，再通过import语句导入模块后，在进行使用）
# 4、自定义函数（开发人员自己编写的函数）

# 函数的格式：
# def 函数名称（参数列表）
#    '''文档字符串'''(函数的注释说明)
#     函数体
#     return [表达式]

# 需求：编写一个自定义函数，实现比较两个数值内容的大小，输出较大的一个数值
def showMax(i,j): # 参数列表中定义的变量，占据参数位置，并在函数体中被使用，称为形式参数，简称形参
    if i>j:
        print('较大的值为：{0}'.format(i))
    else:
        print('较大的值为：{0}'.format(j))
# 对自定义的函数进行调用，使之被执行
showMax(2,3)  # 函数调用时，实际传递给函数的数据，成为实际参数，简称实参
showMax(789,159)

# help()函数可以对文档字符串进行查看，注意给help函数传入的是函数名称，不带英文小括号
help(showMax)

# 可以使用help()函数查看内置函数的注释说明
help(print)
#
# Help on built-in function print in module builtins:
#
# print(...)
#     print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
#
#     Prints the values to a stream, or to sys.stdout by default.
#     Optional keyword arguments:
#     file:  a file-like object (stream); defaults to the current sys.stdout.
#     sep:   string inserted between values, default a space.
#     end:   string appended after the last value, default a newline.
#     flush: whether to forcibly flush the stream.
