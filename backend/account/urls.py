from django.conf.urls import url
from django.urls import path, include
from account import views

urlpatterns = [
    path('logout/', views.logout, name ="logout"),
]