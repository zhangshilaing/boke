import pymysql
# 数据库的连接信息
config={
    'host':'localhost',
    'user':'root',
    'password':'sa',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}
# 1、创建数据库的连接对象
connection=pymysql.connect(**config)
# 2、创建游标对象
with connection.cursor() as cursor:
    # 3、执行SQL语句操作
    sql='''
    CREATE TABLE student
    (
        studentid INT AUTO_INCREMENT PRIMARY KEY,
        studentname VARCHAR(10) NOT NULL,
        studentage INT NOT NULL

    )
        '''
    cursor.execute(sql)
    # 4、对于查询提供结果集
    print('创建表成功！')
# 6、关闭数据库连接对象
connection.close()