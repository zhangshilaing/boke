# 需求：百钱百鸡问题：母鸡一只5元，公鸡一只3元，小鸡三只1元，现有100元，如何买到100只鸡？
# 母鸡多少只？公鸡多少只？小鸡多少只？（母鸡公鸡小鸡均有）
# 思路：从需求中得到一系列的规则
#   母鸡数量+公鸡数量+小鸡数量=100
#   母鸡单价*母鸡数量+公鸡单价*公鸡数量+小鸡单价*小鸡数量=100
#   小计数量是3的倍数
#   母鸡数量>0，公鸡数量>0，小鸡数量>0
#   得到规则后，考虑运用穷举的思想，一种情况一种情况去尝试
#   买1只母鸡，再买1只公鸡，还可以买多少只小鸡凑齐100元？
#   买1只母鸡，再买2只公鸡，还可以买多少只小鸡凑齐100元？
#   买1只母鸡，再买3只公鸡，还可以买多少只小鸡凑齐100元？
#   ····
#   买2只母鸡，再买1只公鸡，还可以买多少只小鸡凑齐100元？
#   买2只母鸡，再买2只公鸡，还可以买多少只小鸡凑齐100元？
#   ····

# 母鸡数量
i=1
# 公鸡数量
j=1
# 小鸡数量
k=1
print('计算百钱百鸡问题：')

while i<100:
    while j<100:
        k=100-i-j
        if (5*i+3*j+k/3==100)and(k%3==0)and(i>0)and(j>0)and(k>0):
            print('母鸡{0}只，公鸡{1}只，小鸡{2}只'.format(i,j,k))
        j+=1

    # 内置循环变量需要重置
    j=1
    i+=1


# 下句可以进行改进：
while i<20:
    while j<33:
        k=100-i-j
        if(5*i+3*j+k/3==100)and(k%3==0):
            print('母鸡{0}只，公鸡{1}只，小鸡{2}'.format(i,j,k))
        j+=1

    j=1
    i+=1