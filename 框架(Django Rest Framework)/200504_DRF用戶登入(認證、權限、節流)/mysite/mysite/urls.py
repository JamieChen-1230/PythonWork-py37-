from django.urls import path
from api import views

urlpatterns = [
    path('api/v1/auth', view=views.AuthView.as_view()),
    path('api/v1/order', view=views.OrderView.as_view()),
    path('api/v1/userinfo', view=views.UserInfoView.as_view()),
]
