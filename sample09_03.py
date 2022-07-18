# with...as语句结构：在as关键字后声明一个资源变量，当语句代码块执行结束之后，python解释器会自动释放资源
# with...as进行写文件操作：
with open('test.txt','a',encoding='utf-8') as file:
    # 写入的内容
    file.write('\n测试tab缩进\t测试tab缩进\t测试tab缩进')
