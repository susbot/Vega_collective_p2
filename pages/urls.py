from django.urls import path
from .views import HomePageView

urlpatterns = [

    # Default Homepage URL
    path('',
         HomePageView.as_view(),
         name='home'),
]