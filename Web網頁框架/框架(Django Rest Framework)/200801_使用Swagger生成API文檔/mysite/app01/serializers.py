from rest_framework import serializers
from app01 import models


# /api/bookshops/頁面，用來顯示所有店家列表
class BookshopsSerializer(serializers.ModelSerializer):
    # 更改顯示之字段名，因為前端工程師可能會要求字段規格
    shop_id = serializers.IntegerField(source='id')
    shop_name = serializers.CharField(source='title')

    class Meta:
        model = models.Bookshops  # 關聯的表
        fields = ['shop_id', 'shop_name']


# /api/bookshops/<shop_id>/books/<book_id>/頁面，用來顯示所有借這家店的這本書的借閱者資料
class UsersSerializer2(serializers.ModelSerializer):
    # 更改顯示之字段名，因為前端工程師可能會要求字段規格
    user_id = serializers.IntegerField(source='id')
    user_name = serializers.CharField(source='name')

    class Meta:
        model = models.Users  # 關聯的表
        fields = ['user_id', 'user_name']


#  /api/books/頁面，用來顯示所有書籍列表(包括所屬店家訊息)
#  /api/books/<book_id>/頁面，用來顯示指定書籍信息(包括所屬店家訊息)
class BooksSerializer(serializers.ModelSerializer):
    # 更改顯示之字段名，因為前端工程師可能會要求字段規格
    book_id = serializers.IntegerField(source='id')
    book_name = serializers.CharField(source='title')
    # 嵌套另一個Serializer
    shop = BookshopsSerializer(many=False)

    class Meta:
        model = models.Books
        fields = ['book_id', 'book_name', 'shop']


#  /api/bookshops/<shop_id>/books/頁面，用來顯示所有該店家有的書籍列表(不帶任何店家信息)
class OnlyBooksSerializer(serializers.ModelSerializer):
    # 更改顯示之字段名，因為前端工程師可能會要求字段規格
    book_id = serializers.IntegerField(source='id')
    book_name = serializers.CharField(source='title')

    class Meta:
        model = models.Books
        fields = ['book_id', 'book_name']


# /api/bookshops/<shop_id>/頁面，用來顯示這家店所有借閱者資料(包含借了什麼書)
class UsersSerializer(serializers.ModelSerializer):
    # 更改顯示之字段名，因為前端工程師可能會要求字段規格
    user_id = serializers.IntegerField(source='id')
    user_name = serializers.CharField(source='name')
    # 嵌套另一個Serializer
    lend_books = OnlyBooksSerializer(many=True)

    class Meta:
        model = models.Users  # 關聯的表
        fields = ['user_id', 'user_name', 'lend_books']
        # 因為想要不顯示某些字段，所以不使用depth，而是嵌套另一個Serializer
        # depth = 1
