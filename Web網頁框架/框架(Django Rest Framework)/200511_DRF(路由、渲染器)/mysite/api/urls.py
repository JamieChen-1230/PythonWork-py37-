from django.urls import re_path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'roles', viewset=views.RolesView)

router2 = routers.DefaultRouter()
router2.register(r'roles', viewset=views.RendersView)


urlpatterns = [
    # # 要額外設置路由映射
    # re_path(r'^(?P<version>[v1|v2]+)/roles/$', views.RolesView.as_view({
    #     'get': 'list',   # 數據列表
    #     'post': 'create',  # 創建
    # })),
    # re_path(r'^(?P<version>[v1|v2]+)/roles/(?P<pk>\d+)/$', views.RolesView.as_view({
    #     'get': 'retrieve',  # 獲取單條數據
    #     'delete': 'destroy',  # 刪除
    #     'put':  'update',  # 更新
    #     'patch': 'partial_update',  # 局部更新
    # })),
    # # 可以選定以甚麼格式呈現(渲染器提供的)
    # # EX: http://127.0.0.1:8000/api/v1/roles.json/  =>  以json格式呈現
    # re_path(r'^(?P<version>[v1|v2]+)/roles\.(?P<format>\w+)/$', views.RolesView.as_view({
    #     'get': 'list',   # 數據列表
    #     'post': 'create',  # 創建
    # })),

    # 使用DRF路由器幫我們生成URL
    # 使用這個就等於幫我們生成了以上全部URL
    re_path(r'(?P<version>[v1|v2]+)/', include(router.urls)),

    # 渲染器測試
    re_path(r'^(?P<version>[v1|v2]+)/test/', include(router2.urls)),
]
