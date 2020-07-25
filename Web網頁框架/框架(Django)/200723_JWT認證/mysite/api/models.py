from django.db import models
from django.conf import settings
import datetime
import jwt


class User(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='創建時間')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新時間')
    username = models.EmailField(max_length=255, unique=True, verbose_name='用戶名')
    fullname = models.CharField(max_length=64, null=True, verbose_name='中文名')
    phonenumber = models.CharField(max_length=16, null=True, unique=True, verbose_name='電話')
    is_active = models.BooleanField(default=True, verbose_name='激活狀態')

    def __str__(self):
        return self.username

    @property
    def token(self):
        """
        方便之後在view中調用 => user_obj.token
        """
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        利用PyJWT生成Token，這里傳了三部分內容給JWT，
            第一部分： 是一個Json對象，稱為Payload，主要用來存放有效的信息，例如用戶名，過期時間等等所有你想要傳遞的信息
            第二部分： 是一個秘鑰字串，這個秘鑰主要用在下文Signature簽名中，服務端用來校驗Token合法性，這個秘鑰只有服務端知道，不能泄露
            第三部分： 指定了Signature簽名的算法
        """
        token = jwt.encode({
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'data': {
                'username': self.username,
                'fullname': self.fullname,
                'is_active': self.is_active
            }
        }, settings.SECRET_KEY, algorithm='HS256')
        # 解碼成字符串
        return token.decode('utf-8')

