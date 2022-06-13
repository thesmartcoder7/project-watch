
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='projects-home' ),
    path('profile/', views.profile, name='projects-profile')
]
