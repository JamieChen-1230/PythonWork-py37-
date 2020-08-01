from django.db import models


class Bookshops(models.Model):
    title = models.CharField(max_length=32)
    
    
class Books(models.Model):
    title = models.CharField(max_length=32)
    shop = models.ForeignKey(to=Bookshops, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Users(models.Model):
    name = models.CharField(max_length=32)
    lend_books = models.ManyToManyField(to=Books)

