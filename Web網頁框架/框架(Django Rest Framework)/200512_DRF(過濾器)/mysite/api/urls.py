from django.urls import re_path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'roles', viewset=views.RolesView)


urlpatterns = [
    re_path(r'(?P<version>[v1|v2]+)/', include(router.urls)),
]
