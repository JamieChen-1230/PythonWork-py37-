# 執行檔(要放在celery目錄外)
from DirectoryStructure import tasks_1, tasks_2


res1 = tasks_1.add(40, 4)
# 這樣取值也不用在用res1.get()了
print(res1)

res2 = tasks_2.xsum([1, 2, 3, 4, 5])
print(res2)

