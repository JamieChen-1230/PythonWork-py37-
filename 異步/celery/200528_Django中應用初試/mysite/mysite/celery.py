from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# 在默認Django settings中定義Celery程序
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
# 創建Celery應用
app = Celery('celery_task')


# 在django配置文件中配置Celery
# namespace='CELERY' 表示之後要在配置文件中設定Celery相關參數時要使用「CELERY」關鍵字
# 所以之後還需要到settings.py中配置broker和backend等
app.config_from_object('django.conf:settings', namespace='CELERY')

# 配置好設定後，可以讓Django自動去找各個Django應用下的tasks.py(不管放在哪個app下都可以)
app.autodiscover_tasks()


# 自帶的任務
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
