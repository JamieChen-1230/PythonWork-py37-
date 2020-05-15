from django.urls import path
from app01 import views


"""
CBV調用流程：url -> xxxView.as_view() -> 返回一個view方法 -> dispatch方法(反射) -> 執行相對應動作(get, put等)
"""
urlpatterns = [
    path('users/', views.users),
    path('students/', views.StudentsView.as_view()),  # .as_view()固定寫法
]
