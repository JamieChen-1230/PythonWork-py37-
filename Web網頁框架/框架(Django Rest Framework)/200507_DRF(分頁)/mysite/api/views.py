from rest_framework.views import APIView
from api import models
from api.serializers import RolesSerializer
from rest_framework.response import Response
from api.pagination import MyPageNumberPagination, MyLimitOffsetPagination, MyCursorPagination


class RolesView(APIView):

    def get(self, request, *args, **kwargs):
        # 獲取所有數據
        roles = models.Role.objects.all()
        # 創建分頁對象
        pg = MyCursorPagination()
        # 獲取分頁大小的數據
        page_roles = pg.paginate_queryset(queryset=roles, request=request, view=self)
        # 序列化
        ser = RolesSerializer(instance=page_roles, many=True)  # many=True表取出多條數據

        # 方法一：
        # ret = json.dumps(ser.data, ensure_ascii=False)  # ensure_ascii=False才能顯示中文
        # return HttpResponse(ret)
        # (推薦)方法二：
        # 使用DRF的渲染器，不用轉json，他會自動幫我們處理
        # return Response(ser.data)
        # (推薦)方法三：
        # 使用DRF分頁提供的渲染器，功能更強(幫我們生成了上下一頁)
        return pg.get_paginated_response(data=ser.data)

