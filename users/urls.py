from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.userRegister, name='register'),
    path('auth/', views.userAuthenticate, name='auth'),
    path('myaccount/', views.MainPage.as_view(), name='myaccount'),
    path('myaccount/exit/', views.exit, name='exit'),
    path('myaccount/community/', views.Comunidade.as_view(), name='comunidade'),
]
