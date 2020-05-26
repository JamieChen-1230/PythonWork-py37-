from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        if not token:
            raise exceptions.AuthenticationFailed('用戶認證失敗')
        return ('jamie', None)


# 要繼承APIView，APIView基礎上也是通過繼承View實現的。
class DogView(APIView):
    authentication_classes = [MyAuthentication, ]

    # GET：取出資源(一項或多項)
    def get(self, request, *args, **kwargs):
        print(request.user)
        return HttpResponse('獲取狗狗')

    # POST：新建資源
    def post(self, request, *args, **kwargs):
        return HttpResponse('創建狗狗')

    # PUT：更新資源(全部更新)
    def put(self, request, *args, **kwargs):
        return HttpResponse('更新狗狗')

    # PATCH：更新資源(局部更新)
    def patch(self, request, *args, **kwargs):
        return HttpResponse('更新狗狗')

    # DELETE：刪除資源
    def delete(self, request, *args, **kwargs):
        return HttpResponse('刪除狗狗')


