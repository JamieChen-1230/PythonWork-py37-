from django import template
from django.utils.safestring import mark_safe

register = template.Library()   # register的名字是固定的，不可改成其他的


# 自定義過濾器
@register.filter()  # filter只能2個參數
def filter_multi(x, y):
    print(x, y)
    return x*y


# 自定義標籤
@register.simple_tag()  # simple_tag不限制參數數
def simple_tag_multi(x, y, z):
    print(x, y, z)
    return x*y*z
