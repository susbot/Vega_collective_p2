"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # Points to the urls.py Incident App (Incident List)
    path('incidents/', include('incidents.urls')),

    # Default API URL - API Homepage
    path('api/v1/', include('api.urls')),

    # Default API Auth URL - Login and Logout functionality
    path('api-auth/', include('rest_framework.urls')),

    # Points to urls.py Pages app (HomePage)
    path('', include('pages.urls')),
]
