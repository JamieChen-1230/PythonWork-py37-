from django.db import models
# @python_2_unicode_compatible：使用此裝飾器後，能讓資料表與python2兼容
from django.utils.six import python_2_unicode_compatible
from django.conf import settings


# @python_2_unicode_compatible：使用此裝飾器後，能讓資料表與python2兼容
@python_2_unicode_compatible
class Category(models.Model):
    """
    商品類別：筆電、平板、主機等
    """
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # 直接使用對象時，會調用__str__
    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Manufacturer(models.Model):
    """
    製造商
    """
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(blank=True, null=True, max_length=200, upload_to='manufacturer/uploads/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Product(models.Model):
    """
    產品
    """
    model = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(max_length=200, upload_to='product/uploads/%Y/%m/%d/')
    # DecimalField小數：max_digits(整數+小數位數)、decimal_places(小數點最多幾位)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    sold = models.PositiveIntegerField(default=0)
    # related_name為反向關聯要用的字段，若沒設置則默認為表名_set
    category = models.ForeignKey(to=Category, related_name='product_in', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(to=Manufacturer, related_name='product_of', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model


@python_2_unicode_compatible
class DeliveryAddress(models.Model):
    """
    收貨地址
    """
    # settings.AUTH_USER_MODEL就是auth.User表
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='delivery_address_of',)
    contact_person = models.CharField(max_length=200)
    contact_mobile_phone = models.CharField(max_length=200)
    delivery_address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.delivery_address


@python_2_unicode_compatible
class UserProfile(models.Model):
    """
    用戶資料
    """
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile_of',)
    mobile_phone = models.CharField(blank=True, null=True, max_length=200)
    nickname = models.CharField(blank=True, null=True, max_length=200)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(blank=True, null=True, max_length=200, upload_to='user/uploads/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    delivery_address = models.ForeignKey(to=DeliveryAddress, related_name='user_delivery_address',
                                         on_delete=models.CASCADE, blank=True, null=True,)


@python_2_unicode_compatible
class Order(models.Model):
    """
    訂單
    """
    STATUS_CHOICES = (
        ('0', 'new'),
        ('1', 'not paid'),
        ('2', 'paid'),
        ('3', 'transport'),
        ('4', 'closed'),
    )
    status = models.CharField(choices=STATUS_CHOICES, default='0', max_length=2)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_of',)
    remark = models.TextField(blank=True, null=True)
    product = models.ForeignKey(to=Product, related_name='order_product', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    address = models.ForeignKey(to=DeliveryAddress, related_name='order_address', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'order of %d' % self.user.id
