from django.db.models import Prefetch
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from app01 import serializers
from app01 import models


class BookshopsView(ModelViewSet):
    # /api/bookshops/頁面，用來顯示所有店家列表
    serializer_class = serializers.BookshopsSerializer
    queryset = models.Bookshops.objects.all()

    # 自定義retrieve顯示
    # /api/bookshops/<shop_id>/頁面，用來顯示這家店所有借閱者資料(包含借了什麼書)
    def retrieve(self, request, *args, **kwargs):
        bookshop_id = self.get_object().id
        # 方法一(效率差，多次使用到SQL)
        # 這是先找出有買過這間書店書的user列表，然後再循環列表，並將買過這間書店的書籍插入
        # user_list = models.Users.objects.filter(lend_books__shop_id=bookshop_id).distinct().values('id', 'name')
        # # print(list(user_list))
        # for user in user_list:
        #     book_list = models.Books.objects.filter(shop_id=bookshop_id, users=models.Users.objects.get(id=user['id']))
        #     print(book_list)
        #     user.setdefault('lend_books', book_list)
        # print(list(user_list))
        # serializer = serializers.UsersSerializer(instance=list(user_list), many=True)

        # 方法二(優，透過聯表提升效率，降低SQL查找次數)
        # 透過prefetch_related()可以進行對多對多字段的聯表操作，降低SQL查找次數
        # Prefetch方法可以讓我們再聯表時進行深層的篩選
        user_list = models.Users.objects.filter(lend_books__shop_id=bookshop_id).distinct().prefetch_related(
            Prefetch('lend_books', queryset=models.Books.objects.filter(shop_id=bookshop_id))
        )
        serializer = serializers.UsersSerializer(instance=user_list, many=True)
        return Response(serializer.data)


class BookshopsBooksView(GenericViewSet):
    queryset = models.Bookshops.objects.all()

    # 自定義list顯示
    #  /api/bookshops/<shop_id>/books/頁面，用來顯示所有該店家有的書籍列表
    def list(self, request, *args, **kwargs):
        bookshop_id = self.get_object().id
        books_list = models.Books.objects.filter(shop_id=bookshop_id)
        # 當instance不止一條數據時，要使用many=True
        serializer = serializers.OnlyBooksSerializer(instance=books_list, many=True)
        return Response(serializer.data)
    
    # 自定義retrieve顯示
    # /api/bookshops/<shop_id>/books/<book_id>/頁面，用來顯示所有借這家店的這本書的借閱者資料
    def retrieve(self, request, *args, **kwargs):
        bookshop_id = self.get_object().id
        # print(bookshop_id)
        # 獲取所有URL上的變數
        # print(self.kwargs)
        user_list = models.Users.objects.filter(lend_books__shop_id=bookshop_id, lend_books=self.kwargs['book_id']).distinct().values('id', 'name')
        # print(list(user_list))
        serializer = serializers.UsersSerializer2(instance=list(user_list), many=True)
        return Response(serializer.data)


class BooksView(ModelViewSet):
    queryset = models.Books.objects.all()
    serializer_class = serializers.BooksSerializer

