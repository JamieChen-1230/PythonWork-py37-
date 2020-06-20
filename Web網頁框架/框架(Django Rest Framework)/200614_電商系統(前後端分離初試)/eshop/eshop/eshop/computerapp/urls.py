from rest_framework.urlpatterns import format_suffix_patterns
from computerapp import views
from django.urls import re_path


urlpatterns = [
    re_path(r'^user_info/$', views.UserInfoView.as_view(), name='user_info'),
    re_path(r'^product_list/$', views.ProductListView.as_view(), name='product_list'),
    re_path(r'^product_list_by_category/$', views.ProductListByCategoryView.as_view(), name='productlistbycategory'),
    re_path(r'^product_list_by_category_manufacturer/$', views.ProductListByCategoryManufacturerView.as_view(), name='product_list_by_category_manufacturer'),
    re_path(r'^product_retrieve/(?P<pk>[0-9]+)/$', views.ProductRetrieveView.as_view(), name='product_retrieve'),
    # re_path(r'^user_profile_ru/(?P<pk>[0-9]+)/$', views.UserProfileRUView.as_view(), name='user_profile_ru'),
    re_path(r'^user_profile_ru/$', views.UserProfileRUView.as_view(), name='user_profile_ru'),
    
    re_path(r'^user_create/$', views.UserCreateView.as_view(), name='user_create'),
    re_path(r'^delivery_address_lc/$', views.DeliveryAddressLCView.as_view(), name='delivery_address_lc'),
    re_path(r'^delivery_address_rud/(?P<pk>[0-9]+)/$', views.DeliveryAddressRUDView.as_view(), name='delivery_address_rud'),
    re_path(r'^cart_list/$', views.CartListView.as_view(), name='cart_list'),
    re_path(r'^order_list/$', views.OrderListView.as_view(), name='order_list'),
    re_path(r'^order_create/$', views.OrderCreateView.as_view(), name='order_create'),
]

