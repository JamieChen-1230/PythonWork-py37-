from django.shortcuts import render, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):
        return HttpResponse('POST')


# @method_decorator()：在CBV中要為函數加上裝飾器的話要透過它來完成
# 在CBV中，csrf_exempt, csrf_protect要裝飾在dispatch方法上(而不是post方法)
@method_decorator(csrf_protect, name='dispatch')
class Index2View(View):
    def get(self, request):
        return render(request, 'index2.html')

    def post(self, request):
        return HttpResponse('POST2')
