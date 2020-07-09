import MySQLdb
import configparser

config = configparser.ConfigParser()
config.read('Config.ini')
user = config.get('mysql_root', 'user')
pwd = config.get('mysql_root', 'pwd')


# connect()方法用於建立資料庫的連線，裡面可以指定引數：使用者名稱，密碼，主機等資訊。
conn = MySQLdb.connect(host='localhost', port=3306, user=user, passwd=pwd, db='test', charset='utf8')
# 這只是連線到了資料庫，要想操作資料庫需要建立遊標。
cursor = conn.cursor()

# =======-insert-=======
# cursor.execute("insert into student values(9, 'Jamie', '1990-01-01', '男')")
# 插入一條資料
# sqli="insert into student values(%s,%s,%s,%s)"
# cursor.execute(sqli,(10,'Huhu','1990-01-01','男'))
# 一次插入多條記錄
# sqli="insert into student values(%s,%s,%s,%s)"
# cursor.executemany(sqli, (
#     (13,'Huhu4','1990-01-01','男'),
#     (14,'Huhu5','1990-01-01','男'),))
# conn.commit() # 新增或修改資料必須提交才能生效


# =======-update-=======
# cursor.execute("update student set s_sex='female' where s_name = 'Huhu3'")
# conn.commit() # 新增或修改資料必須提交才能生效


# =======-delete-=======
# cursor.execute("delete from student where s_name='jamie'")
# conn.commit() # 新增或修改資料必須提交才能生效


# =======-select-=======
cursor.execute('select * from student')  # 不會返回任何對象，想要拿到數據可以通過cursor.方法名
one_result = cursor.fetchone()  # 查詢結果集的下一條數據
many_result = cursor.fetchmany(5)  # 查詢結果集的下五條數據
all_result = cursor.fetchall()  # 查詢結果集的剩余所有數據

print(one_result)
print('*' * 100)
print(many_result)
print('*' * 100)
print(all_result)


# 關閉遊標
cursor.close()
# 關閉資料庫連線
conn.close()