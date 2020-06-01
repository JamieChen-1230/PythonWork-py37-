from django.shortcuts import render, HttpResponse
from app01 import models
from django.db.models import Q, F
from django.db.models import Avg,Min,Sum,Max,Count


def index(request):
    book_list = models.Book.objects.all()
    return render(request, 'index.html', locals())


def search_book(request):
    # ----------------聚合查詢----------------
    # 所有書的平均價格
    # avg_ret = models.Book.objects.all().aggregate(Avg('price'))
    # print(avg_ret)

    # 所有書的總價格和最高價
    # sum_ret = models.Book.objects.all().aggregate(Sum('price'), Max('price'))
    # print(sum_ret)

    # nb的書總價格，nb_money為自定義名稱
    # sum_ret = models.Book.objects.filter(authors__name="jamie").aggregate(jamie_money=Sum('price'))
    # print(sum_ret)

    # ----------------分組查詢----------------
    # 先用values分組，再用annotate個別進行處理
    # 個別作者出的書的總價
    # ret = models.Book.objects.all().values('authors__name').annotate(s=Sum('price'))
    # print(ret)
    # 每個出版社最便宜的書價格
    # ret = models.Book.objects.all().values('publish__name').annotate(Min('price'))
    # print(ret)
    # 每本書的作者數量
    # ret = models.Book.objects.all().values("name").annotate(Count("authors__name"))
    # print(ret)

    # ----------------F&Q查詢----------------(可以跟一般查詢混用但要放在一般查詢前)
    # 找出書籍id大於作者id的書
    # ret = models.Book.objects.filter(id__gt=F("authors__id"))
    # print(ret)
    # 幫現有的值加上固定值
    # models.Book.objects.all().update(price=F('price')+10)  # F('price')把現有的price抓出來
    # |或
    # ret = models.Book.objects.filter(Q(price__gt=550) | Q(name='python')).values('name')
    # print(ret)
    # ~not
    # ret = models.Book.objects.filter(~Q(name='python')).values('name')
    # print(ret)
    return render(request, "index.html", locals())
