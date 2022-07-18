# 系列赋值（赋值号的右侧一系列的数据内容以英文的逗号分隔开，对应赋值给赋值号的左侧一系列的变量，这些变量也以英文的逗号分隔开）
a , b = 1,2
print('a为：',a)
print('b为：',b)

#执行出错：TypeError: cannot unpack non-iterable int object
# c , d=3
# print('c为：',c)
# print('d为：',d)

#执行出错：ValueError: too many values to unpack (expected 2)
c , d = 3, 4, 5
print('c为：',c)
print('d为：',d)
