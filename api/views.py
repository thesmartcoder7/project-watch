from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from projects.models import Project
from users.models import Profile
from .serializers import *

@api_view(['GET'])
def all_profiles(request):
    profiles = Profile.objects.all()
    serialized = ProfileSerializer(profiles, many=True)
    return Response(serialized.data)


@api_view(['GET'])
def all_projects(request):
    projects = Project.objects.all()
    serialized = ProjectSerializer(projects, many=True)
    return Response(serialized.data)