from celery import Celery
import time
import random


# 這裡兩者都是用redis實現，設置 redis://:密碼@網域
app = Celery('tasks',
             broker='redis://:851230@localhost',  # broker為中間商，用來接收和發送任務消息，以及存儲任務結果
             backend='redis://:851230@localhost')   # backend為儲存任務結果的地方


# @app.task裝飾的函數代表worker可執行的一個任務模板
@app.task
def add(x, y):
    time.sleep(random.randint(0, 5))
    print("running...", x, y)
    return x + y


@app.task
def cmd(cmd_str):
    print('run cmd', cmd_str)
