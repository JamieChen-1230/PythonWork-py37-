from api import models
from api.serializers import RolesSerializer
from api.pagination import MyPageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from api import filters
from django_filters.rest_framework import DjangoFilterBackend


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

    # 局部配置過濾類
    # 內建過濾器類：OrderingFilter, SearchFilter
    # filter_backends = (OrderingFilter, SearchFilter,)
    # # 內建過濾器可參與排序之字段
    # ordering_fields = ('id', 'title',)
    # # 內建過濾器可搜尋之字段
    # search_fields = ('id', 'title',)

    # 使用DRF自定義過濾器類：LimitFilter
    # filter_backends = (filters.LimitFilter,)

    # 使用django-filter自定義高級過濾器：DjangoFilterBackend
    # 兩行都有才會生效
    filter_backends = (DjangoFilterBackend,)
    filter_class = filters.RoleFilter






