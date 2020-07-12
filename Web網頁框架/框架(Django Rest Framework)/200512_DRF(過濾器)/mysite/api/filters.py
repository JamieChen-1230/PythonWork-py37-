from rest_framework.filters import BaseFilterBackend
from django_filters import rest_framework as filters  # pip install django-filter
from api import models


# 自定義filter(最低階)
class LimitFilter(BaseFilterBackend):
    # 必須實現filter_queryset()方法，並return一個queryset
    def filter_queryset(self, request, queryset, view):
        lim = request.query_params.get('lim', None)
        if lim:
            return queryset[:int(lim)]
        return queryset


class RoleFilter(filters.FilterSet):
    # 自定義查詢字段
    # field_name為要查的字段名，lookup_expr為查找時使用的表達式，label為前端顯示的名字，required=True為必填欄位
    # 透過d_g=&title_c=
    id_g = filters.NumberFilter(field_name="id", lookup_expr='gte', label="大於id", required=True)
    title_c = filters.CharFilter(field_name="title", lookup_expr='icontains')

    class Meta:
        model = models.Role  # 模型名
        # 透過title__icontains=&id__gte=&id__lte=使用
        fields = {
            'title': ['icontains'],  # title字段可使用icontains包含查找
            'id': ['gte', 'lte'],  # id字段可使用gte大於等於和lte小於等於查找
        }



