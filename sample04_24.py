# 需求：商店里的篮球，原价为78元，现在为了促销，推出买5个送一个的活动，老王需要35个球，问他需要花多少钱？
# 单价
price=78
# 购买的篮球数
number=1
# 赠送的球数
extend_number=0
# 需要的篮球数
total_number=35
# 写法一：使用while循环结合break语句
while True:
    # 买五送一，赠送的数量加在赠送的篮球数的变量上
     if number%5==0:
         extend_number+=1

    # 购买的篮球数+赠送的篮球数=需要的篮球数时，跳出死循环
     if number+extend_number>=total_number:
         break

     number+=1

print('老王需要35个球，需要花费{0}元'.format(number*price)) # 老王需要35个球，需要花费2340元


# 写法二：使用while循环
flag=True
while flag:
    if number%5==0:
        extend_number+=1
    if number+extend_number>=total_number:
        flag=False
    if flag:
        number+=1
print('老王需要35个球，需要花费{0}元'.format(number*price))  # 老王需要35个球，需要花费2340元


# 写法三：使用for循环
for number in range(1,36):
    if number%5 == 0:
        extend_number+=1
    if number+extend_number>=total_number:
        break

print('老王需要35个球，需要花费{0}元'.format(number*price))




