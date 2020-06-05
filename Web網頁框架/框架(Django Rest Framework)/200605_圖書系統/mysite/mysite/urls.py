from django.contrib import admin
from django.urls import path, re_path, include
from app01 import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'bookshops', viewset=views.BookshopsView)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'api/', include(router.urls)),
]
