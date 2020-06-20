from django.urls import re_path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^computer/', include('computerapp.urls')),
    re_path(r'^api-token-auth/', views.obtain_auth_token),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


if settings.DEBUG:
    # 路由列裡面添加MEDIA_URL，讓我們能找到對應位置的圖片
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
