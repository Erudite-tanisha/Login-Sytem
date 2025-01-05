from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('login/', views.LoginUser, name = "login"),
    path('signup/', views.Signup, name = "signup"),
    path('home/', views.HomeView, name = "home"),
    path('users/', views.getUsers, name='get_users'),
    path('users/<str:email>/', views.get_by_email, name='get_by_email'),
    path('update-user/<str:email>/', views.updateUser, name='update_user'),
    path('users/delete/<str:email>/', views.deleteUser, name='delete_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

