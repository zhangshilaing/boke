# 需求：分组问题
# 根据输入的每组人数对人员进行随机分配，不足每组设定人数的人员最后单独成组
# 比如：张三、李四、王五、赵六、钱七，可以交互输入设定每组有3人，那么就分成两组，每组的人是随机的，也可以通过交互输入设定每组有2人，
#      那么就分成三组，每组的人是随机的。
# 思路：1、根据交互输入设定每组的人数，可以计算出不足每组设定人数的人员个数（如果有不足时）和组数。
#      2、通过随机从人员列表中取出若干数量的人员进行分组。
#      3、进行分组时，去除的人员要从列表中移除，避免后续操作时出现重复。
import math,random
persons=['张三','李四','王五','赵六','钱七']
print('初始化人员信息为{0}'.format(persons))
# 1、根据交互输入设定每组的人数，可以计算出不足每组设定人数的人员个数（如果有不足时）和组数。
#  获得设定的每组人员的数量
number=int(input('请输入每组的人数：'))
#  不足每组设定人数的人员个数
remainder=len(persons)%number
#  组数：可以使用if...else的选择结构，也可以使用选择结构的三元运算形式,也可使用math模块的ceil函数做向上取整
# teams=((len(persons)//number) if len(persons)%number==0 else len(persons)//number+1)
teams=math.ceil(len(persons)/number)
print('一共分为{0}组'.format(teams))
for i in range(1,teams+1):
# 2、通过随机从人员列表中取出若干数量的人员进行分组。
# 通过查看Python文档，发现random模块的Functions for sequences(针对序列的一系列方法)
# random.sample(population,k):返回一个k长度的由唯一元素组成的序列集合
# Return a k length list of unique elements chosen from the population sequence or set.
    temp=[]
    if i==1 and remainder>0:
        temp=random.sample(persons,remainder)
    else:
        temp=random.sample(persons,number)
    print('组员为{0}'.format(temp))
# 3、进行分组时，去除的人员要从列表中移除，避免后续操作时出现重复。
    [persons.remove(item) for item in temp]