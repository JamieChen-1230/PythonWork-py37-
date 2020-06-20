from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from snippetsapp.serializers import UserSerializer, SnippetSerializer
from snippetsapp import models
from django.contrib.auth.models import User


# /snippets/頁面
# /snippets/<snippet_id>/頁面
class SnippetViewSet(viewsets.ModelViewSet):
    """
    Snippets頁面
    """
    queryset = models.Snippet.objects.all()
    serializer_class = SnippetSerializer
    # IsAuthenticatedOrReadOnly表若沒登入只能唯讀
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # /snippets/<snippet_id>/highlight/頁面
    # 詳情路由：使用@action((detail=True)裝飾函數，此函數名為路徑字段
    # renderer_classes為渲染器(StaticHTMLRenderer是用來顯示靜態HTML文檔的)
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        # 獲取當前snippet對象
        snippet = self.get_object()
        # 顯示snippet.highlighted
        return Response(snippet.highlighted)

    # 覆寫perform_create()方法，perform_create方法是在使用create操作時負責進行數據持久化動作
    def perform_create(self, serializer):
        # 在持久化前，先把owner字段賦值為當前登入用戶
        serializer.save(owner=self.request.user)


# /users/頁面
# /users/<user_id>/頁面
# ReadOnlyModelViewSet：唯讀的ModelViewSet
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Users頁面
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
