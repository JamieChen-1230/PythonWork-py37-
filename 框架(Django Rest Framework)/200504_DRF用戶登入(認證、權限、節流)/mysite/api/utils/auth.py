from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from api import models


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        print(token)
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用戶驗證失敗')
        # 在rest framework內會自動將return的這兩個字段賦值給request，以供操作使用。
        # 會賦值給(request.user, request.auth)
        return (token_obj.user, token_obj)

