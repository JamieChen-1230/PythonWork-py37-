from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


class Course(models.Model):
    """
    普通課
    """
    title = models.CharField(max_length=32)

    """3. GenericRelation幫我們快速實現反向查找"""
    # 內建幫我們快速查找相關數據。(僅用於反向查找，不會顯示在數據表字段中)
    price_policy_list = GenericRelation('PricePolicy')


class DegreeCourse(models.Model):
    """
    學位課
    """
    title = models.CharField(max_length=32)

    # 內建幫我們快速查找相關數據。(僅用於反向查找，不會顯示在數據表字段中)
    price_policy_list = GenericRelation('PricePolicy')


class PricePolicy(models.Model):
    """
    價格策略
    """
    price = models.IntegerField()
    period = models.IntegerField()

    """1. content_type幫我們生成了價格與課程間的關聯數據表"""
    # Django內建的contenttypes設置：
    # 因為Django在建表時會自動創建一張表(ContentType)，裡面存放這所有表名稱，
    # 所以我們只要透過外建去鏈結這張表，就能從其中取得我們需要的表名稱。
    content_type = models.ForeignKey(ContentType, verbose_name="關聯的課程表名稱", on_delete=models.CASCADE)
    object_id = models.IntegerField(verbose_name="關聯表中的課程ID")

    """2. GenericForeignKey幫我們快速實現CRUD操作，關於對content_type外鍵直接幫我們處理"""
    # 內建提供幫助我們快速實現content_type操作。(這不會顯示在數據表字段中)
    content_object = GenericForeignKey('content_type', 'object_id')



