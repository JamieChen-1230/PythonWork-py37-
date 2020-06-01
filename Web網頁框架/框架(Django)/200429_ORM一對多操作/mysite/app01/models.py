from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    # 一對多操作：ORM會自動抓publish的id進行連結，並自動建立publish_id
    publish = models.ForeignKey('Publisher', on_delete=models.CASCADE)  # 外鍵要建在【多】那方


# Publisher對Book：一對多關係
class Publisher(models.Model):
    name = models.CharField(max_length=32)
