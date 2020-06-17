from django.contrib import admin
from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^index/', views.IndexView.as_view()),
    re_path(r'^index2/', views.Index2View.as_view()),
]
