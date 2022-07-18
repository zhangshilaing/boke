# 读文件操作
# 步骤1：以指定模式和指定编码打开文件，得到文件对象
file=open('test.txt','r',encoding='utf-8')
# 步骤2：使用read()函数从文件中读取内容
print(file.read())
# 步骤3：使用完毕后，关闭资源（文件对象）
file.close()