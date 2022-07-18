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
    # 3、执行SQL语句
    sql='SELECT * FROM student'
    cursor.execute(sql)
    # 4、对查询提供结果集
    data=cursor.fetchall()
    print('{0}\t{1}\t{2}'.format('编号','姓名','年龄'))
    for item in data:
        print('{0}\t{1}\t{2}'.format(item[0],item[1],item[2]))
# 关闭数据库连接对象
connection.close()