from django.urls import path, re_path
from app01 import views


# re_path(正則表達式, views視圖函數, 參數, 別名)
# path(路徑, views視圖函數, 參數, 別名)
# 由上到下匹配
urlpatterns = [
    # -----無命名分組url配置： re_path(正則表達式(有分組), views視圖函數)-----
    re_path(r'no_name_grouping/(\d{4})/(\d{2})', views.no_name),
    # -----有命名分組url配置： re_path(正則表達式(有分組), views視圖函數)-----
    re_path(r'name_grouping/(?P<year>\d{4})/(?P<month>\d{2})', views.has_name),  # 函數參數需對應命名

    # -----基本url配置： path(正則表達式, views視圖函數)-----
    path('no_alias_register', views.no_alias_register),
    # -----有別名url配置： path(正則表達式, views視圖函數, 別名)-----
    path('alias_register', views.alias_register, name="reg"),  # 使用別名，減低維護複雜度
]
