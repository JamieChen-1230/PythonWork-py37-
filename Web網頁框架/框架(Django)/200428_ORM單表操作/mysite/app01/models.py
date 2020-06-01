from django.db import models


# create table book(
#     name varchar(20),
#     price int(),
# )
class Book(models.Model):  # 必須要繼承models.Model，python才會知道他是表
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    date = models.DateField()
    author = models.CharField(max_length=32, null=False)  # 不能為空

    def __str__(self):
        return self.name


