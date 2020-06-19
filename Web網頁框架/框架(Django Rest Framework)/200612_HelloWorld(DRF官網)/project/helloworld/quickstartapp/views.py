from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstartapp.serializers import UserSerializer, GroupSerializer
from quickstartapp.pagination import MyPageNumberPagination


# 視圖集
class UserViewSet(viewsets.ModelViewSet):
    """
    查看、編輯用戶數據的API接口
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    pagination_class = MyPageNumberPagination
    
    
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = MyPageNumberPagination
