from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quickstartapp.urls')),
    # rest_framework內建登入系統
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
