"""
JWT生成的Token是一個用兩個點（.）分割的長字符串
    - 點分割成的三部分分別是Header頭部，Payload負載，Signature簽名：Header.Payload.Signature
    - 其中第一部分Header和第二部分Payload只是對原始輸入的信息轉成了base64編碼，第三部分Signature是用header+payload+secret_key進行加密的結果
"""
import jwt
from rest_framework import exceptions
from django.utils.translation import ugettext as _
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework_jwt.authentication import get_authorization_header
from rest_framework_jwt.settings import api_settings


class MyJWTAuthentication(BaseJSONWebTokenAuthentication):
    """
    Description:
        一、自定義JWT認證，繼承自BaseJSONWebTokenAuthentication
        二、本類中的方法內容幾乎無修改，只為了做筆記
    """

    @staticmethod
    def get_jwt_value(request):
        """
        Description:
            用於獲取前端傳來的認證權杖(token)
        Parameters:
            request: DRF.request對象
        return:
            bytes: b'<token>'
        """
        # 元素為字節類型，auth => [b'jwt', b'<token>']
        auth = get_authorization_header(request).split()
        # 在setting.py中，可以自定義設定，auth_header_prefix => jwt
        auth_header_prefix = api_settings.JWT_AUTH_HEADER_PREFIX.lower()

        if not auth:
            # 若在Headers中沒有得到Authorization則執行
            if api_settings.JWT_AUTH_COOKIE:
                return request.COOKIES.get(api_settings.JWT_AUTH_COOKIE)
            return None

        if auth[0].decode(encoding='UTF-8', errors='strict').lower() != auth_header_prefix:
            # 判斷前綴是否相同
            return None

        if len(auth) == 1:
            msg = _('無效的Authorization請求頭，格式須為「JWT <token>」')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('無效的Authorization請求頭，格式須為「JWT <token>」')
            raise exceptions.AuthenticationFailed(msg)
        return auth[1]

    def authenticate(self, request):
        """
        Description:
            一、自定義認證，必須覆寫authenticate()
            二、主要認證功能
        Parameters:
            request: DRF.request對象
        return:
            tuple: (<model.User對象>, <token>)
        """
        # jwt_value => b'<token>'
        jwt_value = self.get_jwt_value(request)
        if jwt_value is None:
            return None

        try:
            payload = jwt_decode_handler(jwt_value)
        except jwt.ExpiredSignature:
            msg = _('權杖(token)已過期')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = _('權杖(token)解碼發生錯誤')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed()

        # model.User實例對象
        user = self.authenticate_credentials(payload)

        return user, jwt_value  # 返回後，會被賦值給request.user, request.auth


def jwt_response_payload_handler(token, user=None, request=None):
    """
    Description:
        一、因為JWT認證成功之後，默認只返回token，所以要自定義返回資訊的話需要重寫jwt_response_payload_handler()
        二、還須到settings.py中的JWT_AUTH中定義 'JWT_RESPONSE_PAYLOAD_HANDLER': 'api.utils.jwt.jwt_response_payload_handler',
    """
    return {
        'token': token,
        'id': user.id,
        'username': user.username,
        'email': user.email
    }
