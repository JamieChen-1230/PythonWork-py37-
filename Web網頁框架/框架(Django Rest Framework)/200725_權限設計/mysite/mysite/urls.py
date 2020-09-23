from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    # include((<urls>, <應用名稱>), namespace=<實例命名空間>)
    re_path(r"^api/v1/", include(('api.urls', "api"), namespace="v1")),
    # =========-JWT內建提供的功能-=========
    # 獲取權杖
    re_path(r"^login/", obtain_jwt_token),  # 請求：POST, data:{'email':jackooo@kimo.com, 'password':'jack000'}
    # 權杖刷新(須在settings.py中的JWT_AUTH設置 'JWT_ALLOW_REFRESH': True)，且只有為過期之權杖才可刷新
    re_path(r'^api-token-refresh/', refresh_jwt_token),  # 請求:POST, data:{'token': <舊token>}
    # 權杖驗證
    re_path(r'^api-token-verify/', verify_jwt_token),  # 請求:POST, data:{'token': <token>}
]
