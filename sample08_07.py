# deepcopy()函数：使用copy模块的deepcopy()函数实现深拷贝，对被复制字典的所有元素都进行复制，而不是只复制引用
import copy
dict3={1:['中国','韩国'],2:['美国','英国']}
dict4=copy.deepcopy(dict3)
print('dict4:{0}'.format(dict4)) # dict4:{1: ['中国', '韩国'], 2: ['美国', '英国']}
dict4[2].remove('英国')
print('dict4:{0}'.format(dict4)) # dict4:{1: ['中国', '韩国'], 2: ['美国']}
print('dict3:{0}'.format(dict3)) # dict3:{1: ['中国', '韩国'], 2: ['美国', '英国']}