from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time


# 這裡使用shared_task的原因是因為可以讓其他Django app下也可以調用此task
@shared_task
def add(x, y):
    time.sleep(20)
    return x + y


@shared_task
def fib(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    elif x >= 3:
        return fib(x-1) + fib(x-2)

