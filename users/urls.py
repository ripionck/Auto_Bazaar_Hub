from django.urls import path
from . import views

urlpatterns = [
    path('register_user/', views.AddUserCreateView.as_view(), name="register_user"),
    # path('register_user/', views.register_user, name="register_user"),
    
    path('login_user/', views.UserLoginView.as_view(), name="login_user")
]
