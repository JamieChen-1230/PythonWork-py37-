from django.urls import path, re_path
from api import views


urlpatterns = [
    # 序列化
    re_path(r'^(?P<version>[v1|v2]+)/roles/$', views.RolesView.as_view(), name='roles'),  # name為別名
    re_path(r'^(?P<version>[v1|v2]+)/userinfo/$', views.UsersView.as_view(), name='user'),
    re_path(r'^(?P<version>[v1|v2]+)/group/(?P<fk>\d+)/$', views.GroupsView.as_view(), name='gp'),
    # 請求驗證
    re_path(r'^(?P<version>[v1|v2]+)/verify_gp/$', views.VerifyView.as_view(), name='verify_gp'),
]
