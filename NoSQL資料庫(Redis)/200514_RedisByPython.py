from redis import Redis

# 初始化Redis對象
cache = Redis(host='127.0.0.1', port=6379, password='851230')  # 這裡用本機做測試

"""
操作方法跟redis-cli裡大同小異，參考redis-cli筆記。
"""
# --------字符串--------
# 添加
cache.set('user', 'Jamie', ex=60)  # ex為過期時間(秒)
# 獲取
print(cache.get('user'))
# 刪除
cache.delete('user')


# --------列表--------
# 左添加
cache.lpush('users', 'jj', 'jamie')
# 右添加
cache.rpush('users', '1', '2')
# 獲取
print(cache.lrange('users', 0, -1))


# --------集合--------
# 添加
cache.sadd('set_user', 'a', 'b', 'c')
# 獲取
print(cache.smembers('set_user'))


# --------hash--------
cache.hset('di_users', 'name', 'jamie')
cache.hset('di_users', 'age', 18)
print(cache.hgetall('di_users'))


# --------事務--------(重要)
# 開啟一個pip事務
pip = cache.pipeline()
# 事務內容
pip.set('qq', '123')
# 執行事務
pip.execute()


# --------發佈與訂閱--------
# 實現異步發送郵件功能
ps = cache.pubsub()  # 可以透過這個對象操作發佈與訂閱
ps.subscribe('email')  # 監聽email頻道
# 訂閱功能
while True:
    ret = ps.listen()  # 接收，返回的是一個生成器對象
    for item in ret:
        if item['type'] == 'message':  # type=message表從publish那傳來的訊息
            print(item)

# 清除所有
# cache.flushall()
