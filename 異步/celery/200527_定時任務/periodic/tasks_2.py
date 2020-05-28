from __future__ import absolute_import, unicode_literals
from .celery import app  # 因為導入absolute_import的關係，所以要調用我們自己寫的celery.py要加 .
from celery.schedules import crontab


@app.task
def add(x, y):
    print('run add function... ', x+y)
    return x+y


@app.task
def hello(name):
    print('run hello function...  hello~ ', name)
    return name


# 方法二：用配置文件格式配置定時任務
app.conf.beat_schedule = {
    'add-every-10-seconds': {   # 任務名稱
        'task': 'periodic.tasks_2.add',  # 添加任務(要從celery目錄開始寫)
        'schedule': 10.0,  # 每隔幾秒執行
        'args': (40, 4),  # 參數
    },
    'hello-every-5-seconds': {
        'task': 'periodic.tasks_2.hello',
        'schedule': 5.0,
        'args': ('jamie', ),
    },
    # 每周四早上10:24運行
    'hello-every-morning': {
        'task': 'periodic.tasks_2.hello',
        'schedule': crontab(hour=10, minute=24, day_of_week=4),
        'args': ('hello-every-monday-morning', ),
    },
}
app.conf.timezone = 'Asia/Shanghai'  # 時區設在上海

