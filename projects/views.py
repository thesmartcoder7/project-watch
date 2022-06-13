from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return render(request, 'projects/index.html')

def profile(request):
    return render(request, 'projects/profile.html')

def project(request):
    return render(request, 'projects/project.html')

def logged_user(request):
    return render(request, 'projects/user.html')