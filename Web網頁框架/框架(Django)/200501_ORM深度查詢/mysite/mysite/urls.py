from django.urls import re_path
from django.contrib import admin
from app01 import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^index/', views.index),
    re_path(r'^search_book/', views.search_book),
]
