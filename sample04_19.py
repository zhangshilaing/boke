# 对比一个while循环和for循环的区别

# while循环
# 循环变量=初始值
# while 循环条件：
#　　　　循环体
#      循环变量的变化

# for循环
# for 循环变量 in 序列：
#　　　　循环体

# for循环相比while循环比较简化，但是for循环需要指定序列的范围，while循环的循环条件可以是多种多样的布尔结果的表达式：

# while循环的写法
i=1
while i<=5:
    print(i)
    i+=1

# for循环的写法
for i in range(1,6):
    print(i)