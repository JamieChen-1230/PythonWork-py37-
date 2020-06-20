import datetime
from rest_framework import generics
from rest_framework import permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from computerapp.serializers import ProductListSerializer, ProductRetrieveSerializer, UserProfileSerializer, UserSerializer, DeliveryAddressSerilizer, OrderListSerializer, OrderCreateSerializer, UserInfoSerializer
from computerapp.models import Product, UserProfile, DeliveryAddress, Order

import logging
LOG_FILENAME = 'shop.log'

# logging.basicConfig(filename=LOG_FILENAME,level = logging.DEBUG)
logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)


class ProductListView(generics.ListAPIView):
    """產品列表 """
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permissin_classes = (permissions.AllowAny,)  # AllowAny誰都可以訪問，DRF默認也是這個權限
    ordering_fields = ('category', 'manufacturer', 'created', 'sold',)  # 提供給用戶可以排序的字段
    search_fields = ('description', 'model')  # 提供給用戶可以查詢的字段
    filter_backends = (OrderingFilter, SearchFilter,)  # 須加上這行，才能讓用戶進行排序和搜索
    ordering = ('-id',)  # 照id倒敘排序(默認)
    pagination_class = LimitOffsetPagination


class ProductListByCategoryView(generics.ListAPIView):
    """按類別來分類之產品列表 """
    serializer_class = ProductListSerializer
    permissin_classes = (permissions.AllowAny,)
    ordering_fields = ('category', 'manufacturer', 'created', 'sold', 'stock', 'price',)
    search_fields = ('description',)
    filter_backends = (OrderingFilter, SearchFilter)
    ordering = ('id',)

    # 覆寫get_queryset()方法，get_queryset()方法是用來獲取queryset的
    def get_queryset(self):
        """有類別的話，則須過濾類別條件"""
        # query_params為查詢參數(get的話會顯示在URL上)
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = Product.objects.filter(category=category)
        else:
            queryset = Product.objects.all()
        return queryset


class ProductListByCategoryManufacturerView(generics.ListAPIView):
    """按類別和製造商來分類之產品列表 """
    serializer_class = ProductListSerializer
    permissin_classes = (permissions.AllowAny,)
    ordering_fields = ('category', 'manufacturer', 'created', 'sold', 'stock', 'price',)
    search_fields = ('description',)
    filter_backends = (OrderingFilter, SearchFilter)
    ordering = ('id',)

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        manufacturer = self.request.query_params.get('manufacturer', None)
        print(manufacturer)

        if category is not None:
            queryset = Product.objects.filter(category=category, manufacturer=manufacturer)
        else:
            queryset = Product.objects.all()
        return queryset


class ProductRetrieveView(generics.RetrieveAPIView):
    """產品詳細資料"""
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveSerializer
    permission_classes = (permissions.AllowAny,)


class UserInfoView(APIView):
    """用戶基本信息"""
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        user = self.request.user
        serializer = UserInfoSerializer(user)
        return Response(serializer.data)


class UserProfileRUView(generics.RetrieveUpdateAPIView):
    """用戶其他信息"""
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        user = self.request.user
        obj = UserProfile.objects.get(user=user)
        return obj


class UserCreateView(generics.CreateAPIView):
    """創建用戶"""
    serializer_class = UserSerializer


class DeliveryAddressLCView(generics.ListCreateAPIView):
    '''收货地址LC'''
    serializer_class = DeliveryAddressSerilizer
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        user = self.request.user
        queryset= DeliveryAddress.objects.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        user=self.request.user
        s=serializer.save(user=user)
        profile=user.profile_of
        profile.delivery_address=s
        profile.save()


class DeliveryAddressRUDView(generics.RetrieveUpdateDestroyAPIView):
    '''收货地址RUD'''
    serializer_class = DeliveryAddressSerilizer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        user = self.request.user
        # obj =DeliveryAddress.objects.get(user=user)
        try:
            obj=DeliveryAddress.objects.get(id=self.kwargs['pk'],user=user)
        except Exception as e:
            raise NotFound('no found')
        return obj


class CartListView(generics.ListAPIView):
    '''购物车列表'''
    serializer_class=OrderListSerializer
    permissin_classes=(permissions.IsAuthenticated,)

    def get_queryset(self):
       user=self.request.user
       queryset=Order.objects.filter(user=user,status='0')
       return queryset


class OrderListView(generics.ListAPIView):
    '''订单列表'''
    serializer_class=OrderListSerializer
    permissin_classes=(permissions.IsAuthenticated,)

    def get_queryset(self):
       user=self.request.user
       queryset=Order.objects.filter(user=user,status__in=['1','2','3','4'])
       return queryset


class OrderCreateView(generics.CreateAPIView):
    '''创建订单'''
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user
        product=serializer.validated_data.get('product')
        serializer.save(user=user,price=product.price,address=user.profile_of.delivery_address,status='0',)

        logging.info('user %d cart changed,product %d related.Time is %s.', user.id, product.id, str(datetime.datetime.now()))


# class OrderRUDView(generics.RetrieveUpdateDestroyAPIView):
#     '''Order'''
#     serializer_class = OrderRUDSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get_object(self):
#         user = self.request.user
#         obj= Order.objects.get(user=user,id=self.kwargs['pk'])
#         return obj
#
#     def perform_update(self, serializer):
#         user = self.request.user
#         serializer.save(user=user,sttus='1')
