from django.shortcuts import render, HttpResponse, redirect
from app01 import models


def books(request):
    book_list = models.Books.objects.all()
    return render(request, 'books.html', locals())


def add_book(request):
    # ----------一對多----------
    # 方法一
    # Book.objects.create(name='c++', price=999, publish_id=1)
    # 方法二
    obj_publisher = models.Publisher.objects.get(name='台灣出版社')
    models.Books.objects.create(name='c++', price=455, publish=obj_publisher)
    return redirect('/books/')


def update_book(request):
    models.Books.objects.filter(name='c++').update(price=666)
    return redirect('/books/')


def delete_book(request):
    models.Books.objects.filter(name='c++').delete()
    return redirect('/books/')


def search_book(request):
    # obj_book = models.Books.objects.get(name='python')
    # print(obj_book.name)
    # # 一對多：obj_book.publish(外鍵)一定是一個對象
    # # obj_book.publish是publisher的對象
    # print(obj_book.publish.name)

    # 找出吉米出版社出的書
    # 方式一：
    # obj_publisher = models.Publisher.objects.get(name='吉米出版社')
    # queryset_book = models.Books.objects.filter(publish=obj_publisher).values('name', 'price')
    # print(queryset_book)
    # 方式二：
    # obj_publisher = models.Publisher.objects.get(name='吉米出版社')
    # queryset_book = obj_publisher.books_set.all().values('name', 'price')  # 主表_set
    # print(queryset_book)
    # 方法三：雙下滑線查詢(最好)
    # queryset_book = models.Books.objects.filter(publish__name='吉米出版社').values('name', 'price')
    # print(queryset_book)

    # 找出python的出版社
    # 方式一：雙下滑線查詢
    # queryset_publish = models.Publisher.objects.filter(books__name='python').values('name')
    # print(queryset_publish)
    # 方式二：雙下滑線查詢
    # print(models.Books.objects.filter(name='python').values('publish__name'))

    # 減少sql查詢次數
    # # book_list = models.Books.objects.all()
    # 一次聯表查詢獲取所有的數據(一次查多張表)，聯太多表時會有性能的損耗
    # book_list = models.Books.objects.all().select_related('publish', )  # 能合併多張表
    # for book in book_list:
    #     print(book.id, book.name, book.publish_id)
    #     print(book.publish.name)  # 這需要額外再做一次sql請求

    # 減少sql查詢次數(2)
    # # book_list = models.Books.objects.all()
    # 直接進行兩次sql語句查詢(沒做聯表)
    # book_list = models.Books.objects.all().prefetch_related('publish', )  # 能合併多張表
    # for book in book_list:
    #     print(book.id, book.name, book.publish_id)
    #     print(book.publish.name)  # 這需要額外再做一次sql請求

    return redirect('/books/')
