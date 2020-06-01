from django.shortcuts import render, HttpResponse, redirect
import time


# views必須有參數，用來接收客戶端的請求信息(request)
def show_time(request):
    now_time = time.asctime()

    # -----頁面渲染render-----
    # 自動找到模板路徑下的show_time.html文件，讀取並返回給用戶
    # 第一個參數必須為客戶端的請求信息(request)
    # 第二個參數為網頁
    # 第三個參數為前端要用的變數(字典形式)，key為變量名稱，value為值
    # return render(request, "show_time.html", {"t": t})
    return render(request, 'show_time.html', locals())  # locals()把此函數內所有變量渲染到模板


def no_name(request, y, m):  # 參數對應urls裡被()分組的值
    return HttpResponse("%s %s" % (y, m))


def has_name(request, year, month):  # 有命名的話，參數須跟前面命名相同
    return HttpResponse("%s %s" % (year, month))


def no_alias_register(request):
    print(request.GET)  # 取出get形式表單之資料
    # print(request.POST)  # 取出post形式表單之資料

    # 回傳路徑
    print(request.path)  # => /app01/no_alias_register/
    # 回傳包括get資訊的路徑
    print(request.get_full_path())  # => /app01/no_alias_register/?user=sb&age=87&hobby=1

    # 也能用 if request.method == "GET":
    if request.GET:
        print(request.GET.get("user"))  # => sb
        print(request.GET.get("age"))  # => 87
        return HttpResponse('no_alias_register success')

    return render(request, 'no_alias_register.html')


def alias_register(request):
    if request.GET:
        print(request.GET.get("user"))
        print(request.GET.get("age"))
        if request.GET.get("user") == 'sb':
            # render和redirect最大區別在於 (1)url是否改變 (2)login函式內的其他程序是否會被執行
            # redirect()頁面跳轉，第一個參數為路徑
            return redirect("/login/")  # 會到mysite的urls下找出/login/路徑
            # render()頁面渲染
            # return render(request, "login.html")

        return HttpResponse('alias_register success')

    return render(request, "alias_register.html")


def login(request):
    name = "sb"
    print(name)
    return render(request, "login.html", locals())
