from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    height = models.IntegerField()
