from pymongo import MongoClient


# 建立連結(本地MongoDB)
client = MongoClient(host='127.0.0.1', port=27017)
# test1為DB名，stu為集合名
collection = client["test1"]["stu2"]

# 插入一條數據
# ret = collection.insert_one({'name': 'pyjamie', 'age': 35})
# print(ret.inserted_id)  # 獲取_id

# 插入多條數據
# collection.insert_many([
#     {'name': 'pyjamie2', 'age': 33},
#     {'name': 'pyjamie3', 'age': 33},
#     {'name': 'pyjamie4', 'age': 33},
# ])

# 查詢一條數據(直接返回對象字典)
# ret = collection.find_one({'name': 'pyjamie'})
# print(ret)

# 查詢多條數據(返回Cursor對象，為一生成器)
# ret = collection.find({'age': 33})
# 1.透過轉成列表獲取
# print(list(ret))
# 2.透過.__next__()取值
# print(ret.__next__())
# 3.可透過for跌代生成器對象
# for i in ret:
#     print(i)

# 更新一條數據
# ※ 使用"$set"，代表局部更新(python中必須使用$set)
# collection.update_one({"name": "pyjj"}, {"$set": {"name": "pyjj", "age": 11, "height": 180}})

# 更新多條數據
# 必須使用$set
# collection.update_many({"name": "pyjj"}, {"$set": {"name": "pyjj", "age": 11, "height": 180}})

# 刪除一條數據
# collection.delete_one({'name': 'pyjamie2'})

# 刪除多條數據
# collection.delete_many({'name': "pyjj"})


# 練習：
# 插入1000文檔：
# 通過生成器推導創建數據 => ({'_id': str(i), 'name': 'py'+str(i)} for i in range(1000))
# collection.insert_many(({'_id': str(i), 'name': 'py'+str(i)} for i in range(1000)))
# 找出所有_id為100倍數的文檔
# ret = collection.find()
# for i in ret:
#    if type(i['_id']) == str:
#        if int(i['_id'])%100 == 0:
#            print(i)
