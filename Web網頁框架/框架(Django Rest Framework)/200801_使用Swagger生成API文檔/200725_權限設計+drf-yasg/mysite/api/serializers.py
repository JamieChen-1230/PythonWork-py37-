from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from api import models
from django.contrib.auth.hashers import make_password, check_password
import re


class UsersSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        """
        Description:
            一、當ViewSet中調用serializer.save()時，會依照實例紀錄是否存在，執行create()或update()方法，最後執行instance.save()
            二、覆寫create()，讓在將資料寫入資料庫(instance.save())前，先將明文密碼進行加密
        Parameters:
            validated_data: 為一dict，已經過validate()驗證的資料
        returns:
            model實例對象: instance
        """
        if validated_data.get('password', None):  # 為前端傳來的明文密碼進行加密
            # make_password為Django內建提供的功能
            validated_data['password'] = make_password(validated_data['password'])

        if validated_data.get('is_active', None) is False:  # is_active默認設為true
            validated_data['is_active'] = True

        instance = super(UsersSerializer, self).create(validated_data=validated_data)
        return instance

    def validate(self, attrs):
        """
        Description:
            一、驗證會在serializer.save()前調用
            二、自定義驗證，覆寫validate()，可對想要驗證的字段新增驗證規則
        Parameters:
            attrs: 為一OrderedDict，為前端傳來的資料
        returns:
            OrderedDict: attrs
        """
        for field, val in attrs.items():
            if field == 'telephone':
                if not re.fullmatch("\\d{10}", val):
                    raise ValidationError(detail="電話格式輸入錯誤")
        return attrs

    class Meta:
        # 指名要與哪張表產生關係
        model = models.User
        fields = '__all__'
        depth = 1
        # 將密碼設為唯寫欄位
        extra_kwargs = {'password': {'write_only': True}}

