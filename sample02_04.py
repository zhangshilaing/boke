# 数值类型间的转换（注意：不同的数值类型间转换时，可能会有数据内容的丢失）

# float类型--->int类型，使用内置函数int()
i=1.23
print(int(i)) # 1
j=1.56
print(int(j)) # 1
k=1.89
print(int(k)) # 1

# int类型--->float类型，使用内置函数float（）
num1=123
print(float(num1)) # 123.0

# int类型--->complex类型，使用内置函数complex（）
num2=456
print(complex(num2)) # (456+0j)

print(complex(789,2)) # (789+2j)

