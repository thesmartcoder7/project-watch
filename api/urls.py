from django.urls import path
from . import views


urlpatterns = [
    path('profiles/', views.all_profiles, name='api-profiles'),
    path('projects/', views.all_projects, name='api-projects')
]
