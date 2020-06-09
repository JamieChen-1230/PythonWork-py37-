"""
現有2個進程A和B，他們都在內存中開闢了空間，那麼我們在內存中再開闢一個空間C，作用是連接這兩個進程的
對於進程來說內存空間是可以共享的（任何一個進程都可以使用內存，內存當中的空間是用地址來標記的，我們通過查找某一個地址就能找到這個內存）
A進程可以不斷的向C空間輸送東西，B進程可以不斷的從C空間讀取東西，這就是進程間的通信 
"""

from multiprocessing import Pipe, Process
import os, time, random


# 進程函數
def func(num, child_conn):
    time.sleep(random.randint(1, 4))
    child_conn.send(['第%d個子進程send' % num])
    print('第%d個子進程運行結束，id為:' % num, os.getpid())


# 創建五個進程
if __name__ == '__main__':
    # 創建管道對象，會返回兩個對象
    child_conn, parent_conn = Pipe()
    job = []
    for i in range(5):
        # target為子進程要運行的函數；args為參數
        p = Process(target=func, args=(i+1, child_conn))
        # 把新的進程添加到列表裡
        # 新添加的都是子進程，父進程為此py檔的運行
        job.append(p)
        p.start()
    for i in range(5):
        # 接收從child_conn.send()的資料
        # 因為總共send了五次，所以要recv五次
        # ※ recv是一個阻塞函數(當管道為空的時候就會阻塞)
        data = parent_conn.recv()
        print(data)
    for i in job:
        # process對象.join()  => 阻塞當前進程，直到調用join方法的那個進程執行完，再繼續執行當前進程。
        i.join()
    # 若沒加.join()方法，主進程有可能會比其他子進程早結束
    print('主進程執行結束')


"""
總結：
    1. 向管道發送數據使用send函數，從管道接收數據使用recv()函數
    2. recv()函數為阻塞函數，當管道中數據為空的時候會阻塞
    3. 一次recv()只能接收一次send()的內容
    4. send可以發送的數據類型比較多樣，字符串、數字、列表等等
"""
