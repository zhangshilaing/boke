# 使用列表推导式进行读取（考虑到有序性 和 可重复性）
print([item.strip() for item in open('test.txt', 'r', encoding='utf-8')])
# ['你好，Java你好，Python', '测试tab缩进\t测试tab缩进\t测试tab缩进']
