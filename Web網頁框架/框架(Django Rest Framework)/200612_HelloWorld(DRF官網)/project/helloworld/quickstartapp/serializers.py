from rest_framework import serializers
# 導入Django內置的User表(這次專案是使用User練習)
from django.contrib.auth.models import User, Group


# 序列器：(1) 驗證用  (2) 翻譯轉換用(轉成讓前後端能溝通的格式)
# HyperlinkedModelSerializer： 繼承於ModelSerializer，並附加超連結功能
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Meta： 元數據類，用來描述外層類(UserSerializer)的類
    class Meta:
        # 定義模型
        model = User
        # 定義要顯示的字段
        # url字段是使用HyperlinkedModelSerializer就可以自動幫我們添加的，不需做額外操作
        # groups是正向查找字段，所以不用_set
        fields = ['id', 'url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Group
        # user_set 反向查找(小寫表名_set)
        fields = ['url', 'name', 'user_set']
