from rest_framework import serializers
from app01 import models


class BookshopsSerializer(serializers.ModelSerializer):
    # user_id = serializers.SerializerMethodField()  # 自定義顯示
    #
    # def get_user_id(self, obj):  # 自定義顯示的方法，名稱為get_字段名
    #     books_list = obj.books_set.all()
    #     ret = []
    #     for book in books_list:
    #         for user in book.users_set.all():
    #             ret.append({'id': user.id, 'title': user.name})
    #     return ret  # 要顯示的數據

    class Meta:
        model = models.Bookshops  # 關聯的表
        fields = '__all__'
        # fields = ['user_id']
        # # depth = 2


class UsersSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='id')
    user_name = serializers.CharField(source='name')
    # lend_book = serializers.CharField(source='lend_book')

    class Meta:
        model = models.Users  # 關聯的表
        fields = ['user_id', 'user_name', 'lend_books']
        depth = 2

