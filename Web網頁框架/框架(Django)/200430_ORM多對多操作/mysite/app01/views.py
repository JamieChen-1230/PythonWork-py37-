from django.shortcuts import render, HttpResponse, redirect
from app01 import models


def books(request):
    book_list = models.Books.objects.all()
    return render(request, 'books.html', locals())


def add_book(request):
    # ---透過ManyToManyField建---
    # # obj_book.authors.add()綁定多對多關係
    # obj_book = models.Books.objects.get(id=3)
    # obj_author = models.Author.objects.all()
    # obj_book.authors.add(*obj_author)  # obj_author因為是集合對象所以要加個*

    # ---自己建表---
    # Book_author.objects.create(book_id=4, author_id=3)
    return redirect('/books/')


def update_book(request):
    models.Books.objects.filter(name='c++').update(price=666)
    return redirect('/books/')


def delete_book(request):
    # 刪除
    models.Books.objects.filter(name='js').delete()

    # # obj_book.authors.remove()刪除多對多關係
    # obj_book = models.Books.objects.get(id=3)
    # obj_author = models.Author.objects.all()
    # obj_book.authors.remove(*obj_author)
    return redirect('/books/')


def search_book(request):
    # ---透過ManyToManyField建---(Good)
    # obj_book = models.Books.objects.get(id=3)
    # # obj_book.authors.all()為書籍對象的所有關聯作者對象
    # queryset_author = obj_book.authors.all().values('name')
    # print(queryset_author)
    # 找出jamie出的書(1)
    # obj_author = models.Author.objects.get(name="jamie")
    # query_book = obj_author.books_set.all().values('name')
    # print(query_book)
    # 找出jamie出的書(2)：雙下滑線查詢，形式和一對多相同
    # queryset_book = models.Books.objects.filter(authors__name='jamie').values('name', 'price')
    # print(queryset_book)

    # ---自己建表---
    # obj_book = models.Books.objects.get(id=2)
    # print(obj_book.book_author_set.all()[0].author.name)
    # 找出nb出的書
    # queryset_book = models.Books.objects.filter(book_author__author__name='nb').values('name', 'price')
    # print(queryset_book)

    return redirect('/books/')
