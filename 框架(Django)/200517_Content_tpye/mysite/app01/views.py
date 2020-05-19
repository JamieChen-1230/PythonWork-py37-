from django.shortcuts import render, HttpResponse
from app01 import models


def test1(request):
    # 1.為Python添加一個價格策略
    """
    obj = models.DegreeCourse.objects.filter(title='Python').first()
    cobj = .ContentType.objects.filter(model='degreecourse').first()
    models.PricePolicy.objects.create(price=10, period=1, content_type_id=cobj.id, object_id=obj.id)
    """
    # obj = models.DegreeCourse.objects.filter(title='Python').first()
    # # 透過content_object自動幫我們去獲取obj_id和cobj_id，並填入object_id和content_type字段
    # models.PricePolicy.objects.create(price=9.9, period=30, content_object=obj)
    # models.PricePolicy.objects.create(price=19.9, period=60, content_object=obj)
    # models.PricePolicy.objects.create(price=29.9, period=90, content_object=obj)
    #
    # # 2. 為RestFramework添加一個價格策略
    # obj2 = models.Course.objects.filter(title='RestFramework').first()
    # # 透過content_object自動幫我們去獲取obj_id和cobj_id，並填入object_id和content_type字段
    # models.PricePolicy.objects.create(price=1.1, period=30, content_object=obj2)
    # models.PricePolicy.objects.create(price=11.1, period=60, content_object=obj2)
    # models.PricePolicy.objects.create(price=21.1, period=90, content_object=obj2)

    # 3. 根據課程ID獲取課程價格策略
    course = models.Course.objects.filter(id=1).first()
    # 透過設置特殊字段，內建幫我們取出。
    price_policys = course.price_policy_list.all()
    print(price_policys)

    return HttpResponse('success')
