from django.urls import path
from singuplogin import views

urlpatterns = [
    path("", views.singup_page, name="singup_page")
]