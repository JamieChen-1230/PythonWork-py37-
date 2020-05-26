from django.contrib import admin
from django.urls import path
from app01 import views


urlpatterns = [
    path('test/', views.test1),
]
