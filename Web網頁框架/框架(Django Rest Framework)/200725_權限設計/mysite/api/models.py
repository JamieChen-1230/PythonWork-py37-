from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
import datetime


class Role(models.Model):
    title = models.CharField(max_length=32)
    permissions = models.ManyToManyField('Permission', through='RolePermission')

    def __str__(self):
        return self.title


class UserManager(BaseUserManager):
    """
    Description:
        一、重寫UserManager，繼承自BaseUserManager
        二、須定義以下方法(create_user和create_superuser)，並依照我們想要的欄位去創建用戶
    """
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("請填入信箱！")
        if not password:
            raise ValueError("請填入密碼！")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        print("extra_fields", extra_fields)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('超級用戶必須將is_staff設為True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('超級用戶必須將is_superuser設為True')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Description:
        一、自定義User表，繼承自AbstractBaseUser和PermissionsMixin，這樣就可以自定義我們想要的欄位
        二、但有些欄位會被之後的方法調用，所以必須定義(EX:is_active, is_staff)
        三、USERNAME_FIELD可以選擇哪個欄位當作帳號(還須完成<五>才能實現)
        四、REQUIRED_FIELDS可以設置必填欄位
        五、重新定義Manager對象
        六、最後要記得到settings.py中定義 AUTH_USER_MODEL='<app_name>.User'，這樣Django才會找我們的表當作User表
    """
    # 要定義的其他字段(password等字段，內建有幫我們定義的，就不需額外再定義)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150)
    telephone = models.CharField(max_length=11, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    # 像is_staff這種會被其他內建函數調用的字段我們也須定義
    is_staff = models.BooleanField(default=False)  # 決定用戶是否可以訪問admin管理界面
    is_active = models.BooleanField(default=True)
    # 多對多字段，through參數能讓我們自定義中間表
    roles = models.ManyToManyField('Role', through='UserRole')

    # 指定email作為USERNAME_FIELD，以後使用authenticate函數驗證的時候，就可以根據email來驗證
    USERNAME_FIELD = 'email'
    # USERNAME_FIELD對應的email字段和密碼字段默認是必須的字段
    # 而其他必填字段可以通過REQUIRED_FIELDS來設定
    REQUIRED_FIELDS = ['username']

    # 重新定義Manager對象，在創建user的時候使用email和password，而不是使用原來的username和password
    objects = UserManager()

    def __str__(self):
        return self.email


class UserRole(models.Model):
    """
    Description:
        一、在ManyToManyField字段中，加入through參數，即可自定義中間表
        二、其中必須建立對雙方表的一對多(ForeignKey)字段，on_delete刪除時的模式
        三、也可以新增額外字段(EX:push_at)
    """
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    role_id = models.ForeignKey('Role', on_delete=models.CASCADE)
    push_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return '%s | %s' % (self.user_id, self.role_id)


class Permission(models.Model):
    resource = models.CharField(max_length=32)
    method = models.CharField(max_length=32)

    def __str__(self):
        return '%s | %s' % (self.resource, self.method)


# 自定義中間表
class RolePermission(models.Model):
    permission_id = models.ForeignKey('Permission', on_delete=models.CASCADE)
    role_id = models.ForeignKey('Role', on_delete=models.CASCADE)
    push_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return '%s | %s' % (self.permission_id, self.role_id)


# error
# class MyUser(models.Model):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#     username = models.CharField(max_length=150)
#     is_active = models.BooleanField(default=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#
#     def __str__(self):
#         return self.username
