# eval() 函数：将字符串当作有效表达式执行并返回执行结果
str='print(123)'
eval(str) # 123
i=1
j=2
print(eval('i+j')) # 3
