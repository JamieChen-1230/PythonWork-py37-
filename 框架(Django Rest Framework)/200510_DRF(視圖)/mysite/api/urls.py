from django.urls import path, re_path
from api import views


urlpatterns = [
    # re_path(r'^(?P<version>[v1|v2]+)/roles/$', views.RolesView.as_view(), name='roles'),
    # 要額外設置路由映射
    re_path(r'^(?P<version>[v1|v2]+)/roles/$', views.RolesView.as_view({
        'get': 'list',   # 數據列表
        'post': 'create',  # 創建
    })),
    re_path(r'^(?P<version>[v1|v2]+)/roles/(?P<pk>\d+)/$', views.RolesView.as_view({
        'get': 'retrieve',  # 獲取單條數據
        'delete': 'destroy',  # 刪除
        'put':  'update',  # 更新
        'patch': 'partial_update',  # 局部更新
    })),
]
