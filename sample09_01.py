# 数据的持久化涉及到输入（Input）和输出（Output），具体来说，就是文件的读写操作
# 写文件操作
# 步骤1：以指定模式和指定编码打开文件，得到文件对象
# 模式设置为：'w',写入的内容会覆盖文件中原有的内容
# file=open('test.txt','w',encoding='utf-8')
# 模式设置为：'a',写入的内容会追加文件中在原有内容的尾部
file=open('test.txt','a',encoding='utf-8')
# 步骤2：使用write()函数向文件中写入内容
file.write('你好，Python')
# 步骤3：使用完毕后，关闭资源（文件对象）
file.close()