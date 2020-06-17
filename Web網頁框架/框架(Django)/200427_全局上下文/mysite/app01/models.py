from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return u'Menu:%s' % self.title

    class Meta:
        db_table = 't_menu'
