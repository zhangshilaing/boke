# 需求：输入考试成绩，低于60分的显示为不及格，60分~90分（不包含90分）为及格，90分~100分的为优秀
# 思路：选择结构注意边界范围
# 写法一：
score=int(input('请输入分数：'))
if score>=0 and score<60:
    print('不及格')
elif score>=60 and score<90:
    print('及格')
elif score>=90 and score<=100:
    print('优秀')
else:
    print('输入不在合理范围内！')

# 写法二：简化链式表达式
if 0<=score<60:
    print('不及格')
elif 60<=score<90:
    print('及格')
elif 90<=score<=100:
    print('优秀')
else:
    print('输入不在合理范围内！')