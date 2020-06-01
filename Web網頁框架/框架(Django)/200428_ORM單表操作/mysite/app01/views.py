from django.shortcuts import render, HttpResponse, redirect
from app01 import models


def books(request):
    book_list = models.Book.objects.all()
    return render(request, 'books.html', locals())


def add_book(request):
    # 時間格式必須為YYYY-MM-DD
    # 方法一
    # b = models.Book(name='test', price=10, date='1999-09-09', author='jj')
    # b.save()
    # 方法二，也可以 models.Book.objects.create(**dict)
    # models.Book.objects.create(name='test', price=10, date='1999-09-09', author='jj')
    book = {"name": 'test', "price": 10, "date": '1999-09-09', "author": 'jj'}
    models.Book.objects.create(**book)
    return redirect('/books/')


def update_book(request):
    # 方法一(只能改一個)
    # b = models.Book.objects.get(name='python')  # b為Book實例對象
    # b.date = '1000-01-01'
    # b.save()
    # print(b, type(b))  # Book object <class 'app01.models.Book'>
    # 方法二(可改多個)
    models.Book.objects.filter(name='test').update(price=666)
    return redirect('/books/')


def delete_book(request):
    models.Book.objects.filter(id=12).delete()
    return redirect('/books/')


def search_book(request):
    # filter(**kwargs): 它包含了與所給篩選條件相匹配的對象(返回集合對象QuerySet)
    # ret = models.Book.objects.filter(name='test')
    # print(ret)  # => <QuerySet [<Book: test>, <Book: test>]>

    # all(): 查詢所有結果(返回集合對象QuerySet)
    # book_list = models.Book.objects.all()[:3]  # 支持切片
    # print(book_list)  # => <QuerySet [<Book: python>, <Book: test>, <Book: js>]>

    # get(**kwargs): 返回與所給篩選條件相匹配的對象，返回結果有且只有一個，如果符合篩選條件的對象超過一個或者沒有都會拋出錯誤(返回實例對象)
    # book_obj = models.Book.objects.get(name='python')
    # print(book_obj, type(book_obj))  # => python <class 'app01.models.Book'>

    # exclude(**kwargs): 它包含了與所給篩選條件不匹配的對象(返回集合對象QuerySet)
    # book_list = models.Book.objects.exclude(author='jamie')
    # print(book_list)  # => <QuerySet [<Book: test>, <Book: js>, <Book: test>]>

    # -----------下面的方法都是對查詢的結果再進行處理:比如objects.filter.values()--------
    # values(*field): 返回一個ValueQuerySet——一個特殊的QuerySet，運行後得到的並不是一系列model的實例化對象，而是一個可迭代的字典序列
    # ret = models.Book.objects.filter(name='test').values('name', 'price')  # 字典形式
    # print(ret)  # => <QuerySet [{'price': 100, 'name': 'test'}, {'price': 100, 'name': 'test'}]>
    # ret = models.Book.objects.filter(name='test').values_list('name', 'price')  # 元組形式
    # print(ret)  # => <QuerySet [('test', 100), ('test', 100)]>

    # order_by(*field): 對查詢結果排序
    # book_list = models.Book.objects.all().order_by('price')
    # book_list = models.Book.objects.all().order_by('-price')  # 反序
    # print(book_list)  # => <QuerySet [<Book: test>, <Book: test>, <Book: js>, <Book: python>]>

    # distinct(): 從返回結果中剔除重複紀錄
    # book_list = models.Book.objects.all().values('name').distinct()
    # print(book_list)  # => <QuerySet [{'name': 'python'}, {'name': 'test'}, {'name': 'js'}]>
    # book_list = models.Book.objects.all().values('name', 'price').distinct()
    # print(book_list)  # => <QuerySet [{'price': 999, 'name': 'python'}, {'price': 100, 'name': 'test'}, {'price': 500, 'name': 'js'}, {'price': 150, 'name': 'test'}]>

    # count(): 返回數據庫中匹配查詢(QuerySet)的對像數量
    # ret = models.Book.objects.filter(name='test').count()
    # print(ret)  # => 2

    # only(*field): 只取出想要的字段名，跟values差別在於，only出來的仍是obj
    # ret = models.Book.objects.filter(name='test').only()
    # print(ret)

    # raw(sql語句): 可以使用sql語句
    # ret = models.Book.objects.raw("SELECT id,name FROM Book;")  # 一定要包含主鍵
    # print(ret)

    # ------------萬能的__------------
    # price__gt大於, price__lt小於
    # book_list = models.Book.objects.filter(price__gt=400)
    # print(book_list)  # => <QuerySet [<Book: python>, <Book: js>]>

    # id__in(id = 1 or 8)
    # book_list = models.Book.objects.filter(id__in=[1, 8])
    # print(book_list)  # => <QuerySet [<Book: python>, <Book: test>]>

    # name__icontains包含且不分大小寫, name__contains包含
    # book_list = models.Book.objects.filter(name__icontains="s")
    # print(book_list)  # => <QuerySet [<Book: test>, <Book: js>, <Book: test>]>

    return redirect("/books/")
