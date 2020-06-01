from django.shortcuts import render, redirect


def login(request):
    print('COOKIES', request.COOKIES)
    print('SESSION', request.session)
    if request.method == 'POST':
        name = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if name == 'sb' and pwd == '123':
            # 純COOKIE(不安全)
            # ret = redirect('/index/')
            # # set_cookie(key, values, 有效存在時間(s))
            # ret.set_cookie('data', {'user': name, 'pwd': pwd}, max_age=5)  # cookie加入信息
            # return ret

            # COOKIE & SESSION
            request.session['is_login'] = True
            request.session['user'] = name

            # request.session.set_expiry(value)
            # 如果value是個整數，session會在些秒數後失效。
            # 如果value是個datatime或timedelta，session就會在這個時間後失效。
            # 如果value是0, 用戶關閉瀏覽器session就會失效。
            # 如果value是None, session會依賴全局session失效策略。
            request.session.set_expiry(10)

            return redirect('/index/')

    return render(request, 'login.html')


def index(request):
    # 純COOKIE(不安全)
    # if request.COOKIES.get('data', None):  # 沒有抓到回傳None
    #     user = request.COOKIES.get('data')
    #     return render(request, 'index.html', locals())

    # COOKIE & SESSION
    if request.session.get('is_login', None):
        user = request.session.get('user')
        return render(request, 'index.html', locals())
    else:
        return redirect('/login/')
