from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from api import models
import json
from api.serializers import RolesSerializer, UsersSerializer, GroupsSerializer
from rest_framework import serializers


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
        users = models.UserInfo.objects.all()
        # 若要使用到HyperlinkedIdentityField字段，這邊要加上context={'request': request}
        ser = UsersSerializer(instance=users, many=True, context={'request': request})   # many=True表取出多條數據
        # print(ser.data)  # 經過序列化的data(類型為OrderedDict)
        ret = json.dumps(ser.data, ensure_ascii=False)  # ensure_ascii=False才能顯示中文
        return HttpResponse(ret)


class GroupsView(APIView):

    def get(self, request, *args, **kwargs):
        fk = kwargs.get('fk')
        obj = models.UserGroup.objects.filter(id=fk).first()
        ser = GroupsSerializer(instance=obj, many=False)   # many=True表取出多條數據
        # print(ser.data)  # 經過序列化的data(類型為OrderedDict)
        ret = json.dumps(ser.data, ensure_ascii=False)  # ensure_ascii=False才能顯示中文

        return HttpResponse(ret)


# ########################### 請求驗證 #############################
# 方法一：validators設置自定義驗證規則
class Myvalidator(object):
    def __init__(self, x):
        self.x = x

    # 驗證規則
    def __call__(self, value):
        if not value.startswith(self.x):
            message = 'title開頭必須為 %s' % self.x
            raise serializers.ValidationError(message)


class VerifySerializer(serializers.Serializer):
    # error_messages為錯誤信息
    # 方法一：validators設置自定義驗證規則
    title = serializers.CharField(
        error_messages={'required': 'title不能為空'}, validators=[Myvalidator('jamie')])

    # (推薦)方法二：鉤子函數設置自定義驗證規則
    # def validate_字段名(self, data)，data為request.data.get(字段名)
    def validate_title(self, data):
        from rest_framework import exceptions
        if not data.endswith('老男人'):
            raise exceptions.ValidationError('title結尾必須為老男人')
        return data  # 驗證成功回傳data


class VerifyView(APIView):

    def post(self, request, *args, **kwargs):
        # request.data 為獲取經過解析器解析的數據
        ser = VerifySerializer(data=request.data)
        # 驗證
        if ser.is_valid():
            print(ser.validated_data)
        else:
            print(ser.errors)

        return HttpResponse('提交數據')
