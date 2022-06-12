from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='users-signup'),
    path('signin/', views.signin, name='users-signin')
]
