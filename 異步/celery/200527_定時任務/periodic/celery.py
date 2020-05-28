from __future__ import absolute_import, unicode_literals
from celery import Celery  # 因為導入absolute_import的關係，這裡的celery是系統檔的celery，不是我們自己寫的celery.py

# 連接Celery，並配置中間件
# 這裡broker和backend都是用redis實現，設置： redis://:密碼@網域
app = Celery('periodic',  # 應用名稱
             broker='redis://:851230@localhost',  # broker用來接收和發送任務消息
             backend='redis://:851230@localhost',  # backend為儲存任務結果的地方
             include=['periodic.tasks_1', 'periodic.tasks_2'])   # 配置目錄下的task檔

# 設定默認參數
app.conf.update(
    result_expires=3600,  # 結果最多保存一小時
)

if __name__ == '__main__':
    app.start()  # 執行Celery應用
