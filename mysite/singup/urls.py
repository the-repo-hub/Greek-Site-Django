from django.urls import path
from singup import views

urlpatterns = [
    path("", views.singup, name="singup")
]