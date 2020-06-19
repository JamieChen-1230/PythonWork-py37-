from rest_framework import serializers
from snippetsapp.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


# 序列器：(1) 驗證用  (2) 翻譯轉換用(轉成讓前後端能溝通的格式)
# HyperlinkedModelSerializer： 繼承於ModelSerializer，並附加超連結功能
class UserSerializer(serializers.ModelSerializer):
    # Meta： 元數據類，用來描述外層類(UserSerializer)的類
    class Meta:
        # 定義模型
        model = User
        # 定義要顯示的字段
        # url字段是使用HyperlinkedModelSerializer就可以自動幫我們添加的，不需做額外操作
        # groups是正向查找字段，所以不用_set
        fields = ['id', 'username', 'email']


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'highlighted']
        # depth = 1


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
# 
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)
# 
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
