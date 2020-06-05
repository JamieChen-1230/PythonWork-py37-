from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from app01 import serializers
from app01 import models


class BookshopsView(ModelViewSet):
    serializer_class = serializers.BookshopsSerializer
    queryset = models.Bookshops.objects.all()

    # 自定義顯示
    def retrieve(self, request, *args, **kwargs):
        bookshop_id = self.get_object().id
        user_list = models.Users.objects.filter(lend_books__shop_id=bookshop_id).values('id', 'name')
        print(list(user_list))
        for user in user_list:
            book_list = models.Books.objects.filter(shop_id=bookshop_id, users=models.Users.objects.get(id=user['id']))
            print(book_list)
            user.setdefault('lend_books', book_list)
        serializer = serializers.UsersSerializer(instance=list(user_list), many=True)
        return Response(serializer.data)


