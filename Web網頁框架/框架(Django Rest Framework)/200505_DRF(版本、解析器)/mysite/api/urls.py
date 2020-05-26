from django.urls import path, re_path
from api import views

urlpatterns = [
    path('users/', views.UsersView.as_view()),
    # re_path要使用正則表達式時使用
    re_path(r'^(?P<version>[v1|v2]+)/users/$', views.UsersView.as_view(), name='uuu'),  # name為別名
    path('parser/', views.ParserView.as_view()), 
]
