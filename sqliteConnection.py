# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# 导入SQLite驱动
import sqlite3, os

# 连接到SQLite数据库
# 数据库文件是lhrtest.db
# 如果文件不存在，那么会自动在当前目录创建一个数据库文件:
conn = sqlite3.connect('lhrtest.db')

# db_file = os.path.join(os.path.dirname(__file__), 'lhrtest.db')
# if os.path.isfile(db_file):
#     os.remove(db_file)
# conn = sqlite3.connect(db_file)

# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
# cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
# 继续执行一条SQL语句，插入一条记录:
cursor.execute('insert into user (id, name) values (\'2\', \'夏凡\')')
# 通过rowcount获得插入的行数:
print(cursor.rowcount)
# 执行查询语句:
cursor.execute('select * from user where id=?', ('2'))
# 获得查询结果集:
values = cursor.fetchall()
print(values)
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()
def test(name):
    print(name)
