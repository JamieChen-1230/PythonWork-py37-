from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt import authentication
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from api import models
from api.serializers import UsersSerializer


class UsersViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    UserViewSet
    """
    authentication_classes = (authentication.JSONWebTokenAuthentication,)  # 使用JWT作為認證機制
    # IsAuthenticated 讓只有通過認證者才可使用
    permission_classes = (IsAuthenticated,)
    queryset = models.User.objects.all()
    serializer_class = UsersSerializer
