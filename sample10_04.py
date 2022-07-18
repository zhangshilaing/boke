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
try:
    # 2、创建游标对象
    with connection.cursor() as cursor:
        # 3、执行SQL语句操作
        sql='''
         INSERT INTO student VALUES(NULL,'test',18)
        '''
        result=cursor.execute(sql)
        # 对于增删改，需要显示提交数据库事务，如果审核通过，事务顺利提交
        connection.commit()
        print('影响的条数：{0}'.format(result))

except Exception:
    # 对于增删改，需要显示的数据库事务，如果审核不通过，事务进行回滚的操作
    connection.rollback()
    print('新增操作失败！')
finally:
    connection.close()
