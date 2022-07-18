# 需求：使用readline()函数读取多行内容
with open('test.txt', 'r', encoding='utf-8') as file:
    # print(file.readline())
    # print(file.readline())
    # 上述两行语句的写法，明显让我们考虑到不可能先去数文件中有多少行，然后来写多少个readline()语句，肯定会想到使用循环

    # 如下写法会显示出偶数行的内容，因为在while循环的判断时就读取了一行
    # while file.readline() != '':
    #     print(file.readline())

    # 思路：把读取的内容先存在一个变量中，循环时对这个变量进行判断，相当于手动实现do...while循环的效果
    # line = file.readline()
    #
    # while line != '':
    #     print(line)
    #     line = file.readline()

    # 上述写法可以把文件中的内容都读取出来，但是行与行之间有一个空行
    # 这是因为print()函数默认会换行，文本内容读取时又带有换行，所以出现了两次换行
    # 使用字符串的strip()函数对字符串首尾的换行符进行处理
    # str.strip([chars])
    # Return a copy of the string with the leading and trailing characters removed.
    line = file.readline()

    while line != '':
        print(line.strip())
        line = file.readline()

        # 你好，Java你好，Python
        # 测试tab缩进	测试tab缩进	测试tab缩进