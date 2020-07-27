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


# 重寫UserManager
class UserManager(BaseUserManager):
    """
    Description:
        因為我們希望要用email當作帳號，所以我們須重新定義原方法
    """
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("請填入信箱號碼！")
        if not password:
            raise ValueError("請填入密碼！")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


# 當我們不滿意原本的User時，能透過繼承AbstractBaseUser和PermissionsMixin(原User也是繼承這個類)來定義我們想要的字段
# 並在設計好此表後，到settings.py中設定AUTH_USER_MODEL = 'appname.User'，讓django知道我們要使用的表是此表
class User(AbstractBaseUser, PermissionsMixin):
    """
    Description:
        一、繼承AbstractBaseUser和PermissionsMixin，可以自定義我們想要的欄位
        二、但有些欄位會被之後的方法調用，所以須定義(EX:is_active, is_staff)
        三、USERNAME_FIELD可以選擇哪個欄位當作帳號(還須完成<五>才能實現)
        四、REQUIRED_FIELDS可以設置必填欄位
        五、重新定義Manager對象
        六、最後要記得到settings.py中定義 AUTH_USER_MODEL='<app_name>.User'
    """
    # 要定義的其他字段(password等字段他們有幫我們定義的，就不用再定義)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150)
    telephone = models.CharField(max_length=11, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    # 像is_staff這種會被其他內建函數調用的字段我們也須定義
    is_staff = models.BooleanField(default=False) 
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

    # 以下get_full_nam()和get_short_name()是因為原User有定義，所以照著定義會比較好
    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.email


# 自定義中間表
class UserRole(models.Model):
    """
    Description:
        透過自定義中間表可以新增額外的字段(EX:push_at)
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

