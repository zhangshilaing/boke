# 字符串的常用输出形式
from string import Template

# 1、%：格式化字符串
#    常用形式：%d格式化整型数据；%s格式化字符串内容
print('%s真牛逼！'%'中国') # 中国真牛逼！
print('热烈祝贺%s成立%d周年！'%('中华人民共和国',71)) # 热烈祝贺中华人民共和国成立71周年！


# 2、format()函数：使用格式化函数
print('{0}真牛逼！'.format('中国')) # 中国真牛逼！
print('热烈祝贺{0}成立{1}周年！'.format('中华人民共和国',71)) # 热烈祝贺中华人民共和国成立71周年！
print('热烈祝贺{1}成立{0}周年！'.format(71,'中华人民共和国')) # 热烈祝贺中华人民共和国成立71周年！
print('热烈祝贺{country}成立{year}周年！'.format(country='中华人民共和国',year=71)) # 热烈祝贺中华人民共和国成立71周年！

# 3、字符串模板：
# 执行出错：ValueError: Invalid placeholder in string: line 1, col 1
# print(Template('$0真牛逼！').substitute('中国'))
print(Template('$country真牛逼！').substitute(country='中国')) # 中国真牛逼！
print(Template('热烈祝贺$country成立$year周年！').substitute(country='中华人民共和国',year=71)) # 热烈祝贺中华人民共和国成立71周年！
