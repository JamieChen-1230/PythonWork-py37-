from rest_framework.pagination import PageNumberPagination


# 概念： 看到第n頁，每頁顯示m條數據
class MyPageNumberPagination(PageNumberPagination):
    # 每頁數據量
    page_size = 3
    # 使用get傳參(key=page)來獲取分頁
    page_query_param = 'page'
    # 用戶自定義page_size，可以透過get傳參(key=size)，來獲取更多的數據量
    page_size_query_param = 'size'
    # 每頁數據量上限
    max_page_size = 10
