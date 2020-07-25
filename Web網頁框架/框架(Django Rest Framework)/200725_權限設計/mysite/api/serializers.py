from rest_framework import serializers
from api import models


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User  # 關聯的表
        fields = '__all__'

