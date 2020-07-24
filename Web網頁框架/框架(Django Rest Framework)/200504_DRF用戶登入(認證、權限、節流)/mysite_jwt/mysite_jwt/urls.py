"""mysite_jwt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
import api.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 獲取權杖
    re_path(r"^login/", obtain_jwt_token),  # 請求：POST, data:{'username':jamie, 'password':'jamie851230'}
    # 權杖刷新(須在settings.py中的JWT_AUTH設置 'JWT_ALLOW_REFRESH': True)，且只有為過期之權杖才可刷新
    re_path(r'^api-token-refresh/', refresh_jwt_token),  # 請求:POST, data:{'token': <舊token>}
    # 權杖驗證
    re_path(r'^api-token-verify/', verify_jwt_token),  # 請求:POST, data:{'token': <token>}
    # 測試頁面
    re_path(r"^roles/", api.views.RolesView.as_view({'get': 'list'})),  # 須在Headers中帶有{'Authorization': <token>}
]
