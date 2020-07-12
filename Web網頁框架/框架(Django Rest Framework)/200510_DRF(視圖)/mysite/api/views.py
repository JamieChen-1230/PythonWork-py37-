from api import models
from api.serializers import RolesSerializer
from rest_framework.response import Response
from api.pagination import MyPageNumberPagination
"""
from rest_framework.generics import GenericAPIView
class RolesView(GenericAPIView):
    queryset = models.Role.objects.all()
    serializer_class = RolesSerializer
    pagination_class = MyPageNumberPagination
    def get(self, request, *args, **kwargs):
        # 獲取數據
        roles = self.get_queryset()
        # 分頁
        page_roles = self.paginate_queryset(roles)
        # 序列化
        ser = self.get_serializer(instance=page_roles, many=True)
        return Response(ser.data)
"""

from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListAPIView
"""
from rest_framework.viewsets import GenericViewSet
class RolesView(GenericViewSet):
    queryset = models.Role.objects.all()
    serializer_class = RolesSerializer
    pagination_class = MyPageNumberPagination

    # 自定義名稱的get方法
    def func1(self, request, *args, **kwargs):
        # 獲取數據
        roles = self.get_queryset()
        # 分頁
        page_roles = self.paginate_queryset(roles)
        # 序列化
        ser = self.get_serializer(instance=page_roles, many=True)
        return Response(ser.data)

    # 自定義名稱的post方法
    def func2(self, request, *args, **kwargs):
        pass
"""

from rest_framework.viewsets import ModelViewSet


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

