# lambda表达式：本质上就是一种匿名函数，只允许包含一个表达式，不能包含复杂的操作
# 语法格式：lambda arg1[,arg2[,.....]]:<表达式>
# 语法说明：arg1[,arg2[,....]]: 参数列表
#             <表达式>：函数体（lambda体）
method1=lambda i,j:i+j

print(method1) # <function <lambda> at 0x000002967CF271F8>
print(type(method1)) # <class 'function'>
print(method1(1,2)) # 3

method2=[lambda i:i*10,lambda j:j*100]
print(method2) # [<function <lambda> at 0x000001C80A9D7438>, <function <lambda> at 0x000001C80A9D74C8>]
print(type(method2)) # <class 'list'>
print(method2[0](2),method2[1](3)) # 20 300

