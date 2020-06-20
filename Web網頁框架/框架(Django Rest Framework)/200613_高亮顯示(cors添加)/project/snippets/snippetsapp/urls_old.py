from django.urls import path, include
from snippetsapp import views
from rest_framework import routers

# 舊版的(使用於nouse1,2)
# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]

# 路由器
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', views.api_root),  # 起始路由畫面
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('', include(router.urls), name='user-list'),
]


