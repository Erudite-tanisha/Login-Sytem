from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginUser, name = "login"),
    path('signup/', views.Signup, name = "signup"),
    path('home/', views.HomeView, name = "home"),
    path('users/', views.getUsers, name='get_users'),
    path('users/<str:email>/', views.get_by_email, name='get_by_email'),
    path('update-user/<str:email>/', views.updateUser, name='update_user'),
    path('users/delete/<str:email>/', views.deleteUser, name='delete_user'),
]

