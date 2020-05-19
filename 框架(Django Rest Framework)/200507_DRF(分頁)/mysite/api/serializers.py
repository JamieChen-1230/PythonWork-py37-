from rest_framework import serializers


class RolesSerializer(serializers.Serializer):
    # 字段名必須跟數據庫一致，除非有加source參數
    id = serializers.IntegerField()
    title = serializers.CharField()

