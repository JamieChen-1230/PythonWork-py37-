from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', viewset=views.UsersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/(?P<version>[v1|v2|v3]+)/', include(router.urls)),
]
