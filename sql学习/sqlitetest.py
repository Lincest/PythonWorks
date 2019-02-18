import sqlite3


"""
要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；

连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果
"""
# 若文件不存在则在当前目录创建
conn = sqlite3.connect('db_file.db')
# 创建一个cursor
cursor = conn.cursor()
# 执行sql语句，创建user表（varchar为可变长字符串）
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
# 关闭cursor，connection，并提交事务
cursor.close()
conn.commit()
conn.close()

# 进行分数的查询并从小到大以list形式传出name
def get_score_in(low,high):
    conn = sqlite3.connect('db_file.db')
    cursor = conn.cursor()
    val=[]
    for i in range(low,high+1):
        cursor.execute("select name from user where score=?",(i,))
        try:
            val += (cursor.fetchall())[0]
        except:
            pass
    conn.close()
    return val

# 测试
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('pass')