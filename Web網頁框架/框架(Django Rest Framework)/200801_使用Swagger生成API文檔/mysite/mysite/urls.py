from django.contrib import admin
from django.urls import path, re_path, include
from app01 import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'bookshops', viewset=views.BookshopsView)
router.register(r'books', viewset=views.BooksView)

# =================-用於生成Swagger文檔-=================
from rest_framework import permissions
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
    # authentication_classes： 架構視圖本身的身份驗證類
    permission_classes=(permissions.AllowAny,),  # 架構視圖本身的權限類
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'api/bookshops/(?P<pk>\d+)/books/$', views.BookshopsBooksView.as_view({
        'get': 'list',  # 獲取單條數據
    })),
    re_path(r'api/bookshops/(?P<pk>\d+)/books/(?P<book_id>\d+)/$', views.BookshopsBooksView.as_view({
        'get': 'retrieve',  # 獲取單條數據
    })),
    re_path(r'api/', include(router.urls)),
    # =================-用於生成Swagger文檔-=================
    # 獲取沒有UI渲染器的視圖實例
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # 使用指定的UI渲染器獲取視圖實例
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
