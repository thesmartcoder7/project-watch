from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signup(request):
    return render(request, 'users/signup.html')


def signin(request):
    return render(request, 'users/login.html')