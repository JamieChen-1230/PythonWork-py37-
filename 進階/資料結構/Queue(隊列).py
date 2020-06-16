"""
Queue(隊列、佇列)：是一種概念性的抽象資料結構，具有「先進先出」的特性。
不過Python標準庫中的queue有實現三種模式：
    - 先進先出佇列l： queue.Queue(maxsize)
    - 後進先出佇列： queue.LifoQueue(maxsize)
    - 優先級別佇列： queue.PriorityQueue(maxsize)
"""

import queue

# 如果maxsize小於1就表示隊列長度無限
q = queue.Queue(3)

# 返回佇列中的元素數量
print(q.qsize())

# 判斷佇列是否為空
print(q.empty())

# 判斷佇列是否為滿的
print(q.full())

# 插入元素
# 參數：
#   - item：放入隊列中的數據元素
#   - block：
#       當隊列中元素個數達到上限繼續往裡放數據時，
#       1. 如果block=False，直接引發queue.Full異常
#       2. 如果block=True，且timeout=None，則一直等待直到有數據出隊列後可以放入數據
#       3. 如果block=True，且timeout=N，N為某一正整數時，則等待N秒，如果隊列中還沒有位置放入數據就引發queue.Full異常
#   - timeout：設置超時時間
q.put(item='a')
q.put('b')
q.put('c')
# q.put('d', block=True, timeout=3)

# 取出元素
# 參數：
#   - block：
#       當隊列中沒有數據元素繼續取數據時，
#       1. 如果block=False，直接引發queue.Empty 異常
#       2. 如果block=True，且timeout=None，則一直等待直到有數據入隊列後可以取出數據
#       3. 如果block =True，且timeout=N，N 為某一正整數時，則等待N秒，如果隊列中還沒有數據放入的話就引發queue.Empty異常
#   - timeout：設置超時時間。
print(q.get())

# 阻塞呼叫執行緒
# 直到佇列中的所有任務被處理掉，實際上意味著等到佇列為空，再執行別的操作
q.join()

print('這不會被運行，因為被阻塞了')

