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
        sql = '''
        UPDATE student SET studentage = %d WHERE studentid = %d
        '''
        result = cursor.execute(sql % (16, 2))

        # 4、对于增删改，需要显式的提交数据库事务，如果审核通过，事务顺利提交
        connection.commit()
        print('影响的行数为：{0}条'.format(result))
except Exception:
    # 4、对于增删改，需要显式的提交数据库事务，如果审核不通过，事务进行回滚的操作
    connection.rollback()
    print('修改操作失败！')
finally:
    # 6、关闭数据库连接对象
    connection.close()