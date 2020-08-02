from django.contrib import admin
from django.urls import path, re_path, include
# =================-JWT內建提供的功能-=================
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
# =================-用於生成Swagger文檔-=================
from rest_framework.permissions import IsAuthenticated
from api.utils import permission, jwt
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    # info： 如果省略，則默認為DEFAULT_INFO
    openapi.Info(
        title="BookShops API",
        default_version='v1',
        description="use to test",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="aas124122323@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    # url： API基本網址，如果為空，則將從提供視圖的位置推斷出
    public=True,  # 如果為False，則僅包括當前用戶有權訪問的端點
    # authentication_classes=(jwt.MyJWTAuthentication,),  # 架構視圖本身的身份驗證類
    # permission_classes=(IsAuthenticated, permission.MyPermission,),  # 架構視圖本身的權限類
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # include((<urls>, <應用名稱>), namespace=<實例命名空間>)
    re_path(r"^api/v1/", include(('api.urls', "api"), namespace="v1")),
    # =================-JWT內建提供的功能-=================
    # 獲取權杖
    re_path(r"^login/", obtain_jwt_token),  # 請求：POST, data:{'username':jamie, 'password':'jamie851230'}
    # 權杖刷新(須在settings.py中的JWT_AUTH設置 'JWT_ALLOW_REFRESH': True)，且只有為過期之權杖才可刷新
    re_path(r'^api-token-refresh/', refresh_jwt_token),  # 請求:POST, data:{'token': <舊token>}
    # 權杖驗證
    re_path(r'^api-token-verify/', verify_jwt_token),  # 請求:POST, data:{'token': <token>}
    # =================-用於生成Swagger文檔-=================
    # 獲取沒有UI渲染器的視圖實例
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # 使用指定的UI渲染器獲取視圖實例
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
