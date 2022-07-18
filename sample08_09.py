# 需求：制作内存版的通讯录，实现输入数字可以选择相应的功能，功能有：
#      输入1，可以查看所有人员的信息
#      输入2，可以查看指定人员的信息
#      输入3，可以增加人员的信息
#      输入4，可以修改人员的信息
#      输入5，可以删除人员的信息
#      输入6，可以退出
print('-----欢迎进入通讯录程序-----')
print('-输入1：可以查看所有人员信息-')
print('-输入2：可以查看指定人员信息-')
print('---输入3：可以增加人员信息---')
print('---输入4：可以修改人员信息---')
print('---输入5：可以删除人员信息---')
print('-------输入6：可以退出-------')
dict1={'张三':['联系电话：1234','籍贯：安徽'],
       '李四':['联系电话：4567','籍贯：江苏'],
       '王五':['联系电话：7894','籍贯：北京'],
       '赵六':['联系电话：1472','籍贯：浙江']}
while(1):
     n=int(input('请输入相关指令代码：'))
     if n==1:
        print('通讯录的所有人员信息为：{0}'.format(dict1))
        print('')
     elif n==2:
        key=input('请输入人员的名字：')
        print(dict1.get(key))
        print('')
     elif n==3:
        key=input('请输入您想添加的人员姓名：')
        if (key in dict1):
            print('您输入的姓名在通讯录中：{0}'.format(dict1.get(key)))
        else:
            value1=input('请输入用户联系电话：')
            value2=input('请输入用户籍贯：')
            dict1[key]=[value1,value2]
        print('')
     elif n==4:
        key=input('请输入想要修改的人员姓名：')
        value3=input('请输入想要修改的联系电话：')
        dict1[key]=value3
        print('')
     elif n==5:
        key=input('请输入想要删除的人员姓名：')
        del dict1[key]
        print('')
     elif n==6:
         print('----感谢使用通信录程序----')
         print('')
         break



