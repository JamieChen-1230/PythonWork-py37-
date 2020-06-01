# 總路由分發
from django.urls import path, re_path, include
from app01 import views


urlpatterns = [
    # -----基本的url配置： path(路徑, views視圖函數)-----
    path('login/', views.login),
    # -----基本的url配置2： re_path(可使用正則表達式之路徑, views視圖函數)-----
    re_path(r'^show_time/$', views.show_time),   # ^ 匹配字符串須為網址開頭, $ 須為網址結尾
    # -----進階路由分發(include(欲分配至的url檔))-----
    re_path(r'^app01/', include('app01.urls')),  # 有關app01的網址都移到app01的urls，這樣APP多時才不會搞混
]
