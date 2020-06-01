from django.urls import re_path
from django.contrib import admin
from app01 import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^books/', views.books),
    re_path(r'^add_book/', views.add_book),
    re_path(r'^update_book/', views.update_book),
    re_path(r'^delete_book/', views.delete_book),
    re_path(r'^search_book/', views.search_book),
]