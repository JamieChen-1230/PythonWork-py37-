from rest_framework import serializers
from app01 import models


# /api/bookshops/頁面，用來顯示所有店家列表
class BookshopsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Bookshops  # 關聯的表
        fields = '__all__'


# /api/bookshops/<shop_id>/頁面，用來顯示這家店所有借閱者資料(包含借了什麼書)
# /api/bookshops/<shop_id>/books/<book_id>/頁面，用來顯示所有借這家店的這本書的借閱者資料
class UsersSerializer(serializers.ModelSerializer):
    # 改顯示之字段名
    user_id = serializers.IntegerField(source='id')
    user_name = serializers.CharField(source='name')

    class Meta:
        model = models.Users  # 關聯的表
        fields = ['user_id', 'user_name', 'lend_books']
        depth = 1


#  /api/bookshops/<shop_id>/books/頁面，用來顯示所有該店家有的書籍列表
class BookshopsBooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Books  # 關聯的表
        fields = '__all__'
