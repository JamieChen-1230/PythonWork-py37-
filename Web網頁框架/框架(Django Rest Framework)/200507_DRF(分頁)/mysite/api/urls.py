from django.urls import path, re_path
from api import views


urlpatterns = [
    re_path(r'^(?P<version>[v1|v2]+)/roles/$', views.RolesView.as_view(), name='roles'),  # name為別名
]
