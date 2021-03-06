# 需求：存折中现有1000块钱，银行的年利息为3.5%，问在银行里放多少年后，连本带利可以翻倍？

# 思路：将连本带利转换为相应的代码表达式

# 定义存折的金额
cash = 1000
# 目标金额
total = cash * 2
# 定义年数
year = 0

while cash < total:
# 注意：如果循环判断条件写成下句，会造成循环条件判断的错误，但是会在cash值为1.7631392740683778e+308时停止执行（因为数值达到了上限）
# while cash < cash * 2:
    # print(cash)
    cash *= (1 + 0.035)
    year += 1

print('在银行里放 {0} 年后，连本带利可以翻倍'.format(year))  # 在银行里放 21 年后，连本带利可以翻倍