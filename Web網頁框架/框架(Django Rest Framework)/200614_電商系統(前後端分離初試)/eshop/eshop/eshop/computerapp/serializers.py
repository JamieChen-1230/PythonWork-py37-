from rest_framework import serializers
from django.contrib.auth.models import User
from computerapp.models import Product, Manufacturer, Category, UserProfile, DeliveryAddress, Order


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'mobile_phone', 'nickname', 'description', 'icon', 'created', 'updated']
        read_only_fields = ['user']


class UserInfoSerializer(serializers.ModelSerializer):
    profile_of = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'profile_of',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name',)
        # 添加額外關鍵字參數
        # 把密碼設為唯寫
        extra_kwargs = {'password': {'write_only': True}}

    # 覆寫create方法，為了要對密碼加密和同時創建UserProfile關聯數據
    def create(self, validated_data):
        # validated_data存放著前端傳來的數據
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # 對密碼進行加密並設置
        user.save()  # 數據持久化
        user_profile = UserProfile(user=user)  # 同時創建UserProfile關聯數據
        user_profile.save()
        return user


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('id', 'name',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'model', 'image', 'price', 'sold', 'category', 'manufacturer',)


class ProductRetrieveSerializer(serializers.ModelSerializer):
    # manufacturer = serializers.CharField(source='manufacturer.name')  # => EX:华硕
    manufacturer = ManufacturerSerializer(many=False)  # => EX:{id: 5, name: "华硕"}
    category = CategorySerializer(many=False)

    class Meta:
        model = Product
        fields = ('id', 'model', 'image', 'price', 'sold', 'category', 'manufacturer', 'description', 'created', 'updated')


class DeliveryAddressSerilizer(serializers.ModelSerializer):
    """收貨地址"""
    class Meta:
        model = DeliveryAddress
        fields = ('id', 'user', 'contact_person', 'contact_mobile_phone', 'delivery_address', 'created', 'updated',)
        read_only_fields = ('user',)


class OrderListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()
    address = DeliveryAddressSerilizer()

    class Meta:
        model = Order
        fields = ('id', 'status', 'user', 'product', 'price', 'quantity', 'remark', 'address', 'created', 'updated',)


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'status', 'user', 'product', 'price', 'quantity', 'remark', 'address', 'created', 'updated',)
        read_only_fields = ('user', 'price', 'address',)
