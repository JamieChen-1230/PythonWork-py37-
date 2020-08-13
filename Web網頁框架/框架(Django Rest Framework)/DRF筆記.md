# Django Rest FrameWork基礎筆記

[![hackmd-github-sync-badge](https://hackmd.io/Gx1LYIs3Tk2VFwyoizxYfQ/badge)](https://hackmd.io/Gx1LYIs3Tk2VFwyoizxYfQ)


&emsp;
## 認證(EX:用戶登入)：【先做認證，在做權限】
### 一、使用：
- 創建類：
    - 繼承BaseAuthentication，並實現authenticate方法
- 返回值(三種)：
    - None：
        - 自己不處理，交給下認證來處理
    - 拋出異常：
        ```python
        from rest_framework import exceptions
        raise exceptions.AuthenticationFailed('用戶驗證失敗')
        ```
    - (元素1, 元素2)：
        - 元素1賦值給request.user；元素2賦值給request.auth
- 局部使用(在view中加入靜態字段authentication_classes)：
    ```python
    class OrderView(APIView):
        authentication_classes = [MyAuthentication, ]
    ```
- 全局使用(加到settings.py)：
    ```python
    REST_FRAMEWORK = {
        # 全局使用認證類(若想讓view不使用全局認證類，則在其中加入authentication_classes=[])
        # 通常不會寫到views中，而是會再另外創一個py檔(EX:auth.py)
        "DEFAULT_AUTHENTICATION_CLASSES": ('api.utils.auth.MyAuthentication', )  
    }
    ```
### 二、源碼流程：
- 從view中的dispatch()進入
    - 封裝到request
        - 獲取所有定義的認證類(全局/局部定義的)，在通過列表生成式(列表推導)創建了各個認證類之對象
    - initial
        - perform_authentication
            - request.user (在內部循環了認證類的所有對象)
### 三、內置類：
```python
class BaseAuthentication(object):
    # 具體做認證操作的方法
    def authenticate(self, request):
        raise NotImplementedError(".authenticate() must be overridden.")
    # 當認證失敗時，給瀏覽器返回的響應頭
    def authenticate_header(self, request):
        pass
```
### 四、用戶類別：
- 遊客(Anonymous user)：代表校驗通過，直接進入下一步校驗（權限校驗）
- 合法用戶：代表校驗通過，將用戶存儲在request.user中，再進入下一步校驗（權限校驗）
- 非法用戶：代表校驗失敗，拋出異常，返回403權限異常結果



&emsp;
## 權限(EX:用戶等級權限)：【先做認證，在做權限】
### 一、使用：不同視圖不同權限可以訪問
- 創建類：
    - 繼承BasePermission，並實現has_permission方法
- 返回值(兩種)：
    - True：有權限
    - False：無權限
- 局部使用(在view中加入靜態字段permission_classes)：
    ```python
    class OrderView(APIView):
        permission_classes = [OtherPermission, ]
    ```
- 全局使用(加到settings.py)：
    ```python
    REST_FRAMEWORK = {
        # 全局使用認證類(若想讓view不使用全局認證類，則在其中加入authentication_classes=[])
        "DEFAULT_PERMISSION_CLASSES": ('api.utils.permission.SVIPPermission',)
    }
    ```
### 二、源碼流程：
- 從view中的dispatch()進入
    - initial
        - check_permissions
            - for permission in self.get_permissions(): (循環了權限類的所有對象)
### 三、內置類：
```python
class BasePermission(object):
    # 具體做權限操作的方法
    def has_permission(self, request, view):
        return True
    def has_object_permission(self, request, view, obj):
        return True
```



&emsp;
## 節流(EX:訪問頻率限制)：
### 一、使用：
- 創建類：
    - 繼承BaseThrottle，並實現allow_request方法
    - (優)繼承SimpleRateThrottle，並實現scope屬性(setting.py中的key)和get_cache_key方法
- 返回值(兩種)：
    - True：可繼續訪問
    - False：訪問頻率太高，不可繼續訪問
- 局部使用(在view中加入靜態字段throttle_classes)：
    ```python
    class OrderView(APIView):
        throttle_classes = [VisitThrottle, ]
    ```
- 全局使用(加到settings.py)：
    ```python
    REST_FRAMEWORK = {
        # 通常不會寫到views中，而是會再另外創一個py檔(EX:throttle.py)
        'DEFAULT_THROTTLE_CLASSES': ('api.utils.throttle.VisitThrottle',),  
        # 使用內置的訪問節流器(SimpleRateThrottle)，需要設置訪問的頻率
        'DEFAULT_THROTTLE_RATES': {
            'ip': '3/m',   # ip為自定義字段，3/m表示一分鐘三次
            'username': '10/m',
        },  # 若繼承SimpleRateThrottle的話就必須設置
    }
    ```
### 二、源碼流程：
- 從view中的dispatch()進入
    - initial
        - check_throttles
            - for throttle in self.get_throttles() (循環了節流器類的所有對象)

### 三、內置類：
```python
# SimpleRateThrottle的歷史紀錄是存在Django中的內置緩存裡
class VisitThrottle(SimpleRateThrottle):  # 只要實現這樣就能得到一個訪問節流器了
    # 作為key，到時要到settings.py裡取我們設定的頻率
    scope = 'ip'

    # get_cache_key表示訪問紀錄的key，這要我們自己覆寫
    def get_cache_key(self, request, view):
        # 使用用戶IP當作key
        return self.get_ident(request)  # 父類的get_ident(request)方法可以直接取IP
```



&emsp;
## 版本：
### 一、方式：
- 在URL中透過get參數傳參。
    - URL：
        - http://127.0.0.1:8000/api/users/?version=v1
    - 類： 
        - 使用DRF內置提供的QueryParameterVersioning
        - 配置文件(settings.py):
            ```python
            REST_FRAMEWORK = {
                'DEFAULT_VERSION': 'v1',  # 默認版本號
                'ALLOWED_VERSIONS': ['v1', 'v2'],  # 允許的版本號
                'VERSION_PARAM': 'version',  # 在get請求中版本號的key(EX: ?version)
            }
            ```
        - 路由設置(urls.py)：
            ```python
            urlpatterns = [
                path('users/', views.UsersView.as_view()),
            ]
            ```
- (推薦)在URL的路徑中傳參。
    - URL：
        - http://127.0.0.1:8000/api/v1/users/
    - 類： 
        - 使用DRF內置提供的URLPathVersioning
        - 配置文件(settings.py)：
            ```python
            REST_FRAMEWORK = {
                'DEFAULT_VERSION': 'v1',  # 默認版本號
                'ALLOWED_VERSIONS': ['v1', 'v2'],  # 允許的版本號
                'VERSION_PARAM': 'version',  # 在get請求中版本號的key(EX: ?version)
            }
            ```
        - 路由設置(urls.py)：
            ```python
            urlpatterns = [
                # re_path:要使用正則表達式時使用
                re_path(r'^(?P<version>[v1|v2]+)/users/$', views.UsersView.as_view()),
            ]
            ```
### 二、使用：
- 透過版本類中的reverse方法反向生成出當前url
    - url = request.versioning_scheme.reverse(viewname='uuu', request=request)
- 創建類： 
    - 不需要自定義，內建的很夠用了。
- 局部使用(在view中加入靜態字段versioning_class)：
    ```python
    class UsersView(APIView):
        versioning_class = URLPathVersioning
    ```
- 全局使用(加到settings.py)：
    ```python
    REST_FRAMEWORK = {
        # 全局使用版本號
        'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
        'DEFAULT_VERSION': 'v1',  # 默認版本號
        'ALLOWED_VERSIONS': ['v1', 'v2'],  # 允許的版本號
        'VERSION_PARAM': 'version',  # 在get請求中版本號的key
    }
    ```
### 三、源碼流程：
- 從view中的dispatch()進入
    - initial
        - determine_version(返回版本號和所使用的版本類)



&emsp;
## 解析器：【對請求體數據進行解析】
### 一、前戲(Django的request.POST和request.BODY)：
- request.POST中會有值的條件(值為去request.body中解析出來的數據)：
    1. 請求頭中的Content-Type須為 application/x-www-form-urlencoded。
    2. 請求體中的數據格式須為：
        - 範例：name=jamie&age=18&height=179
- 什麼場合會有值：
    - form表單提交(默認情況下)
    - ajax提交(默認情況下)
- 什麼場合不會有值：
    - 解決方法
        - 使用解析器
    - 範例：
        ```javascript
        $.ajax({
            url: ... ,
            type: 'POST',
            headers: {'Content-Type': 'application/json'},  # 但請求頭不符合條件
            data: {'name': 'jamie', 'age': 18},  # 內部會自動轉換為name=jamie&age=18(符合條件)
        })
        ```
    - 範例二：
        ```javascript
        $.ajax({
            url: ... ,
            type: 'POST',
            data: JSON.stringify({'name': 'jamie', 'age': 18}),  # 數據格式不符合條件
        })
        ```
### 二、流程：
1. 獲取用戶請求
2. 獲取用戶請求體
3. 獲取用戶請求頭並和parser_classes進行比對，選擇要用的解析器
4. 解析器對請求體進行解析
5. 數據封裝到request.data

### 三、使用：
- 創建類： 
    - 不需要自定義，內建的很夠用了
- 局部使用(在view中加入靜態字段parser_classes)：
    ```python
    class ParserView(APIView):
        parser_classes = [JSONParser, FormParser, MultiPartParser]
    ```
- 全局使用(加到settings.py)：
    ```python
    REST_FRAMEWORK = {
        'DEFAULT_PARSER_CLASSES': (
            'rest_framework.parsers.JSONParser',
            'rest_framework.parsers.FormParser',
            'rest_framework.parsers.MultiPartParser',
        ),
    }
    ```
### 四、源碼流程：
- 從view中的dispatch()進入
    - 封裝到request
        - 獲取所有定義的解析器類(全局/局部定義的)，在通過列表生成式(列表推導)創建了各個解析器類之對象



&emsp;
## 序列化：
### 一、序列化類：
1. 繼承內置類：
    - 方法一(繼承serializers.Serializer)：
        ```python
        class UsersSerializer(serializers.Serializer):
            # 字段名必須跟數據庫一致，除非有加source參數
            # 一般字段
            id = serializers.IntegerField()
            username = serializers.CharField()
            password = serializers.CharField()
            # choices字段
            user_type_num = serializers.CharField(source='user_type')  # source表示數據庫的某個字段
            # get_字段名_display： 他會先取出字段名對應的數據，但如果是可被執行的話，就會繼續找下去
            user_type = serializers.CharField(source='get_user_type_display')  # 取出來的是VIP、SIP等
            # 一對多字段
            groups = serializers.CharField(source='group.title')  # 取出外鍵對象.title字段
            # 多對多字段
            rls = serializers.SerializerMethodField()  # 自定義顯示

            def get_rls(self, obj):  # 自定義顯示的方法，名稱為get_字段名
                roles_obj_list = obj.roles.all()
                ret = []
                for item in roles_obj_list:
                    ret.append({'id': item.id, 'title': item.title})
                return ret  # 要顯示的數據
        ```
    - (推薦)方法二(繼承serializers.ModelSerializer)：
        ```python
        class UsersSerializer(serializers.ModelSerializer):
            # choices字段
            # get_字段名_display： 他會先取出字段名對應的數據，但如果是可被執行的話，就會繼續找下去
            type = serializers.CharField(source='get_user_type_display')  # 取出來的是VIP、SIP等
            # 一對多字段
            groups = serializers.CharField(source='group.title')
            # 多對多字段
            rls = serializers.SerializerMethodField()  # 自定義顯示

            def get_rls(self, obj):  # 自定義顯示的方法，名稱為get_字段名
                roles_obj_list = obj.roles.all()
                ret = []
                for item in roles_obj_list:
                    ret.append({'id': item.id, 'title': item.title})
                return ret  # 要顯示的數據

            class Meta:
                model = models.UserInfo  # 關聯的表
                # fields = '__all__'
                # 只能用於簡單的字段
                fields = ['id', 'username', 'password', 'type', 'groups', 'rls']  # 要顯示的字段
        ```
    - (推薦)方法三(繼承serializers.ModelSerializer)：
        ```python
        class UsersSerializer(serializers.ModelSerializer):
            type = serializers.CharField(source='get_user_type_display')

            class Meta:
                model = models.UserInfo  # 關聯的表
                fields = ['id', 'username', 'password', 'type', 'group', 'roles']
                # 透過設置深度可以很輕鬆的獲取關聯表的所有數據。(建議範圍1~10)
                # 但無法取到choices字段
                depth = 1  # 深度，若不想要關聯表詳細數據可以設為0
        ```
    - 方法四(透過生成鏈結進行深度查詢)：
        ```python
        class UsersSerializer(serializers.ModelSerializer):
            # lookup_field為要去深度查的外鍵字段
            # lookup_url_kwarg為url中我們設置的變量名
            # view_name為url的別名
            gp_url = serializers.HyperlinkedIdentityField(lookup_field='group_id', lookup_url_kwarg='fk', view_name='gp')

            class Meta:
                model = models.UserInfo  # 關聯的表
                fields = ['id', 'username', 'password', 'gp_url']      	  ```  
2. 字段：
    - get_字段名_display：
        ```python
        user_type = serializers.CharField(source='get_user_type_display')  # 他會先取出字段名對應的數據，但如果是可被執行的話，就會繼續找下去
        ```
    - 要取外鍵屬性之字段：
        ```python
        groups = serializers.CharField(source='group.title')   # 可透過外鍵字段.字段名
        ```
    - 自定義顯示字段：
        ```python
        rls = serializers.SerializerMethodField()  # 自定義顯示
        def get_rls(self, obj):  # 自定義顯示的方法，名稱為get_字段名
            roles_obj_list = obj.roles.all()
            ret = []
            for item in roles_obj_list:
                ret.append({'id': item.id, 'title': item.title})
            return ret  # 回傳要顯示的數據
        ```
    - 生成深度查找鏈結：
        ```python
        # lookup_field為要去深度查的外鍵字段id
        # lookup_url_kwarg為url中我們設置的變量名
        # view_name為url的別名
        gp_url = serializers.HyperlinkedIdentityField(lookup_field='group_id', lookup_url_kwarg='fk', view_name='gp')            	
        ```

### 二、源碼流程：
- 實例化：
    - 對象給Serializer類處理；Queryset給ListSerializer類處理。
    - to_representation
        - 封裝到ser.data中


### 三、作驗證規則使用：
```python
# 方法一：validators設置自定義驗證規則
class Myvalidator(object):
    def __init__(self, x):
        self.x = x  
    # 驗證規則
    def __call__(self, value):
        if not value.startswith(self.x):
            message = 'title開頭必須為 %s' % self.x
            raise serializers.ValidationError(message)

class VerifySerializer(serializers.Serializer):
    # error_messages為錯誤信息
    # 方法一：validators設置自定義驗證規則
    title = serializers.CharField(
        error_messages={'required': 'title不能為空'}, validators=[Myvalidator('jamie')])

    # (推薦)方法二：鉤子函數設置自定義驗證規則
    # def validate_字段名(self, data)，data為request.data.get(字段名)
    def validate_title(self, data):
        from rest_framework import exceptions
        if not data.endswith('老男人'):
            raise exceptions.ValidationError('title結尾必須為老男人')
        return data  # 驗證成功回傳data

class VerifyView(APIView):
    def post(self, request, *args, **kwargs):
        # request.data 為獲取經過解析器解析的數據
        ser = VerifySerializer(data=request.data)
        # 驗證
        if ser.is_valid():
            print(ser.validated_data)
        else:
            print(ser.errors)

        return HttpResponse('提交數據')
```



&emsp;
## 分頁：
### 一、分頁內置類：
1. 繼承或直接使用PageNumberPagination：
    - 概念： 
        - 看到第n頁，每頁顯示m條數據。
    - 代碼：
        ```python
        class MyPageNumberPagination(PageNumberPagination):
            # 每頁數據量
            page_size = 3
            # 使用get傳參(key=page)來獲取分頁
            page_query_param = 'page'
            # 用戶自定義page_size，可以透過get傳參(key=size)，來獲取更多的數據量
            page_size_query_param = 'size'
            # 每頁數據量上限
            max_page_size = 10

        class RolesView(APIView):
            def get(self, request, *args, **kwargs):
                # 獲取所有數據
                roles = models.Role.objects.all()
                # 創建分頁對象
                pg = MyPageNumberPagination()
                # 獲取分頁大小的數據
                page_roles = pg.paginate_queryset(queryset=roles, request=request, view=self)
                # 序列化
                ser = RolesSerializer(instance=page_roles, many=True)  # many=True表取出多條數據
                # 使用DRF分頁提供的渲染器，功能更強(幫我們生成了上下一頁)
                return pg.get_paginated_response(data=ser.data)
        ```
2.	繼承或直接使用LimitOffsetPagination：
    - 概念： 
        - 在第n個位置，向後顯示m條數據。
    - 代碼：
        ```python
        class MyLimitOffsetPagination(LimitOffsetPagination):
            # 每次取幾條數據
            default_limit = 3
            # 用戶自定義limit，可以透過get傳參(key=limit)，來獲取更多的數據量
            limit_query_param = 'limit'  # 默認也叫limit
            # 用戶自定義offset，可以透過get傳參(key=offset)，來設定初始位置
            offset_query_param = 'offset'  # 默認也叫offset，offset:從第幾個位置後開始取
            # 最大獲取量
            max_limit = 10
        ```
3. 繼承或直接使用CursorPagination：
    - 概念： 
        - 加密頁碼分頁，只能透過上下一頁進行切換，但當頁數多的話，此方法不會變慢，效率較好。
    - 代碼：
        ```python
        class MyCursorPagination(CursorPagination):
            # 加密頁碼參數(不需要改，用默認的就好
            # cursor_query_param = 'cursor'
            # 每頁大小
            page_size = 3
            # 排序規則(-id表示照倒敘的id排)
            ordering = '-id'
            # 用戶自定義page_size，可以透過get傳參(key=size)，來獲取更多的數據量
            page_size_query_param = 'size'
            # 每頁數據量上限
            max_page_size = 10
        ```
        


&emsp;
## 視圖：
1. 演變：
    - 過去：
        - (1) class MyView(View)
        - (2) class MyView(APIView)
            - 繼承：APIView繼承View
            - 代碼：
                ```python
                class RolesView(APIView):
                    def get(self, request, *args, **kwargs):
                        # 獲取所有數據
                        roles = models.Role.objects.all()
                        # 創建分頁對象
                        pg = MyCursorPagination()
                        # 獲取分頁大小的數據
                        page_roles = pg.paginate_queryset(queryset=roles, request=request, view=self)
                        # 序列化
                        ser = RolesSerializer(instance=page_roles, many=True)  # many=True表取出多條數據
                        # 使用DRF分頁提供的渲染器，功能更強(幫我們生成了上下一頁)
                        return pg.get_paginated_response(data=ser.data)
                ```
    - 無用(因為跟過去的沒差多少)：
        - (3) class MyView(GenericAPIView)
            - 繼承：GenericAPIView繼承APIView
            - 代碼：
                ```python
                from rest_framework.generics import GenericAPIView

                class RolesView(GenericAPIView):
                    queryset = models.Role.objects.all()
                    serializer_class = RolesSerializer
                    pagination_class = MyPageNumberPagination

                    def get(self, request, *args, **kwargs):
                        # 獲取數據
                        roles = self.get_queryset()
                        # 分頁
                        page_roles = self.paginate_queryset(roles)
                        # 序列化
                        ser = self.get_serializer(instance=page_roles, many=True)
                        return Response(ser.data)
                ```
            - 詳解：
                - GenericAPIView是繼承於APIView，而我們可以根據需求多繼承mixins的ListModelMixin, CreateModelMixin等類
                - URL傳遞過程中，只需調用APIView的as_view()方法即可，然後URL就會根據請求調用對應HTTP方法(EX: get, post, put, delete,...)
                - 基本代碼：
                    ```python
                    class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
                        # 不過須定義初始queryset和serializer_class
                        queryset = Snippet.objects.all()
                        serializer_class = SnippetSerializer  # 指定視圖使用的序列化器
                        # 不需在get, post方法中去ORM調用以及序列化調用(因為都封裝到了list, create等方法，這些方法在mixins中)
                        def get(self, request, *args, **kwargs):
                            return self.list(*args, **kwargs)
                        def post(self, request, *args, **kwargs):
                            return self.create(*args, **kwargs)
                    ```
                - ORM調用是透過GenericAPIView下的get_queryset()方法使用
                - 序列化對象則透過GenericAPIView下的方法：
                    - get_serializer_class()：
                        - 返回序列化器類，默認返回serializer_class
                        - 也可通過覆寫get_serializer_class()方法來應對不同情況下，使用不同序列器類
                        - 覆寫範例：
                            ```python
                            def get_serializer_class(self):
                                if self.request.user.is_staff:
                                    return FullAccountSerializer
                                return BasicAccountSerializer
                            ```
                    - get_serializer_context()：
                        - 為Serializer對象封裝一個key為context的鍵值對
                        - 該方法在提供序列化器對象的時，會向序列化器對象的context屬性補充三個數據：request、format、view，這三個數據對象可以在定義序列化器時使用
                        - 源碼：
                            ```python
                            def get_serializer_context(self):
                                return {
                                    'request': self.request,
                                    'format': self.format_kwarg,
                                    'view': self }
                            ```
                    - get_serializer()：
                        - 裡面調用了get_serializer_context()和get_serializer_class()方法
                        - 返回序列化器對象，主要用來提供給Mixin擴展類使用，如果我們在視圖中想要獲取序列化器對象，也可以直接調用此方法。
                特點整理：
                    - 定義類視圖使用的序列化器和查詢集（屬性）；
                        - queryset： 列表視圖的查詢集（queryset = xxx）
                        - serializer_class： 視圖使用的序列化器（serializer_class = sss）
                    - 分頁和過濾的控制（屬性）；
                        - pagination_class： 分頁控制類
                        - filter_backends： 過濾控制後端
                    - 配合get_obiect()使用的（屬性）；
                        - lookup_field： 查詢單一數據庫對象時使用的條件字段，默認為'pk'
                        - lookup_url_kwarg： 查詢單一數據時URL中的參數關鍵字名稱，默認與look_field相同
                    - 查詢集的獲取/更改：
                        - get_queryset(self)： 默認返回queryset屬性，可以重寫成自己需要的查詢集；
                    - 獲取序列化器對象：
                        - get_serializer()： 默認返回的是系列化器對象；
                        注意，在提供序列化器對象的時候，REST framework會向對象的context屬性補充三個數據：request、format、view，這三個數據對象可以在定義序列化器時使用，也就是說在序列化器類中，可以通過self.context['request']，獲取對應的請求對象
                    - context屬性：
                        - get_serializer_context(self)：
                        這個是給序列化器返回的一個context屬性，context屬性裡面有'request'，'format'，'view'值可以在序列化器類中使用。與5中的描述相對應
                    - 獲取序列化器；
                        - get_serializer_class(self)：獲取需要使用的序列化器，根據需求可以重寫獲取不同的序列化器；
                    - 獲取對應的模型類對象：
                        - get_object(self)： 默認使用lookup_field參數來過濾queryset。
                        若詳情訪問的模型類對像不存在，會返回404。
                        該方法會默認使用APIView提供的check_object_permissions方法檢查當前對像是否有權限被訪問。
    - 有用(當想大量自訂製查詢時能使用)：
        - (4) class MyView(GenericViewSet)
            - 繼承： GenericViewSet(ViewSetMixin, generics.GenericAPIView)
            - 路由：
                ```python
                # GenericViewSet要額外設置路由映射
                re_path(r'^(?P<version>[v1|v2]+)/roles/$', views.RolesView.as_view({'get': 'list', 'post': 'create'}))  
                ```
            - 代碼：
                ```python
                from rest_framework.viewsets import GenericViewSet

                class RolesView(GenericViewSet):
                    queryset = models.Role.objects.all()
                    serializer_class = RolesSerializer
                    pagination_class = MyPageNumberPagination

                    # 自定義名稱的get方法
                    def list(self, request, *args, **kwargs):
                        # 獲取數據
                        roles = self.get_queryset()
                        # 分頁
                        page_roles = self.paginate_queryset(roles)
                        # 序列化
                        ser = self.get_serializer(instance=page_roles, many=True)
                        return Response(ser.data)

                    # 自定義名稱的post方法
                    def create(self, request, *args, **kwargs):
                        pass
                ```
    - 現在(若不需大量自定義可以使用、開發快速)：
        - (5) class MyView(ModelViewSet)
            - 繼承： 
                - ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet)
            - 路由：
                ※ 要設置兩種網址，需要ID的和不需要的
                ※ 對應名稱只能這麼寫(因為繼承裡面的方法名是這樣寫)
                ```python
                re_path(r'^(?P<version>[v1|v2]+)/roles/$', views.RolesView.as_view({
                    'get': 'list',  # 數據列表
                    'post': 'create',  # 創建
                })),
                re_path(r'^(?P<version>[v1|v2]+)/roles/(?P<pk>\d+)/$', views.RolesView.as_view({
                    'get': 'retrieve',  # 獲取單條數據
                    'delete': 'destroy',  # 刪除
                    'put':  'update',  # 更新
                    'patch': 'partial_update',  # 局部更新
                })),
                ```
            - 代碼：
                ```python
                from rest_framework.viewsets import ModelViewSet

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
                ```



&emsp;
## 路由：
1. 演變：
    - 過去：
        -  最開始
        ```python
        re_path(r'^(?P<version>[v1|v2]+)/roles/$', views.RolesView.as_view()),
        ```
        -  細化函數分配
        ```python
        re_path(r'^(?P<version>[v1|v2]+)/roles/$', views.RolesView.as_view({
           # 也可以用這樣呈現(http://127.0.0.1:8000/api/v1/roles/?format=json)
           'get': 'list',   # 數據列表
           'post': 'create',  # 創建
       })),
        ```
        -  可以選定什麼格式呈現
        ```python
        re_path(r'^(?P<version>[v1|v2]+)/roles\.(?P<format>\w+)/$', views.RolesView.as_view({
           # 可以選定什麼格式呈現(EX: http://127.0.0.1:8000/api/v1/roles.json/)
           'get': 'list',   # 數據列表
           'post': 'create',  # 創建
       })),
        ```
    - 現在：
        -  等同於幫我們生成了以上(過去)的所有URL，但如果只想設置增刪等局部的話，還是建議用過去的方式生成。
        ```python
        from rest_framework import routers

        router = routers.DefaultRouter()
        router.register(r'roles', viewset=views.RolesView)

        urlpatterns = [
            # 使用DRF路由器幫我們生成URL
            # 使用這個就等於幫我們生成了以上全部URL
            re_path(r'(?P<version>[v1|v2]+)/', include(router.urls))
        ]
        ```
                                    
                

&emsp;
## 過濾器：pip install django-filter
1. 演變：
    - 使用DRF自定義過濾器類(低階)：
        ```python
        class RolesView(ModelViewSet):
            ...
            filter_backends = (LimitFilter,)

        class LimitFilter(BaseFilterBackend):
            # 必須實現filter_queryset()方法，並return一個queryset
            def filter_queryset(self, request, queryset, view):
                lim = request.query_params.get('lim', None)
                if lim:
                    return queryset[:int(lim)]
                return queryset
        ```
    - 使用django-filter自定義高級過濾器：
        ```python
        class RolesView(ModelViewSet):
            ...
            filter_backends = (DjangoFilterBackend,)
            filter_class = RoleFilter

        class RoleFilter(filters.FilterSet):
            # 自定義查詢字段
            # field_name為要查的字段名，lookup_expr為查找時使用的表達式，label為前端顯示的名字，required=True為必填欄位
            # 透過 d_g=&title_c=
            id_g = filters.NumberFilter(field_name="id", lookup_expr='gte', label="大於id")
            title_c = filters.CharFilter(field_name="title", lookup_expr='icontains')
            class Meta:
                model = models.Role  # 模型名
                # 透過 title__icontains=&id__gte=&id__lte=
                fields = {
                    'title': ['icontains'],  # title字段可使用icontains包含查找
                    'id': ['gte', 'lte'],  # id字段可使用gte大於等於和lte小於等於查找
                }
        ```
        - 環境(若要使用高級的過濾器必須這樣)：
        ```python
        INSTALLED_APPS = [
            ...,
            'django_filters',  # pip install django-filter
        ]
        ```


&emsp;
## 實用技巧：
1. 動態選擇使用序列器字段：
    - 透過get_serializer傳參數時，添加額外參數，並在序列器的init方法中處理
        ```python
        class RankMNView(generics.ListAPIView):
            def list(self, request, *args, **kwargs):
                ...
                # 此fields參數是自定義的，為了讓在序列化時能自定義字段
                serializer = self.get_serializer(data,
                                                 many=True,
                                                 fields=('Stno', 'ObsTime', field, 'Year', 'Month', 'Day', 'TenDays'))
        class RankMNSerializer(serializers.ModelSerializer):
            ...
            def __init__(self, *args, **kwargs):
                # 「fields」中在「self.fields」中不存在的字段將無法被序列化，也就是說「fields」中的字段須定義為「self.fields」的子集
                # 在super(父類init)執行之前，需先將「fields」參數從kwargs取出並剔除，不然傳給父類init會報錯(因為接收到了drf本身未定義的參數)
                fields = kwargs.pop('fields', None)
                super(RankMNSerializer, self).__init__(*args, **kwargs)
                if fields is not None:
                    # 從「self.fields」中剔除非「fields」中指定的字段
                    # 原始self.fields中會包括的字段有資料表的欄位和在此RankMNSerializer中定義的字段(EX: Year)
                    allowed = set(fields)
                    existing = set(self.fields.keys())
                    for field_name in existing - allowed:  # 先取差集，在剔除差集內的字段
                        self.fields.pop(field_name)
        ```

2. 自定義字段：
    - 可自定義資料表中沒有的字段欄位，這裡產生的字段也可以與(一)技巧共用
        ```python
        class RankMNSerializer(serializers.ModelSerializer):
            # 自定義額外字段
            Year = serializers.SerializerMethodField()
            Month = serializers.SerializerMethodField()

            def get_Year(self, queryset):  # DRF會自動調用get_<字段名>之方法去獲取字段值
                # 此queryset是我們view下的list方法傳給Serializer的值，所以是[{紀錄字典},{},...]形式
                return queryset.get('Year', None)
            def get_Month(self, queryset):
                return queryset.get('Month', None)
            class Meta:
                model = models.Mn
                fields = '__all__'
        ```

3. 自定義返回的資料集：
    - 通過覆寫list()方法
        ```python
        class RankMNSerializer(serializers.ModelSerializer):
            ...
            def list(self, request, *args, **kwargs):
                # 篩選出想要的資料集
                queryset = ...
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data)
        ```
4. 動態選擇不同序列器：
    - 覆寫get_serializer_class()方法
        ```python
        class RankMNSerializer(serializers.ModelSerializer):
            ...
            def get_serializer_class(self):
                if self.request.user.is_staff:
                    return FullAccountSerializer
                return BasicAccountSerializer
        ```
5. 序列器之間可互相嵌套：
    - 當然這個字段(shop)的格式也必須符合嵌套之序列器(BookshopsSerializer)
    - 此例的shop是一個外鍵，對應到Bookshops表
        ```python
        class BookshopsSerializer(serializers.ModelSerializer):
            # 更改顯示之字段名，因為前端工程師可能會要求字段規格
            shop_id = serializers.IntegerField(source='id')
            shop_name = serializers.CharField(source='title')
            class Meta:
                model = models.Bookshops  # 關聯的表
                fields = ['shop_id', 'shop_name']
        class BooksSerializer(serializers.ModelSerializer):
            ...
            shop = BookshopsSerializer(many=False)  # 嵌套另一個Serializer
            class Meta:
                model = models.Books
                fields = ['book_id', 'book_name', 'shop']
        ```

6. Views類屬性使用：
    ```python
    from rest_framework.filters import OrderingFilter, SearchFilter
    from rest_framework.pagination import LimitOffsetPagination
    class ProductListView(generics.ListAPIView):
        # 必填屬性
        queryset = Product.objects.all()
        serializer_class = ProductListSerializer
        # 可選屬性
        permissin_classes = (permissions.AllowAny,)  # AllowAny誰都可以訪問，DRF默認也是這個權限
        ordering_fields = ('category', 'manufacturer', 'created', 'sold',)  # 提供給用戶可以排序的字段
        search_fields = ('description', 'model')  # 提供給用戶可以查詢的字段
        filter_backends = (OrderingFilter, SearchFilter,)  # 須加上這行，才能讓用戶進行排序和搜索
        ordering = ('-id',)  # 照id倒敘排序(默認)
        pagination_class = LimitOffsetPagination
    ```
7. 使用路由器最好要設basename：
    ```python
    # 要設basename，因為如果沒設basename，路由器會默認使用裡面定義的queryset當作名稱，
    # 所以當沒設basename且有多個ViewSet的queryset相同時，路由給的url可能就會錯誤(會重複)
    router.register(r'Rank/yr', Rank.views.RankYrViewSet, basename='r_yr')
    router.register(r'Rank/mn', Rank.views.RankMnViewSet, basename='r_mn')
    router.register(r'Rank/dy', Rank.views.RankDyViewSet, basename='r_dy')
    router.register(r'Rank/tenday', Rank.views.RankTenDayViewSet, basename='r_tenday') 
    ```
    
    
    
###### tags: `網頁` `API` `Django`