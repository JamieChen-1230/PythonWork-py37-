from django.shortcuts import render

# Create your views here.
from django.views import View


class Index_View(View):
    def get(self, request):
        return render(request, 'index.html')
