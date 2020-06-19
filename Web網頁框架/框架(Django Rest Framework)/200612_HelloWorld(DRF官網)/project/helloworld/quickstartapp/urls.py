from django.urls import include, path
from rest_framework import routers
from quickstartapp import views

# 路由器
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
