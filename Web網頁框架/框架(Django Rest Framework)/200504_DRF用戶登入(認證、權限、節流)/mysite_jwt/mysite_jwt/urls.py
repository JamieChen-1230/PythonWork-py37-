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
# 在urls.py中，添加以下URL路由，以允許通過包含用戶名和密碼的POST獲得令牌。
from rest_framework_jwt.views import obtain_jwt_token
# 如果JWT_ALLOW_REFRESH為True，則可以“刷新” 未過期的令牌以獲得具有更新的過期時間的全新令牌。添加如下網址格式：
from rest_framework_jwt.views import refresh_jwt_token
# 服務會將將從用戶收到的JWT 傳遞給身份驗證服務，並在將受保護資源返回給用戶之前等待JWT 有效的確認。
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api-token-auth/', obtain_jwt_token),
    re_path(r'^api-token-refresh/', refresh_jwt_token),
    re_path(r'^api-token-verify/', verify_jwt_token),
]
