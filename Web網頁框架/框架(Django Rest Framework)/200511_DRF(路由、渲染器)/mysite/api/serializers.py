from rest_framework import serializers
from api import models


class RolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Role  # 關聯的表
        fields = '__all__'

