from django.contrib import admin
from computerapp.models import Product, Category, Manufacturer, UserProfile, DeliveryAddress, Order


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'mobile_phone', 'nickname', 'user',]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'price', 'category', 'manufacturer', 'sold',]
    list_editable = ['price', 'sold', 'category',]


class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'contact_person', 'contact_mobile_phone', 'delivery_address',]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'user',]


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(DeliveryAddress, DeliveryAddressAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Category, CategoryAdmin)
