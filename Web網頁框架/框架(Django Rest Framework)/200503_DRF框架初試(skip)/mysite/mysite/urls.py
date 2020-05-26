from django.urls import path
from app01 import views


urlpatterns = [
    path('api/v1/dog', view=views.DogView.as_view()),
]
