from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', viewset=views.UsersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"^api/(?P<version>[v1|v2]+)/", include(router.urls)),
    # =========-JWT內建提供的功能-=========
    # 獲取權杖
    re_path(r"^login/", obtain_jwt_token),  # 請求：POST, data:{'username':jamie, 'password':'jamie851230'}
    # 權杖刷新(須在settings.py中的JWT_AUTH設置 'JWT_ALLOW_REFRESH': True)，且只有為過期之權杖才可刷新
    re_path(r'^api-token-refresh/', refresh_jwt_token),  # 請求:POST, data:{'token': <舊token>}
    # 權杖驗證
    re_path(r'^api-token-verify/', verify_jwt_token),  # 請求:POST, data:{'token': <token>}
]
