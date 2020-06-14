from django.db import models


class News(models.Model):
    title = models.CharField(max_length=40)
    outline = models.TextField()
    url = models.URLField()
    post_date = models.CharField(max_length=30)

    class Meta:
        db_table = "news"
