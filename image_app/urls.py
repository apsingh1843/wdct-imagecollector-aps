from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('userform/', views.userform, name="userform"),
]
