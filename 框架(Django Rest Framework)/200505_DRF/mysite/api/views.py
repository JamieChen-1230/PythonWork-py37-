from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.versioning import BaseVersioning, QueryParameterVersioning, URLPathVersioning
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser


class UsersView(APIView):
    """
    QueryParameterVersioning：透過URL中的get參數傳參
    URLPathVersioning：在URL的路徑中傳參
    """
    # versioning_class = URLPathVersioning  # 局部使用版本。(不是列表，跟驗證等不一樣)

    def get(self, request, *args, **kwargs):
        print(request.version)  # 獲取到的版本號
        print(request.versioning_scheme)  # 所使用的版本類
        # 透過版本類中的reverse方法反向生成出當前url
        url = request.versioning_scheme.reverse(viewname='uuu', request=request)
        print(url)
        return HttpResponse('用戶列表')


class ParserView(APIView):
    """
    JSONParser：只能解析json數據
          -  'Content-Type': 'application/json'
          -  數據格式： {"name":"jj", "age":18}

    FormParser：只能解析 HTML 表单内容
         -  'Content-Type': 'application/x-www-form-urlencoded'
         -  數據格式： name=jamie&age=18&height=179

     MultiPartParser：只能解析更多部分HTML表单内容，文件上傳也能使用
        -  'Content-Type': 'multipart/form-data''
    """

    # parser_classes = [JSONParser, FormParser, MultiPartParser]  # 局部使用解析器

    def post(self, request, *args, **kwargs):
        """
                1. 獲取用戶請求
                2. 獲取用戶請求體
                3. 獲取用戶請求頭並和parser_classes進行比對，選擇要用的解析器
                4. 解析器對請求體進行解析
                5. 數據封裝到request.data
        """
        print(request.data)  # 封裝了經解析過後的數據

        return HttpResponse('ParserView')
