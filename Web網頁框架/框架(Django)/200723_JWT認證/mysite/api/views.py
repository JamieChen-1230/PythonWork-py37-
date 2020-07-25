from django.conf import settings
from django.http import JsonResponse
from api import models
import jwt
from django.core.exceptions import ObjectDoesNotExist

"""
來源：https://my.oschina.net/37Y37/blog/3004682
測試工具： postman
測試： 
    1.先用post登入到login中獲取token(只要有username即可，EX:jamie@kimo.com)
    2.在用get到users頁面時，記得要在Headers中加入Authorization: yoyoyo <Signature>
"""


def login(request):
    if request.method == "POST":
        user = request.POST.get("username")
        ret = {"code": 200, "token": None}
        if user:
            try:
                user_obj = models.User.objects.get(username=user)
            except ObjectDoesNotExist:
                return JsonResponse({"status_code": 401, "message": "此用戶不存在"})
            if user_obj:
                token = user_obj.token
                ret["token"] = token
                print('YOYOYO ' + token)
                return JsonResponse(ret)

        return JsonResponse(ret)
    else:
        return JsonResponse({"message": "for test"})


def auth_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        try:
            # 因為我們設計的HTTP_AUTHORIZATION是「<type> <Signature>」
            # type我們可以跟前端約定要叫甚麼，這裡使叫yoyoyo
            # Signature是用header+payload+secret_key進行加密的結果
            auth = request.META.get('HTTP_AUTHORIZATION').split()
            # 所以auth應該要長這樣 ['yoyoyo', <Signature>]
        except AttributeError:
            return JsonResponse({"code": 401, "message": "請求頭中無攜帶AUTHORIZATION"})

        # 用戶通過API獲取數據驗證流程
        if auth[0].lower() == 'yoyoyo':
            try:
                # token解碼
                # 服務端在有秘鑰的情況下可以直接對JWT生成的Token進行解密，解密成功說明Token正確，且數據沒有被篡改
                auth_dict = jwt.decode(auth[1], settings.SECRET_KEY, algorithms=['HS256'])
                print(auth_dict)
                username = auth_dict.get('data').get('username')
            except jwt.ExpiredSignatureError:
                return JsonResponse({"status_code": 401, "message": "Token expired"})
            except jwt.InvalidTokenError:
                return JsonResponse({"status_code": 401, "message": "Invalid token"})
            except Exception as e:
                return JsonResponse({"status_code": 401, "message": "Can not get user object"})

            try:
                user = models.User.objects.get(username=username)
            except ObjectDoesNotExist:
                return JsonResponse({"status_code": 401, "message": "此用戶不存在"})

            if not user.is_active:
                return JsonResponse({"status_code": 401, "message": "此用戶未被激活或是已被刪除"})
        else:
            return JsonResponse({"status_code": 401, "message": "不支持此token_type"})
        return view_func(request, *args, **kwargs)

    return _wrapped_view


# 為要認證的function添加裝飾器
@auth_required
def list_user(request):
    if request.method == "GET":
        user_list = models.User.objects.all().values('id', 'username', 'fullname')
        user_list = list(user_list)
        print(user_list)
        return JsonResponse(user_list, safe=False, json_dumps_params={'ensure_ascii': False})
