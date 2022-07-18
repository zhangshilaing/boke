# 需求：计算给定数字的阶乘，比如：5！=5*4*3*2*1

n=int(input('请输入数字：'))
j=1
for i in range(1,n+1):
       j*=i
print(j)

# 需求：计算1到给定数字的阶乘和，比如：5！+4！+3！+2！+1！
n=int(input('请输入一个数字：'))
sum=0
a=1
for i in range(1,n+1):
    a*=i
    sum+=a
print('阶乘和为{0}'.format(sum))



