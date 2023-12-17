from django.urls import path
from . import views


urlpatterns = [
    path('register_user/', views.UserCreateView.as_view(), name="register_user"),
    path('login_user/', views.UserLoginView.as_view(), name="login_user"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('profile/', views.profile, name="user_profile")
]
