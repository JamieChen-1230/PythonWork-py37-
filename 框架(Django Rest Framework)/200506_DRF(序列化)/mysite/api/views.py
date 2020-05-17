from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from api import models
import json
from api.serializers import RolesSerializer, UsersSerializer


class RolesView(APIView):

    def get(self, request, *args, **kwargs):
        # 方式一：
        # roles = models.Role.objects.all().values('id', 'title')
        # # 因為Queryset不能被json
        # roles = list(roles)
        # ret = json.dumps(roles, ensure_ascii=False)  # ensure_ascii=False才能顯示中文

        # 方法二(透過DRF序列化)：
        roles = models.Role.objects.all()
        ser = RolesSerializer(instance=roles, many=True)   # many=True表取出多條數據
        # print(ser.data)  # 經過序列化的data(類型為OrderedDict)
        ret = json.dumps(ser.data, ensure_ascii=False)  # ensure_ascii=False才能顯示中文

        return HttpResponse(ret)


class UsersView(APIView):

    def get(self, request, *args, **kwargs):
        # 透過DRF序列化：
        users = models.UserInfo.objects.all()
        ser = UsersSerializer(instance=users, many=True)   # many=True表取出多條數據
        # print(ser.data)  # 經過序列化的data(類型為OrderedDict)
        ret = json.dumps(ser.data, ensure_ascii=False)  # ensure_ascii=False才能顯示中文

        return HttpResponse(ret)
