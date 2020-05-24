from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api import serializers
from api import models
from rest_framework import status


class UsersViewSet(ModelViewSet):
    queryset = models.Users.objects.all()
    serializer_class = serializers.UsersSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        print(queryset)
        serializer = self.get_serializer(queryset, many=True)
        print(serializer.data)
        ret = {
            'data': serializer.data,
            'message': 'Success',
        }
        return Response(ret)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        ret = {
            'data': serializer.data,
            'message': 'Success',
        }
        return Response(ret, status=status.HTTP_201_CREATED, headers=headers)

