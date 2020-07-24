from django.contrib import admin
from django.urls import path, re_path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^login/', views.login),
    re_path(r'^users/', views.list_user),
]
