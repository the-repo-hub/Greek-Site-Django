"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from singuplogin.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('review.urls')),
    path('login/', login_page),
    path('singup/', singup_page),
    path('logout/', logout_page),

]

#In development for Django to serve your static files, you have to include the static urls in your urls.py: