# 使用for循环对文件对象进行遍历
# with open('test.txt', 'r', encoding='utf-8') as file:
#     for item in file:
#         print(item)
# 你好，Java你好，Python
#
# 测试tab缩进	测试tab缩进	测试tab缩进

with open('test.txt', 'r', encoding='utf-8') as file:
    for item in file:
        print(item.strip())
# 你好，Java你好，Python
# 测试tab缩进	测试tab缩进	测试tab缩进
