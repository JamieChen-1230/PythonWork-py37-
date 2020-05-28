from django.urls import re_path, include, path
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'roles', viewset=views.RolesView)

urlpatterns = [
    path('celery_task', views.celery_task),
    re_path('celery_res/(?P<task_id>[\w-]+)', views.celery_res),
    # 使用DRF路由器幫我們生成URL
    re_path(r'(?P<version>[v1|v2]+)/', include(router.urls)),
]
