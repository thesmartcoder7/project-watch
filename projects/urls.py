
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='projects-home' ),
    path('profile/', views.profile, name='projects-profile'),
    path('project/', views.project, name='projects-project'),
    path('user/', views.logged_user, name='projects-user'),
]
