from __future__ import absolute_import, unicode_literals
from .celery import app  # 因為導入absolute_import的關係，所以要調用我們自己寫的celery.py要加 .


# 被@app.task裝飾的函數代表是一個worker可執行的任務模板
@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y

