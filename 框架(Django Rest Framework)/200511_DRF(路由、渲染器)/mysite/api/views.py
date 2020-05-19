from api import models
from api.serializers import RolesSerializer
from api.pagination import MyPageNumberPagination
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class RolesView(ModelViewSet):
    """
    mixins.CreateModelMixin,     => 添加
    mixins.RetrieveModelMixin,  => 查詢單條數據(要id)
    mixins.UpdateModelMixin,    => 更新(要id)
    mixins.DestroyModelMixin,   => 刪除(要id)
    mixins.ListModelMixin,         => 數據列表
    """
    queryset = models.Role.objects.all()
    serializer_class = RolesSerializer
    pagination_class = MyPageNumberPagination


# 渲染器
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, AdminRenderer


class RendersView(ModelViewSet):
    queryset = models.Role.objects.all()
    serializer_class = RolesSerializer
    pagination_class = MyPageNumberPagination
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer, AdminRenderer]

