from django.db import models


class Books(models.Model):  # 必須要繼承models.Model，python才會知道他是表
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    # 多對多操作：自動創造book_authors的表，另一種方法是自己建一個表且有兩個ForeignKey
    authors = models.ManyToManyField('Author')  # Good


# # 第二種方法
# class Book_author(models.Model):
#     book = models.ForeignKey('Book')
#     author = models.ForeignKey('Author')

class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
