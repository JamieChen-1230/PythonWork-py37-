from __future__ import absolute_import, unicode_literals
from .celery import app  # 因為導入absolute_import的關係，所以要調用我們自己寫的celery.py要加 .
from celery.schedules import crontab


# 方法一： 透過裝飾器設置定時任務
@app.on_after_configure.connect  # 這代表腳本一啟動就會直接執行此函數
def setup_periodic_tasks(sender, **kwargs):
    # Calls foo('hello') every 10 seconds
    # add_periodic_task(秒數, 任務方法名.s(參數), name='定時任務名稱', expires=任務結果保存秒數)
    sender.add_periodic_task(10.0, foo.s('hello'), name='add every 10')
 
    # Calls foo('world') every 30 seconds
    sender.add_periodic_task(30.0, foo.s('world'), expires=10)
 
    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        # crontab(時, 分, 星期幾)
        crontab(hour=7, minute=30, day_of_week=1),
        foo.s('Happy Mondays!'),
    )


@app.task
def foo(arg):
    print('run function... ', arg)


