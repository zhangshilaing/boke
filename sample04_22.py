# pass语句：什么也不做
if 1==1:
    pass
    print('pass语句之后，且在if结构之内的语句')  # pass语句之后，且在if结构之内的语句
print('pass语句之后，且在if结构之外的语句')  # pass语句之后，且在if结构之外的语句

# break语句：跳出循环
for i in range(1,5):
    if i==3:
        break
    print(i)


# continue语句：跳出循环结构中的当前循环，执行后续的操作
for i in range(1,5):
    if i==3:
        continue
    print(i)