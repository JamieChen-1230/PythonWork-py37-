from django.urls import path, include
from snippetsapp import views
from rest_framework import routers


# 路由器
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'snippets', views.SnippetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


# 原理(一一對應，創建請求方法對應之CBV之方法)
# from snippetsapp.views import SnippetViewSet, UserViewSet
# from rest_framework import renderers
# from rest_framework.urlpatterns import format_suffix_patterns
#
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# urlpatterns = format_suffix_patterns([
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])
