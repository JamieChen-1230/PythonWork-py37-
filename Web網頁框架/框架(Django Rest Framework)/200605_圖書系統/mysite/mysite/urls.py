from django.contrib import admin
from django.urls import path, re_path, include
from app01 import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'bookshops', viewset=views.BookshopsView)
router.register(r'books', viewset=views.BooksView)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'api/bookshops/(?P<pk>\d+)/books/$', views.BookshopsBooksView.as_view({
        'get': 'list',  # 獲取單條數據
    })),
    re_path(r'api/bookshops/(?P<pk>\d+)/books/(?P<book_id>\d+)/$', views.BookshopsBooksView.as_view({
        'get': 'retrieve',  # 獲取單條數據
    })),
    re_path(r'api/', include(router.urls)),
]
