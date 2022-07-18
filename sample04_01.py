# 流程控制：本质对应着解决问题的过程，顺序结构，选择结构，循环结构，是一种面向过程的思想
# 顺序结构：自上而下，顺序执行
# 选择结构：Python语法中，只有if结构，没有switch结构
# 语法结构：
# if condition1：
#     statementblock1
# elif condition2：
#     statementblock2
# else：
#     statementblock3
# 只有if条件
if 1!=2:
     print('1不等于2') # 1不等于2
# 只有if条件和else条件
if 1==2:
    print('1等于2')
else:
    print('1不等于2') # 1不等于2

# 多条件：
# 需求：通过交互，输入两个数字，比较他们的大小
i,j=eval(input('为了比较大小，输入两个数字：'))
if i>j:
    print('前者大于后者')
if i<j:
    print('前者小于后者')
else:
    print('前者等于后者')


