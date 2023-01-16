from django.urls import path
from singuplogin import views

urlpatterns = [
    path("", views.login_page, name="login_page")
]