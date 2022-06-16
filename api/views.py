from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.http import JsonResponse
from projects.models import Project
from users.models import Profile
from .serializers import *

@api_view(['GET'])
def all_profiles(request):
    profiles = Profile.objects.all()
    users = User.objects.all()
    serialized_profiles = ProfileSerializer(profiles, many=True)
    serialized_users = UserSerializer(users, many=True)
    return Response(serialized_users.data)
    # return JsonResponse(serialized_profiles.data, safe=False)
    


@api_view(['GET'])
def all_projects(request):
    projects = Project.objects.all()
    serialized = ProjectSerializer(projects, many=True)
    return Response(serialized.data)