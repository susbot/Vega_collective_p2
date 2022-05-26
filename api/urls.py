from django.urls import path
from.views import APIList, APIDetail

urlpatterns = [
    path('<int:pk>/', APIDetail.as_view()),
    path('', APIList.as_view()),
]