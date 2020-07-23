from django.db import models


class UserInfo(models.Model):
    user_type_choices = (
        (1, "普通用戶"),
        (2, "VIP"),
        (3, "SVIP"),
    )
    user_type = models.IntegerField(choices=user_type_choices)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.username


class UserToken(models.Model):
    user = models.OneToOneField(to="UserInfo", on_delete=models.CASCADE)
    token = models.CharField(max_length=64)

    def __str__(self):
        return self.user.username
