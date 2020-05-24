from rest_framework import serializers
from api import models


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Users
        fields = '__all__'
