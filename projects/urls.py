
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='projects-home' ),
    path('profile/', views.profile, name='projects-profile'),
    path('project/<project_id>/', views.project, name='projects-project'),
    path('user/', views.logged_user, name='projects-user'),
    path('add_project/', views.add_project, name='projects-add-project'),
    path('edit-user/', views.edit_profile, name='projects-edit-user'),
     path('search/', views.search, name='projects-search')
]
