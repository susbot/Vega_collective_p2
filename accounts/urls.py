from django.urls import path
from .views import SignUpView

urlpatterns = [

    # Default Sign Up Page
    path('signup/',
         SignUpView.as_view(),
         name='signup')
]