# 函数有多个返回值的写法1：
def method1(param1,param2):
    return (param1*2,param2*3)
print(method1(5,6)) # (10, 18)

# 借助元组的拆包操作（系列赋值）
i,j=method1(5,6)
print(i,j)  # 10 18

# 函数有多个返回值的写法2：将多个返回值放入一个元组中进行返回（逗号形式）
def method2(param1,param2):
    return param1*2,param2*3

# 系列赋值
result1,result2=method2(7,8)
print(result1,result2)  # 14 24
