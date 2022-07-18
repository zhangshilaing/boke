# 使用with...as 进行读文件操作
with open('test.txt','r',encoding='utf-8') as file:
    # 使用read()函数进行内容的读取
    print(file.read())
