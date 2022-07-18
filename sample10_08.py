import pymysql

# 数据库连接信息
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'sa',
    'database': 'test',
    'port': 3306,
    'charset': 'utf8'
}

# 1、创建数据库连接对象（写法1、使用字典对象作为数据库连接对象的参数）
connection = pymysql.connect(**config)

try:
    # 2、创建游标对象
    with connection.cursor() as cursor:
        # 3、执行SQL语句操作
        # 事务中包括两个操作：操作1、新增一条记录
        sql1 = '''
        INSERT INTO student VALUES(NULL, 'admin', 99)
        '''
        result1 = cursor.execute(sql1)

        # 事务中包括两个操作：操作2、修改一条记录
        # sql2 = '''
        # UPDATE student SET studentname = 'topsec', studentage = 66 WHERE studentid = 3
        # '''
        # result2 = cursor.execute(sql2)

        # 故意把更新语句的关键字写错
        sql2 = '''
        UP student SET studentname = 'topsec', studentage = 66 WHERE studentid = 3
        '''
        result2 = cursor.execute(sql2)

        # 4、对于增删改，需要显式的提交数据库事务，如果审核通过，事务顺利提交
        connection.commit()
        print('新增操作影响的行数为：{0}条，修改操作影响的行数为：{1}条'.format(result1, result2))
except Exception:
    # 4、对于增删改，需要显式的提交数据库事务，如果审核不通过，事务进行回滚的操作
    connection.rollback()
    print('操作失败！')
finally:
    # 6、关闭数据库连接对象
    connection.close()

