from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='users-signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='users/login.html'), name='users-signin'),
    path('signout/', auth_views.LogoutView.as_view(), name='users-signout'),
]
