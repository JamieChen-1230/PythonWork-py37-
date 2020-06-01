from django.shortcuts import render, HttpResponse
import time, datetime
# Create your views here.

# # render()底層實現方法
# from django.template import Template,Context
# def show_time(req):
#     # django模板修改的视图函数
#     now=datetime.datetime.now()
#     t=Template('<html><body>现在时刻是:<h1 style="color:red">{{current_date}}</h1></body></html>')
#     c=Context({'current_date':now})
#     html=t.render(c)
#     return HttpResponse(html)


def show_time(request):
    t = datetime.datetime.now()
    return render(request, "show_time.html", {'time': t})


class Animal:
    def __init__(self, name):
        self.name = name


def variable(request):
    li = ['jamie', 'sb', 'nb']
    d = {'name': 'jamie', 'age': 12}
    obj = Animal('dog')
    test = 'hello world'
    test2 = 'h e ll o w  orld'
    t = datetime.datetime.now()
    e = ''
    a = "<a href=''>click</a>"

    return render(request, "variable.html", locals())


def label(request):
    d = {'name': 'jamie', 'age': 8}
    li = ['jamie', 'sb', 'nb']
    return render(request, "label.html", locals())

