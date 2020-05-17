from rest_framework import serializers
from api import models


class RolesSerializer(serializers.Serializer):
    # 字段名必須跟數據庫一致，除非有加source參數
    id = serializers.IntegerField()
    title = serializers.CharField()

# 方法一：
# class UsersSerializer(serializers.Serializer):
#     # 字段名必須跟數據庫一致，除非有加source參數
#     # 一般字段
#     id = serializers.IntegerField()
#     username = serializers.CharField()
#     password = serializers.CharField()
#     # choices字段
#     user_type_num = serializers.CharField(source='user_type')  # source表示要去哪個字段
#     # get_字段名_display： 他會先取出字段名對應的數據，但如果是可被執行的話，就會繼續找下去
#     user_type = serializers.CharField(source='get_user_type_display')  # 取出來的是VIP、SIP等
#     # 一對多字段
#     groups = serializers.CharField(source='group.title')  # 取出外鍵對象.title字段
#     # 多對多字段
#     rls = serializers.SerializerMethodField()  # 自定義顯示
#
#     def get_rls(self, obj):  # 自定義顯示的方法，名稱為get_字段名
#         roles_obj_list = obj.roles.all()
#         ret = []
#         for item in roles_obj_list:
#             ret.append({'id': item.id, 'title': item.title})
#         return ret  # 要顯示的數據


# 方法二(優)：
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
