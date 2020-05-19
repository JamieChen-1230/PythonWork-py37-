from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


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


# 概念： 在第n個位置，向後顯示m條數據
class MyLimitOffsetPagination(LimitOffsetPagination):
    # 每次取幾條數據
    default_limit = 3
    # 用戶自定義limit，可以透過get傳參(key=limit)，來獲取更多的數據量
    limit_query_param = 'limit'  # 默認也叫limit
    # 用戶自定義offset，可以透過get傳參(key=offset)，來設定初始位置
    offset_query_param = 'offset'  # 默認也叫offset，offset:從第幾個位置後開始取
    # 最大獲取量
    max_limit = 10


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
