from django.urls import path, re_path
from api import views
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('api/v1/auth/', view=views.AuthView.as_view()),
    path('api/v1/order/', view=views.OrderView.as_view()),
    path('api/v1/userinfo/', view=views.UserInfoView.as_view()),
]
