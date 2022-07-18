# 需求：分别使用while循环和for循环打印九九乘法口诀表
# while循环的写法
i=1
j=1
while i<=9:
    while j<=i:
        print('{0}*{1}={2}'.format(i,j,i*j),end='\t')
        j+=1

    print()

    j=1
    i+=1

# for循环的写法
for i in range(1,10):
    for j in range(1,i+1):
        print('{0}*{1}={2}'.format(i,j,i*j),end='\t')

    print()

# 问题：上面的while循环的代码中的i，j对下面for循环的代码中的i，j是否有影响？
# 答：通过设置断点，可以看出在for循环中根据序列的范围的值，对变量i，j做了重新的赋值，所以，上面代码的i，j对下面代码的i，j没有影响。