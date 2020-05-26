from django.http import JsonResponse
from rest_framework.views import APIView
from api import models
from api.utils.permission import SVIPPermission, OtherPermission


# 訂單資料(先用dict代替)
ORDER_DICT = {
    1: {
        'name': "jamie",
        'age': 18,
        'gender': '男',
        'content': '...',
    },
    2: {
        'name': "jack",
        'age': 18,
        'gender': '男',
        'content': '***',
    },
}


def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    # hashlib.md5(<<字節>>)
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))  # 加鹽
    return m.hexdigest()  # .hexdigest()返回十六進制字符串


class AuthView(APIView):
    """
    用於用戶登入
    """
    authentication_classes = []  # 為了不套用全局認證
    permission_classes = []  # 為了不套用全局權限

    # 通常用戶登入是用post請求
    def post(self, request, *args, **kwargs):
        self.dispatch()
        ret = {'code': 1000, 'msg': None}
        try:
            user = request._request.POST.get('username')
            pwd = request._request.POST.get('password')
            obj = models.UserInfo.objects.filter(username=user, password=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = '用戶名或密碼錯誤'

            # 登入成功 => 為用戶創造token
            token = md5(user)
            # 存在就更新，不存在就創建
            models.UserToken.objects.update_or_create(user=obj, defaults={'token': token})
            ret['token'] = token
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '請求錯誤'

        return JsonResponse(ret)


class OrderView(APIView):
    """
    訂單相關業務(只讓SVIP有權限)
    """
    # permission_classes = [SVIPPermission, ]  # 不寫 => 表使用默認權限

    # GET：取出訂單(一項或多項)
    def get(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        # 之後資料庫容易出錯，最好都用try包起來。
        try:
            ret['data'] = ORDER_DICT
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '請求錯誤'

        return JsonResponse(ret)


class UserInfoView(APIView):
    """
    用戶相關業務(讓普通用戶和VIP有權限)
    """
    # 不使用默認權限，使用自己的OtherPermission
    permission_classes = [OtherPermission, ]

    # GET：取出(一項或多項)
    def get(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        # 之後資料庫容易出錯，最好都用try包起來。
        try:
            ret['data'] = 'UserInfoView'
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '請求錯誤'

        return JsonResponse(ret)
