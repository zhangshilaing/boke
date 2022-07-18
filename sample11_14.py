# 嵌套函数：在函数的内部再定义函数
def method1():
    print('method1函数被调用')
    def method2():
        print('method2函数被调用')
    # 在被嵌套的函数中编写对嵌套函数的调用
    method2() # method2函数被调用
method1() # method1函数被调用

