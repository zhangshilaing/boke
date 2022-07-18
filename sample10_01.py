# 日常工作中常用的开源关系型数据库MySQL/MariaDB
# 1、安装MariaDB时的注意事项：
# ①默认的用户为root，设置的密码为sa
# ②勾选UTF8编码作为默认的数据库字符集
# ③服务默认名称为MySQL
# ④默认使用的TCP端口为3306

# 2、使用MariaDB：
# 在命令行串口中输入：mysql -uroot -psa，看见"Welcome"字样，进入MariaDB

# 3、常用的SQL命令
# ①show databases; 查看所有的数据库的信息（默认有四个库，test库供使用者使用，其他三个）
# ②use test;  指明使用test数据库
# ③show tables;  查看库中的所有表的信息
# ④create database 库名; 创建XXX数据库
# ⑤drop database 库名; 删除XXX数据库
# ⑥create table 表名 (字段名1 数据类型 约束，字段名2 数据类型 约束，……，字段名n 数据类型 约束); 创建yyy数据表
# ⑥例如：create table student(studentid int auto_increment primary key, --学生学号，约束为自增且为主键
#                            studentname varchar(10) not null, --学生姓名，字符串型，长度为10，约束为非空
#                            age int not null --年龄，整型，约束为非空
#                             );
# ⑦desc 表名;  查看表的结构
# ⑧drop table 表名;  删除yyy表
# ⑨exit  退出


# Python 操作数据库需要使用第三方模块PyMySQL,通过pip install PyMySQL进行安装
# Python 数据库编程的步骤：
# 1、创建数据库的连接对象
# 2、创建游标对象
# 3、执行SQL语句操作
# 4、对于查询，提供结果集；对于增删改，提交数据库事务或回滚数据库事务
# 5、关闭游标对象
# 6、关闭数据库连接对象

import pymysql
# 数据库的连接信息
# config={
#     'host':'localhost',
#     'user':'root',
#     'password':'sa',
#     'database':'test',
#     'port':3306,
#     'charset':'utf8'
# }

# 1、创建数据库的连接对象（写法1：使用字典对象作为数据库连接对象的参数）
# connection=pymysql.connect(**config)
# 1、创建数据库的连接对象（写法2：使用元组对象作为数据库连接对象的参数）
connection=pymysql.connect(host='localhost',user='root',password='sa',database='test',port=3306,charset='utf8')
# 2、创建游标对象
with connection.cursor() as cursor:
     # 3、执行SQL语句操作
     sql='SELECT VERSION()'
     cursor.execute(sql)
     # 4、对于查询，提供结果集；对于增删改，提交数据库事务或回滚数据库事务
     data=cursor.fetchone()
     print('数据库版本信息为：{0}'.format(data))
     # 6、关闭数据库连接对象
     connection.close()


