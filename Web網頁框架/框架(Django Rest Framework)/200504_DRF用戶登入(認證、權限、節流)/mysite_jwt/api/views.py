from rest_framework.permissions import IsAuthenticated
from api.serializers import RolesSerializer
from rest_framework.viewsets import ModelViewSet
from api import models
from rest_framework_jwt import authentication


class RolesView(ModelViewSet):
    """
    測試用頁面
    """
    authentication_classes = (authentication.JSONWebTokenAuthentication,)  # 使用JWT作為認證機制
    permission_classes = (IsAuthenticated,)  # 設置權限，讓只有通過認證者才可使用
    queryset = models.Role.objects.all()
    serializer_class = RolesSerializer
