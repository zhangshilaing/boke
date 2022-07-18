# readlines()函数：会以行为单位，返回一个列表，一行内容形成列表中的一个元素
# 特点：不会对转义字符进行转义处理，但是会把转义字符读取出来
with open('test.txt','r',encoding='utf-8') as file:
    print(file.readlines()) # ['你好，Python你好，Python\n', '测试tab缩进\t测试tab缩进\t测试tab缩进']
