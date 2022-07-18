# readline()函数：读取一行，默认是第一行
# 特点：读取一行内容，并且执行转义字符的转义处理
with open('test.txt','r',encoding='utf-8') as file:
    print(file.readline()) #你好，Python你好，Python
