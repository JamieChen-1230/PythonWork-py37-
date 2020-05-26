from django.shortcuts import render, HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# 以前實現api接口必須創建四個url和view。
def get_order(request):
    return HttpResponse('獲取訂單')
def add_order(request):
    return HttpResponse('創建訂單')
def del_order(request):
    return HttpResponse('刪除訂單')
def update_order(request):
    return HttpResponse('更新訂單')


################################################################
# 現在根據restful規範整合在一個url和view。(現在逐漸成為主流)
def order(request):
    # restful規範(一)：根據method不同，做不同操作。
    if request.method == "GET":
        return HttpResponse('獲取訂單')
    elif request.method == "POST":
        return HttpResponse('創建訂單')
    elif request.method == "PUT":
        return HttpResponse('更新訂單')
    elif request.method == "DELETE":
        return HttpResponse('刪除訂單')


################################################################
# 根據restful規範整合在一個url和view。(現在逐漸成為主流)
# 更好的是用CBV來實現
@method_decorator(csrf_exempt, name='dispatch')
class OrderView(View):
    # ※ restful規範(一)：根據method不同，做不同操作。
    # GET：取出資源(一項或多項)
    def get(self, request, *args, **kwargs):
        return HttpResponse('獲取訂單')

    # POST：新建資源
    def post(self, request, *args, **kwargs):
        return HttpResponse('創建訂單')

    # PUT：更新資源(全部更新)
    def put(self, request, *args, **kwargs):
        return HttpResponse('更新訂單')

    # PATCH：更新資源(局部更新)
    def patch(self, request, *args, **kwargs):
        return HttpResponse('更新訂單')

    # DELETE：刪除資源
    def delete(self, request, *args, **kwargs):
        return HttpResponse('刪除訂單')
