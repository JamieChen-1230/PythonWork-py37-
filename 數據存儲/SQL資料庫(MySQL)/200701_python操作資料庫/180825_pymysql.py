import pymysql

# # 添加數據
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='python')  # 建立接口
# # cursor = conn.cursor()  # 建立游標
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 建立字典形式游標

# # sql = 'create table test(id int primary key auto_increment, name varchar(20))'
# # cursor.execute(sql)  # 執行命令
# # cursor.execute("insert into test(name) values ('jamie')")

# ret = cursor.execute('select * from test')
# # 查詢數據
# # print(cursor.fetchone())  # 取一條
# # print(cursor.fetchmany(2))  # 取二條
# # cursor.scroll(-1, mode='relative')  # 以光標當前位置向上移動一格
# # cursor.scroll(0, mode='absolute')  # 把光標直接調到0(最頂端)
# # print(cursor.fetchall())  # 取全部


# conn.commit()  # 提交到資料庫
# cursor.close()
# conn.close()


# pymysql實現事務
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s2')
try:
    cursor = conn.cursor()

    sql1 = "update account2 set deposit=deposit-5000 where name='jamie'"
    sql2 = "update account2 set deposit=deposit+5000 where name='sb'"

    cursor.execute(sql1)
    raise Exception
    cursor.execute(sql2)

    cursor.close()
    conn.commit()
except Exception:
    conn.rollback()
    conn.commit()
