
 # 循环结构：理解循环，循是按照···规律，环是重复的动作
# Python中循环只有while循环和for循环，没有do···while循环
# 问题：输出1~5
# 方法一:逐行输出
print(1)
print(2)
print(3)
print(4)
print(5)
# 开发人员为了能偷懒，分析上述的操作，得出规律：
# ①输出的行为是重复的执行
# ②重复的规律为：后一次输出的数值是前一次输出的数值+1

# while循环的语法格式：
#   while 循环条件:
#        循环体

# 针对每次的输出操作，都做如下的判断和处理：
i=1
while i<=5:
    print(i)
    i+=1

while i<=5:
    # 循环体中的处理1：输出数值变量
     print(i)
    # 循环体中的处理2:输出数值变量后，做加1的操作，为了后一次的判断（循环条件的判断）
     i+=1