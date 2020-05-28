from __future__ import absolute_import, unicode_literals
# 因為導入absolute_import的關係，所以要調用我們自己目錄下寫的celery.py要加 .
from .celery import app as celery_app

# 為了讓Django啟動時，可以自動導入Celery app，也讓之後配置的shared_task可以使用此應用
__all__ = ['celery_app']
