from api import models
from api.serializers import RolesSerializer
from api.pagination import MyPageNumberPagination
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import HttpResponse
from api import tasks
from celery.result import AsyncResult


class RolesView(ModelViewSet):
    """
    mixins.CreateModelMixin,     => 添加
    mixins.RetrieveModelMixin,  => 查詢單條數據(要id)
    mixins.UpdateModelMixin,    => 更新(要id)
    mixins.DestroyModelMixin,   => 刪除(要id)
    mixins.ListModelMixin,         => 數據列表
    """
    queryset = models.Role.objects.all()
    serializer_class = RolesSerializer
    pagination_class = MyPageNumberPagination


def celery_task(request):
    import random
    x = random.randint(5, 15)
    # 使用前記得先用cmd啟動一個worker，因為celery所有任務都是給worker完成的
    task = tasks.add.delay(40, x)
    # 不能使用task.get()取值，因為如果任務要10分鐘，我們不可能等10分鐘
    # 所以要透過異步取結果(要透過task.id取)
    task_id = task.id
    response = '任務ID：' + task_id + ' 任務是： 40+' + str(x)
    
    return HttpResponse(response)


def celery_res(request, task_id):
    print('task_id', task_id)
    # 透過AsyncResult(id=task_id)異步取值
    result = AsyncResult(id=task_id)
    print('result:', result)
    print(result.ready())
    if result.ready():  # 判斷結果出來了嗎
        res = result.get()  # 還是需要用.get()去取
    else:
        res = '尚無結果'
    return HttpResponse(res)
