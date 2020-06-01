from django.contrib import admin
from app01 import models


# 設定admin樣式(內建)
class Bookadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'publish',)  # 更改書籍外邊列名顯示(不能加多對多的列名)
    list_editable = ('name', 'price',)  # 可在外邊直接編輯的列名
    list_per_page = 4  # 每頁顯示資料行數(默認20)
    filter_horizontal = ('authors',)   # 使多對多的選擇編輯更佳清晰
    search_fields = ('id', 'name', 'publish__name',)  # 搜尋，可透過列名('id', 'name', 'publish__name')搜尋書籍
    list_filter = ('authors', 'name', 'price',)  # 過濾，可透過('authors', 'name', 'price',)篩選書籍
    ordering = ('-price',)  # 按price排序，加'-'就是遞減
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('price information', {'fields': ['price', 'publish', 'authors'], 'classes': ['collapse']}),
    ]  # collapse摺疊


# 把表註冊到admin介面
admin.site.register(models.Author)
admin.site.register(models.Book, Bookadmin)  # 要把自定義的類傳進去
admin.site.register(models.Publisher)