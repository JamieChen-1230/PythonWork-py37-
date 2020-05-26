from django.shortcuts import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# @csrf_exempt可以讓此方法免除crsf認證
@csrf_exempt
def users(request):
    return HttpResponse("test")


# CBV(Class Base View)：通常命名時會叫做 xxxView，且必須繼承View
# @method_decorator()：在CBV中要為函數加上裝飾器的話要透過它來完成。
@method_decorator(csrf_exempt, name='dispatch')  # (推薦)也可以從這加裝飾器到dispatch方法
class StudentsView(View):
    """
    ※ 我們之所以可以做到『收到GET請求，就調用get方法』，是因為源碼裡的dispatch方法透過『反射』幫我們分配的。
         -  類似這樣實現：
                def dispatch(self, request, *args, **kwargs):
                    func = getattr(self, request.method.lower())
                    ret = func(request, *args, **kwargs)
                    return ret
    """
    # # @method_decorator()：在CBV中要為函數加上裝飾器的話要透過它來完成。
    # # 在CBV中，csrf_exempt要裝飾在dispatch方法上(而不是post方法)，且必須要透過@method_decorator()來裝飾。
    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     # 執行父類的dispatch
    #     return super(StudentsView, self).dispatch(request, *args, **kwargs)

    # 如果是GET請求則會執行這個方法。【等同於以前FBV的 if request.method=="GET":】
    def get(self, request, *args, **kwargs):
        return HttpResponse("get")

    # 如果是POST請求
    def post(self, request, *args, **kwargs):
        return HttpResponse("post")

    # 如果是PUT請求
    def put(self, request, *args, **kwargs):
        return HttpResponse("put")

    # 如果是DELETE請求
    def delete(self, request, *args, **kwargs):
        return HttpResponse("delete")
