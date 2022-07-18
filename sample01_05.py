# print()函数的格式：
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# 参数说明：
# *objects:可变参数，可以一次输入多个参数对象，当输入多个参数时，使用英文逗号,进行分隔
# sep=' ':separation的缩写，表示使用什么符号来间隔多个参数对象，默认是一个英文空格
# end='\n':使用给定的内容作为结尾，默认是换行符\n


print('www.taobao.com')  # www.taobao.com
print('www"taobao"com')  # www"taobao"com
print("www'taobao'com")  # www'taobao'com

print('www','taobao','com')  # www taobao com

i = 1
j = 2
print(i,j)  # 1 2
print(i,j,sep='*')  # 1*2

print(i) # 1
print(j) # 2

print(i,j) # 1 2

print(i,end='------>>>>')
print(j) # 1------>>>>2

