from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt import authentication
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import mixins
from api import models
from api.serializers import UsersSerializer
from api.utils import permission


class UsersViewSet(ModelViewSet):
    # Headers須帶有{'Authorization': JWT <token>}才能訪問
    # IsAuthenticated 讓只有通過認證者才可使用
    permission_classes = (IsAuthenticated, permission.MyPermission, )
    queryset = models.User.objects.all()
    serializer_class = UsersSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # # 高級ORM SQL，之後要做比較複雜的sql語句時能使用
        # queryset = models.User.objects.extra(
        #     where=['id >= 2'],
        # )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


