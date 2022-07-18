# while循环可以结合else使用
#  while  循环条件：
#          循环体
#  else：
#       循环条件不满足时，执行语句块

# 需求：数字猜谜游戏（随机生成10以内的正整数），猜对了退出游戏，猜不对一直猜直到猜对为止
# 思路：通过查找Python文档发现随机生成的方法，找到random模块的Functions for integers
# 内置函数：random.randint(a,b)
# 函数说明：Return a random integer N such that a <= N <= b.

import random
# 通过随机函数生成结果
result=random.randint(1,10)
# 定义猜测用的变量
guess=-1
while guess!=result:
    guess=eval(input('请输入您猜测的正整数：'))
    if guess==result:
       print('恭喜您答对了！')
    elif guess>result:
        print('您猜大了。')
    elif guess<result:
        print('您猜小了。')
else:
    print('欢迎再来玩!')



