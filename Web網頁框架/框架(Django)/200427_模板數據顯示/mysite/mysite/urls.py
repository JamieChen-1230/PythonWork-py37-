from django.urls import re_path
from django.contrib import admin
from app01 import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'show_time/', views.show_time, name='show_time'),
    re_path(r'^variable/', views.variable),
    re_path(r'^label/', views.label),
]
